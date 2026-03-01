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

class Boleta(ApiBase):
    '''
    Módulo que permite gestionar BHEs emitidas y calcular montos brutos y líquidos.

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

    def listar(self, filtros = {}):
        '''
        Recurso que permite obtener el listado paginado de boletas de honorarios
        electrónicas emitidas.

        :param dict filtros: Filtros de búsqueda.
        :return: Respuesta JSON con el listado de boletas emitidas.
        :rtype: dict
        :exception ApiException: Arroja un error cuando los filtros son incorrectos,
        o cuando hay error de conexión.
        '''
        url = '/bhe/boletas'
        query = {}

        if len(filtros) > 0:
            query_string = urlencode(query)
            url += '?%(query)s' % {'url': url, 'query': query_string}

        response = self.client.get(url)

        return response.json()

    def detalle(self, numeroBhe):
        '''
        Recurso que permite obtener el detalle de una boleta de honorarios
        electrónica emitida.

        :param int numeroBhe: Número de BHE a consultar.
        :return: Respuesta JSON con el detalle de la boleta emitida.
        :rtype: dict
        '''
        url = '/bhe/boletas/%(numeroBhe)s' % {'numeroBhe': numeroBhe}

        response = self.client.get(url)

        return response.json()

    def emitir(self, boleta):
        '''
        Emite una nueva Boleta de Honorarios Electrónica.

        :param dict boleta: Información detallada de la boleta a emitir.
        :return: Respuesta JSON con el encabezado y detalle de la boleta emitida.
        :rtype: dict
        '''
        response = self.client.post('/bhe/emitir', data = boleta)

        return response.json()

    def pdf(self, numero_bhe):
        '''
        Obtiene el PDF de una BHE emitida.

        :param int numero_bhe: Número de la BHE registrada en BHExpress.
        :return: Contenido del PDF de la BHE.
        :rtype: bytes
        '''
        url = '/bhe/pdf/%(bhe)s' % {'bhe': numero_bhe}

        return self.client.get(url).content

    def email(self, numero_bhe, email):
        '''
        Envía por correo electrónico una BHE.

        :param str numero_bhe: Número de la BHE registrada en BHExpress.
        :param str email: Correo del destinatario.
        :return: Respuesta JSON con la confirmación del envío del email.
        :rtype: dict
        '''
        url = '/bhe/email/%(bhe)s' % {'bhe': numero_bhe}
        body = {
            'destinatario': {
                'email': email
            }
        }

        response = self.client.post(url, data = body)

        return response.json()

    def anular(self, numero_bhe, causa):
        '''
        Anula una BHE específica.

        :param str numero_bhe: Número de la BHE registrada en BHExpress.
        :param int causa: Causa de la anulación de la BHE.
        :return: Respuesta JSON con el encabezado de la boleta anulada.
        :rtype: dict
        '''
        url = '/bhe/anular/%(bhe)s' % {'bhe': numero_bhe}
        body = {
            'causa': causa
        }

        response = self.client.post(url, data = body)

        return response.json()

    def montoLiquido(self, bruto, periodo):
        '''
        Recurso que permite calcular el monto líquido a partir de un monto bruto.

        :param int bruto: Monto bruto a convertir.
        :param str periodo: Periodo donde buscar. Formato "AAAAMM".
        :return: Respuesta JSON con los montos calculados, retenciones, tasas y periodos.
        :rtype: dict
        '''
        url = '/bhe/liquido/%(bruto)s/%(periodo)s' % {
            'bruto': bruto, 'periodo': periodo
        }

        response = self.client.get(url)

        return response.json()

    def montoBruto(self, liquido, periodo):
        '''
        Recurso que permite calcular el monto bruto a partir de un monto líquido.

        :param int liquido: Monto liquido a convertir.
        :param str periodo: Periodo donde buscar. Formato "AAAAMM".
        :return: Respuesta JSON con los montos calculados, retenciones, tasas y periodos.
        :rtype: dict
        '''
        url = '/bhe/bruto/%(liquido)s/%(periodo)s' % {
            'liquido': liquido, 'periodo': periodo
        }

        response = self.client.get(url)

        return response.json()