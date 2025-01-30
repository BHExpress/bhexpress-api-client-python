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
from datetime import datetime, timedelta
from bhexpress.api_client import ApiException
from bhexpress.api_client.bhe.boletas import Boleta

class AbstractBhe(TestCase):
    '''
    Clase abstracta para hacer pruebas a los servicios relacionados con gestión
    de boletas de honorarios electrónicas.
    '''

    client = Boleta()

    def _listar(self):
        '''
        Método protegido para listar BHEs.
        '''
        try:
            # Variable a utilizar en el diccionario de filtros.
            # Obtiene la fecha desde la variable de entorno. Si no está definida,
            # se obtiene la fecha actual menos 30 días.
            fecha_desde = getenv(
                'TEST_FECHA_DESDE', (
                    datetime.now () - timedelta(days=30)
                ).strftime('%Y-%m-%d')
            )
            # Diccionario de filtros. Variables posibles:
            # periodo: fecha formato AAAAMM.
            # fecha_desde: fecha de inicio de búsqueda, formato AAAA-MM-DD.
            # fecha_hasta: fecha de fin de búsqueda, formato AAAA-MM-DD.
            filtros = {
                'fecha_desde': fecha_desde,
                'fecha_hasta': datetime.now().strftime('%Y-%m-%d')
            }
            boletas = self.client.listar(filtros)

            return boletas
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})