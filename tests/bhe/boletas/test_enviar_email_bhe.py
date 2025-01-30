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

class TestEnviarEmailBhe(AbstractBhe):
    '''
    Clase de pruebas para enviar una BHE a un correo.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        # Correo destinatario. Se debe definir como variable de entorno.
        cls.emailDestinatario = getenv('TEST_CORREO', 'correo@example.com').strip()

    def testEnviarEmailBhe(self):
        '''
        Métodos de test que permite probar el recurso de envío de una BHE a un destinatario
        por correo.
        '''
        # Obtención de listado de BHEs
        listaBhes = self._listar()

        # Si la lista está vacía, no se ejecutará la prueba.
        if len(listaBhes['results']) <= 0:
            print('testEnviarEmailBhe(): No se probó funcionalidad.')
            return
        numeroBhe = listaBhes['results'][0]['numero']

        try:
            email = self.client.email(numeroBhe, self.emailDestinatario)

            self.assertIsNotNone(numeroBhe)

            if self.verbose:
                print('\ntestEnviarEmailBhe(): email', email,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
