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

from .. import ApiBase
from urllib.parse import urlencode

class Receptores(ApiBase):
    '''
    Módulo que permite listar receptores con los que se haya interactuado, y obtener
    el detalle de un receptor específico.

    :param str api_token: Token de autenticación del usuario. Si no se proporciona,
    se intentará obtener de una variable de entorno.
    :param str api_url: URL base de la API. Si no se proporciona, se usará
    una URL por defecto.
    :param str api_version: Versión de la API. Si no se proporciona, se usará
    una versión por defecto.
    :param bool api_raise_for_status: Si se debe lanzar una excepción automáticamente
    para respuestas de error HTTP. Por defecto es True.
    '''

    def __init__(self):
        super().__init__()

    def receptores(self):
        '''
        Recurso que permite obtener un listado de todos los receptores con los que
        el usuario ya haya interactuado alguna vez por medio de emitir BHEs.

        :return: Respuesta JSON con la lista de receptores y el detalle.
        :rtype: dict
        '''
        url = '/bhe/receptores'

        response = self.client.get(url)

        return response.json()

    def detalleReceptor(self, rut = None, codigo = None):
        '''
        Recurso que permite obtener el detalle de un receptor específico con el
        que ya se haya interactuado.

        :param int rut: RUT del receptor a buscar.
        :param int codigo: Código del receptor. Se usa en caso de haber más
        receptores registrados con el mismo RUT (opcional).
        :return: Respuesta JSON con el detalle del receptor buscado.
        :rtype: dict
        '''
        url = '/bhe/receptores'

        if rut is not None:
            url += '/%(rut)s' % {'rut': rut}
        if codigo is not None:
            url += '/%(codigo)s' % {'codigo': codigo}

        response = self.client.get(url)

        return response.json()