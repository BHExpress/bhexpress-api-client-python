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

from unittest import TestCase
from os import getenv
from bhexpress.api_client import ApiException
from bhexpress.api_client.bhe.servicios import Servicios

class TestObtenerDetalleServicio(TestCase):
    '''
    Clase de pruebas para obtener el detalle de un servicio específico.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Servicios()

    def testObtenerDetalleServicio(self):
        '''
        Método de test que permite probar el recurso de obtención de detalles de
        un servicio específico provisto por el usuario.
        '''
        # Filtros de búsqueda.
        filtros = {
            'montos_clp': 'bruto',
            'fecha': '2025-01-01'
        }
        try:
            # Obtención de lista de servicios.
            servicios = self.client.servicios()
            # Si la lista está vacía, no se ejecutará la prueba.
            if len(servicios['results']) <= 0:
                print('testObtenerDetalleServicio(): No se probó funcionalidad.')
                return
            # Obtención de código de un servicio.
            codigo = servicios['results'][0]['codigo']

            servicio = self.client.detalleServicio(codigo, filtros)

            if self.verbose:
                print('\ntestObtenerDetalleServicio(): servicio', servicio,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
