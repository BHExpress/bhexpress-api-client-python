Configuración
=============

Se recomienda ver los ejemplos para más detalles. Lo que se muestra aquí es solo
una idea muy resumida:

Lo más simple, y recomendado, es usar una variable de entorno con el
`token del usuario <https://bhexpress.cl/usuarios/perfil#token>`_,
el cual será reconocida automáticamente por el cliente:

.. code:: python

    from bhexpress.api_client.bhe.boletas import Boleta

    client = Boleta()

    boletas = client.listar()
    print(boletas)

Lo que hizo el ejemplo anterior es listar boletas emitidas en un resultado e imprimir dicho resultado en consola.

Variables de entorno
--------------------

La aplicación y las pruebas hacen uso de variables de entornos. Si quieres usar
estos, debes tenerlas creadas. En Windows 10 se hace con:

.. code:: shell

    set BHEXPRESS_API_URL="https://bhexpress.cl"
    set BHEXPRESS_API_TOKEN="" # aquí el token obtenido en https://bhexpress.cl/usuarios/perfil#token
    set BHEXPRESS_EMISOR_RUT="" # aquí el RUT del emisor de las BHE

Ejemplo de definición de variables de entorno en la consola de Linux:

.. code:: shell

    export BHEXPRESS_API_URL="https://bhexpress.cl"
    export BHEXPRESS_API_TOKEN="" # aquí el token obtenido en https://bhexpress.cl/usuarios/perfil#token
    export BHEXPRESS_EMISOR_RUT="" # aquí el RUT del emisor de las BHE
