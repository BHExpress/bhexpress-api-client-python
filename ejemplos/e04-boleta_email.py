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

# importaciones necesarias
from os import getenv
from bhexpress.api_client import ApiException
from bhexpress.api_client.bhe.boletas import Boleta

# datos a utilizar
url = getenv('BHEXPRESS_API_URL', 'https://bhexpress.cl')
token = getenv('BHEXPRESS_API_TOKEN')
rut = getenv('BHEXPRESS_EMISOR_RUT')
numero = 226 # MODIFICAR numero SEGÚN LA BOLETA QUE DESEA ENVIAR AL EMAIL
email = '' # MODIFICAR email SEGÚN EL DESTINATARIO QUE DEBE RECIBIR EL EMAIL

# crear cliente
Boletas = Boleta(token, url)

# enviar boleta por email
try:
    resultado = Boleta.email(numero, email)
except Exception as e:
    raise ApiException('Error: %(e)s' % {'e': e})

# mostrar respuesta
print(resultado)