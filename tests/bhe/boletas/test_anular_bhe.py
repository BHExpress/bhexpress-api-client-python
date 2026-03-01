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
from bhexpress.api_client import ApiException
from tests.bhe.boletas.abstract_bhe import AbstractBhe

class TestAnularBhe(AbstractBhe):
    '''
    Clase de pruebas para anular una boleta de honorarios electrónica ya emitida.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))

    def testAnularBhe(self):
        '''
        Método de test que prueba el recurso para anular una BHE.
        '''
        # Obtención de lista de BHEs.
        listaBhes = self._listar()
        # Si la lista está vacía, no se ejecutará la prueba.
        if len(listaBhes['results']) <= 0:
            print('testAnularBhe(): No se probó funcionalidad.')
            return
        # Selección del BHE para anular.
        boletaNumero = listaBhes['results'][0]['numero']

        try:
            anular = self.client.anular(boletaNumero, 3)

            self.assertIsNotNone(boletaNumero)

            if self.verbose:
                print('\ntestAnularBhe(): anular', anular,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
