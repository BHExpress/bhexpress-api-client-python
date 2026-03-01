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
from os import getenv
from bhexpress.api_client import ApiException

class TestObtenerDetalleBhe(AbstractBhe):
    '''
    Clase de pruebas para obtener el detalle de una BHE.
    '''

    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))

    # CASO 1: Listado de boletas
    def testObtenerDetalleBhe(self):
        '''
        Método de test que permite probar la obtención del detalle de una BHE emitida.
        '''
        # Obtención de listado de BHEs.
        listaBhes = self._listar()
        # Si la lista está vacía, no se ejecutará la prueba.
        if len(listaBhes['results']) <= 0:
            print('testObtenerDetalleBhe(): No se probó funcionalidad.')
            return
        # Obtención de número de boleta.
        BoletaNumero = listaBhes['results'][0]['numero']

        try:
            boleta = self.client.detalle(BoletaNumero)

            self.assertIsNotNone(BoletaNumero)

            if self.verbose:
                print('\ntestObtenerDetalleBhe(): boleta', boleta, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})