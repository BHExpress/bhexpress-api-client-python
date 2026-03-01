#
# BHExpress: Cliente de API en Python.
# Copyright (C) BHExpress <https://www.bhexpress.cl>
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la GNU Lesser General Public License (LGPL) publicada
# por la Fundación para el Software Libre, ya sea la versión 3 de la Licencia,
# o (a su elección) cualquier versión posterior de la misma.
#
# Este programa se distribuye con la esperanza de que sea útil, pero SIN
# GARANTÍA ALGUNA; ni siquiera la garantía implícita MERCANTIL o de APTITUD
# PARA UN PROPÓSITO DETERMINADO. Consulte los detalles de la GNU Lesser General
# Public License (LGPL) para obtener una información más detallada.
#
# Debería haber recibido una copia de la GNU Lesser General Public License
# (LGPL) junto a este programa. En caso contrario, consulte
# <http://www.gnu.org/licenses/lgpl.html>.
#

import os
from os import getenv
from bhexpress.api_client import ApiException
from tests.bhe.boletas.abstract_bhe import AbstractBhe


class TestDescargarPdfBhe(AbstractBhe):
    '''
    Clase de pruebas para descargar el PDF de una BHE emitida.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        # RUT del emisor necesario para el nombre del archivo PDF.
        cls.emisorRut = getenv('BHEXPRESS_EMISOR_RUT', '').strip()

    def testDescargarPdfBhe(self):
        # Listado de BHEs emitidas.
        listaBhes = self._listar()
        # Si la lista está vacía, no se ejecutará la prueba.
        if len(listaBhes['results']) <= 0:
            print('testDescargarPdfBhe(): No se probó funcionalidad.')
            return
        # Obtención del número de la BHE.
        boletaNumero = listaBhes['results'][0]['numero']

        try:
            # Descarga de datos para el PDF.
            pdf = self.client.pdf(boletaNumero)

            # Retrocede dos niveles para salir de 'bhe/boletas' y entrar en 'archivos'
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

            # Define la carpeta de destino correcta
            output_dir = os.path.join(base_dir, 'archivos', 'bhe_emitidas_pdf')

            # Crear la carpeta si no existe
            os.makedirs(output_dir, exist_ok=True)

            # Creación del la ruta generada y nombre del archivo con la siguiente
            # nomenclatura:
            # BHEXPRESS_BHE_EMITIDA_12345678-9_bhe_123.pdf
            filename = os.path.join(
                output_dir,
                'BHEXPRESS_BHE_EMITIDA_%(emisor_rut)s_bhe_%(boleta_codigo)s.pdf' % {
                    'emisor_rut': self.emisorRut,
                    'boleta_codigo': boletaNumero
                }
            )

            # Creación del archivo PDF usando la ruta, nombre y datos obtenidos.
            with open(filename, 'wb') as f:
                f.write(pdf)

            self.assertIsNotNone(pdf)

            if self.verbose:
                print('\ntestDescargarPdfBhe(): filename', filename,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
