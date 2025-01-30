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

class TestObtenerDetalleReceptor(TestCase):
    '''
    Clase de pruebas para obtener el detalle de un receptor.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Receptores()

    def testObtenerDetalleReceptor(self):
        '''
        Método de test que permite probar el recurso de obtención de detalle
        de un receptor con el que se haya interactuado.
        '''
        try:
            # Se listan los receptores.
            receptores = self.client.receptores()
            # Si la lista está vacía, no se ejecutará la prueba.
            if len(receptores['results']) <= 0:
                print('testObtenerDetalleReceptor(): No se probó funcionalidad.')
                return
            # Se obtiene el RUT de uno de los receptores.
            receptorRut = receptores['results'][0]['rut']

            receptor = self.client.detalleReceptor(receptorRut)

            self.assertIsNotNone(receptorRut)

            if self.verbose:
                print('testObtenerDetalleReceptor(): receptor', receptor)
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
