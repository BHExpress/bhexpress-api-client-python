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
from bhexpress.api_client.bhe.receptores import Receptores

class TestListarReceptores(TestCase):
    '''
    Clase de pruebas para listar receptores con los que se haya interactuado.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Receptores()

    def testListarReceptores(self):
        '''
        Método de test para probar el recurso de listar receptores a los que
        se haya enviado una BHE.
        '''
        try:
            receptores = self.client.receptores()

            self.assertTrue(True)

            if self.verbose:
                print('testListarReceptores(): receptores', receptores)
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
