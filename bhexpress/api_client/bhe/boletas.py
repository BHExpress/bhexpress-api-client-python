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
import requests
from .. import ApiBase

class Boleta(ApiBase):

    def __init__(self):
        super().__init__()

    '''
    Recurso que permite obtener el listado paginado de boletas de honorarios electrónicas emitidas.

    Los parámetros de entrada son filtros para obtener boletas más específicas.

    :param str periodo: Período por el cuál consultar las boletas. Puede ser: 'AAAAMM' o 'AAAA'
    :param str fechaDesde:Fecha desde cuándo consultar las boletas. Formato: 'AAAA-MM-DD'
    :param str fechaHasta:Fecha hasta cuándo consultar las boletas. Formato: 'AAAA-MM-DD'
    :param str receptorCodigo: Código del receptor. Generalmente es el RUT del receptor sin DV.
    :return: Respuesta JSON con el listado de boletas emitidas.
    :rtype: dict
    :exception ApiException: Arroja un error cuando las fechas de fechaDesde y fechaHasta no son correctas, o cuando se coloca sólo una de las dos.
    '''
    def listar(self, periodo=None, fechaDesde=None, fechaHasta=None, receptorCodigo=None):
        url = '/bhe/boletas'
        rut = getenv('BHEXPRESS_EMISOR_RUT')
        # url_dict = {}

        if periodo is not None:
            url += f'?periodo={periodo}'
        elif fechaDesde is not None and fechaHasta is not None:
            url += f'?fechaDesde={fechaDesde}&fechaHasta={fechaHasta}'
        if receptorCodigo is not None:
            url += '?' if url.endswith('boletas') else '&'
            url += f'receptorCodigo={receptorCodigo}'
        
        header = {
            'X-Bhexpress-Emisor': rut
        }
        r = self.client.get(url, header)
        
        return r.json()
    
    '''
    Emite una nueva Boleta de Honorarios Electrónica.

    :param dict boleta: Información detallada de la boleta a emitir.
    :return: Respuesta JSON con el encabezado y detalle de la boleta emitida.
    :rtype: dict
    '''
    def emitir(self, boleta):
        url = '/bhe/emitir'
        rut = getenv('BHEXPRESS_EMISOR_RUT')
        header = {
            'X-Bhexpress-Emisor': rut
        }
        r = self.client.post(url, boleta, header)

        return r.json()
    
    '''
    Obtiene el PDF de una BHE emitida.

    :param str numeroBhe: Número de la BHE registrada en BHExpress.
    :return: Contenido del PDF de la BHE.
    :rtype: bytes
    '''
    def pdf(self, numeroBhe):
        url = f'/bhe/pdf/{numeroBhe}'
        rut = getenv('BHEXPRESS_EMISOR_RUT')
        header = {
            'X-Bhexpress-Emisor': rut
        }
        r = self.client.get(url, header)

        return r.content
    
    '''
    Envía por correo electrónico una BHE.

    :param str numeroBhe: Número de la BHE registrada en BHExpress.
    :param str email: Correo del destinatario.
    :return: Respuesta JSON con la confirmación del envío del email.
    :rtype: dict
    '''
    def email(self, numeroBhe, email):
        url = f'/bhe/email/{numeroBhe}'
        rut = getenv('BHEXPRESS_EMISOR_RUT')
        body = {
            'destinatario': {
                'email': email
            }
        }
        header = {
            'X-Bhexpress-Emisor': rut
        }
        r = self.client.post(url, body, header)

        return r.json()
    
    '''
    Anula una BHE específica.

    :param str numeroBhe: Número de la BHE registrada en BHExpress.
    :param int causa: Causa de la anulación de la BHE.
    :return: Respuesta JSON con el encabezado de la boleta anulada.
    :rtype: dict
    '''
    def anular(self, numeroBhe, causa):
        url = f'/bhe/anular/{numeroBhe}'
        rut = getenv('BHEXPRESS_EMISOR_RUT')
        body = {
            'causa': causa
        }
        header = {
            'X-Bhexpress-Emisor': rut
        }
        r = self.client.post(url, body, header)

        return r.json()