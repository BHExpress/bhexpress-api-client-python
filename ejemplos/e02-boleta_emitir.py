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
# estructura de la boleta
datos = {
    'Encabezado': {
        'IdDoc': {
            'FchEmis': '2024-07-17',
            'TipoRetencion': 2
        },
        'Emisor': {
            'RUTEmisor': rut
        },
        'Receptor': {
            'RUTRecep': '66666666-6',
            'RznSocRecep': 'Receptor generico',
            'DirRecep': 'Santa Cruz',
            'CmnaRecep': 'Santa Cruz'
        }
    },
    'Detalle': [
        {
            'NmbItem': 'Item con monto final solamente (lo básico en SII)',
            'MontoItem': 100
        },
        {
            'CdgItem': 'CASO2',
            'NmbItem': 'Se agrega código al item',
            'MontoItem': 300
        },
        {
            'NmbItem': 'Se agrega cantidad al item (se indica precio unitario)',
            'QtyItem': 1,
            'PrcItem': 120
        },
        {
            'NmbItem': 'Se agrega cantidad al item (se indica precio unitario)',
            'QtyItem': 0.5,
            'PrcItem': 120
        },
        {
            'CdgItem': 'CASO2',
            'NmbItem': 'Se agrega código y cantidad al item (se indica precio unitario)',
            'QtyItem': 2,
            'PrcItem': 250
        },
        {
            'CdgItem': 'COMPLETO',
            'NmbItem': 'Caso más completo, con código, cantidad, precio unitario y descuento en porcentaje',
            'QtyItem': 10,
            'PrcItem': 75,
            'DescuentoPct': 10
        },
        {
            'CdgItem': 'COMPLETO',
            'NmbItem': 'Caso más completo, con codigo, cantidad, precio unitario y descuento en monto fijo',
            'QtyItem': 10,
            'PrcItem': 75,
            'DescuentoMonto': 50
        },
        {
            'NmbItem': 'En este caso el MontoItem es descartado por que va cantidad y precio unitario',
            'QtyItem': 2,
            'PrcItem': 10,
            'MontoItem': 100
        }
    ]
}

# crear cliente
Boletas = Boleta(token, url)

# emitir boleta
try:
    emitir = Boletas.emitir(boleta = datos)
except Exception as e:
    raise ApiException('Error: %(e)s' % {'e': e})

# mostrar boletas
print(emitir)
