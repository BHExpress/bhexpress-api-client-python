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

from os import getenv
from datetime import datetime
from bhexpress.api_client import ApiException
from tests.bhe.boletas.abstract_bhe import AbstractBhe

class TestEmitirBhe(AbstractBhe):
    '''
    Clase de pruebas para emitir una BHE.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        # RUT del emisor necesario para emisión de BHE.
        cls.rutEmisor = getenv('BHEXPRESS_EMISOR_RUT', '').strip()

    # CASO 2: Emitir una boleta
    def testEmitirBhe(self):
        # Fecha de emisión de la BHE
        fechaEmis = datetime.now().strftime('%Y-%m-%d')
        # Datos de la BHE a emitir.
        datos = {
            'Encabezado': {
                'IdDoc': {
                    'FchEmis': fechaEmis,
                    'TipoRetencion': 1
                },
                'Emisor': {
                    'RUTEmisor': self.rutEmisor
                },
                'Receptor': {
                    'RUTRecep': '66666666-6',
                    'RznSocRecep': 'Receptor generico',
                    'DirRecep': 'Santa Cruz',
                    'CmnaRecep': 'Santa Cruz'
                }
            },
            'Detalle': [
                {
                    'CdgItem': 0,
                    'NmbItem': 'Se agrega código y cantidad al item (se indica precio unitario)',
                    'QtyItem': 1,
                    'PrcItem': 1000
                },
                {
                    'NmbItem': 'Se agrega cantidad al item (se indica precio unitario)',
                    'QtyItem': 2,
                    'PrcItem': 2500
                },
                {
                    'CdgItem': 2,
                    'NmbItem': 'Caso más completo, con código, cantidad, precio y descuento porcentual',
                    'QtyItem': 2,
                    'PrcItem': 700,
                    'DescuentoPct': 10
                },
                {
                    'CdgItem': 3,
                    'NmbItem': 'Caso más completo, con código, cantidad, precio y descuento fijo',
                    'QtyItem': 2,
                    'PrcItem': 700,
                    'DescuentoMonto': 600
                }
            ]
        }
        try:
            emitir = self.client.emitir(datos)

            self.assertIsNotNone(emitir)

            if self.verbose:
                print('\ntestEmitirBhe(): emitir', emitir,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})