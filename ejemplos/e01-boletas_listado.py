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

fecha_desde = None
fecha_hasta = None
receptor_codigo = None

# crear cliente
Boletas = Boleta(token, url)

# obtener boletas
try:
    boletas = Boletas.listar(periodo = '202104', fecha_desde = fecha_desde, fecha_hasta = fecha_hasta, receptor_codigo = receptor_codigo)
except Exception as e:
    raise ApiException('Error: %(e)s' % {'e': e})

# mostrar boletas
print(boletas)
