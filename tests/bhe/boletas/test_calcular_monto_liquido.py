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

from tests.bhe.boletas.abstract_bhe import AbstractBhe
from datetime import datetime
from os import getenv
from bhexpress.api_client import ApiException

class TestCalcularMontoLiquido(AbstractBhe):
    '''
    Clase de pruebas para calcular un monto líquido.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))

    def testCalcularMontoLiquido(self):
        '''
        Método de test que prueba el recurso de calcular el monto líquido a partir
        de un monto bruto en un periodo específico.
        '''
        # Monto bruto a convertir.
        montoBruto = 100000
        # Prueba con el primer mes del año, formato "AAAAMM".
        periodo = '%(fecha)s01' % {'fecha': datetime.now().year}
        try:
            montoLiquido = self.client.montoLiquido(montoBruto, periodo)

            self.assertIsNotNone(montoLiquido)

            if self.verbose:
                print('\ntestCalcularMontoLiquido(): monto', montoLiquido,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})