Ejemplo
=======

Para utilizar el cliente de API de BHExpress, deberás tener definido el token de API y el RUT del emisor como variables de entorno.

.. seealso::
    Para más información sobre este paso, referirse al la guía en Configuración.

El siguiente es un ejemplo básico de cómo emitir una BHE utilizando el cliente de API.

.. code-block:: python

    # Importaciones del cliente de API de BHExpress
    from datetime import datetime
    from bhexpress.api_client import ApiException
    from bhexpress.api_client.bhe.boletas import Boleta

    # Instancia de cliente.
    cls.client = Boleta()
    # RUT del emisor.
    rutEmisor = "12345678-9"
    # Fecha de emisión de BHE.
    fechaEmis = datetime.now().strftime('%Y-%m-%d')

    # Datos de la boleta a ser emitida.
    datos = {
        'Encabezado': {
            'IdDoc': {
                'FchEmis': fechaEmis,
                'TipoRetencion': 1
            },
            'Emisor': {
                'RUTEmisor': rutEmisor
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
                'CdgItem': 0,
                'NmbItem': 'Se agrega código y cantidad al item (se indica precio unitario)',
                'QtyItem': 1,
                'PrcItem': 1000
            },
            {
                'NmbItem': 'Se agrega cantidad al item (se indica precio unitario)',
                'QtyItem': 2,
                'PrcItem': 2500
            },
            {
                'CdgItem': 2,
                'NmbItem': 'Caso más completo, con código, cantidad, precio y descuento porcentual',
                'QtyItem': 2,
                'PrcItem': 700,
                'DescuentoPct': 10
            },
            {
                'CdgItem': 3,
                'NmbItem': 'Caso más completo, con código, cantidad, precio y descuento fijo',
                'QtyItem': 2,
                'PrcItem': 700,
                'DescuentoMonto': 600
            }
        ]
    }

    # Respuesta de solicitud HTTP (POST) de emisión de boleta.
    response =  client.emitir(datos)

    # Despliegue del resultado.
    print("\nEMISION BOLETA: \n")
    print("\nEmitir BHE ejemplo: ", response, "\n")

.. seealso::
    Para saber más sobre los parámetros posibles y el cómo consumir las API, referirse a la `documentación de BHExpress. <https://developers.bhexpress.cl/>`_
