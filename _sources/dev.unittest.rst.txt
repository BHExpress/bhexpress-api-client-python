Pruebas Unitarias
=================

Las pruebas utilizan un archivo llamado `test.env`, que sirve para definir todas las variables de entorno
necesarias para ejecutar estas pruebas. Las pruebas se crearon para probar los ejemplos vistos previamente
en el capítulo `Ejemplos`.

Estas pruebas utilizan `unittest`, se ejecutan con el archivo `run.py`, y dependiendo de cómo se configure
`test.env`, se pueden omitir ciertas pruebas. Asegúrate de definir `BHEXPRESS_API_URL`, `BHEXPRESS_API_TOKEN`
y `BHEXPRESS_EMISOR_RUT` en `test.env`, o no podrás efectuar las pruebas.

Para ejecutar las pruebas unitarias, debes ejecutar el siguiente código en consola desde la raíz del proyecto:

.. code:: shell

    python3 tests/run.py

Si quieres ejecutar una prueba específica, deberás especificar el nombre y ruta:

.. code:: shell

    python3 tests/run.py bhe.boletas.test_emitir_bhe

Para ejecutar otros ejemplos, debes reemplazar `test_emitir_bhe` por el nombre de alguna de las otras pruebas descritas posteriormente. Además, si quieres ejecutar un test dentro de otra carpeta, como por ejemplo en `servicios`, deberás ejecutar el siguiente comando:

.. code:: shell

    python3 tests/run.py bhe.servicios.test_listar_servicios

A continuación se detallarán instrucciones de cómo probar el cliente de API de Python:

* `testListarBhe()`:
    - Prueba que permite obtener un listado de todas las boletas emitidas a través de BHExpress usando algunos filtros.
    - Variables necesarias: `Ninguna`
    - Ejecución: `python3 tests/run.py bhe.boletas.test_listar_bhe`
* `testEmitirBhe()`:
    - Prueba que permite emitir una BHE a un receptor.
    - Variables necesarias: `BHEXPRESS_EMISOR_RUT`
    - Ejecución: `python3 tests/run.py bhe.boletas.test_listar_bhe`
* `testDescargarPdfBhe()`:
    - Prueba que permite obtener una BHE y convertirla a un PDF.
    - Variables necesarias: `BHEXPRESS_EMISOR_RUT`
    - Ejecución: `python3 tests/run.py bhe.boletas.test_descargar_pdf_bhe`
* `testListarReceptores()`:
    - Prueba que permite obtener un listado de receptores con los que el usuario ya haya interactuado (enviándoles BHEs).
    - Variables necesarias: `Ninguna`
    - Ejecución: `python3 tests/run.py bhe.receptores.test_listar_receptores`
* `testListarServicios()`:
    - Prueba que permite obtener un listado de servicios provistos que el usuario haya registrado en su cuenta BHExpress.
    - Variables necesarias: `Ninguna`
    - Ejecución: `python3 tests/run.py bhe.servicios.test_listar_servicios`

Las `variables necesarias` son aquellas variables que se necesitan para ejecutar las pruebas.
`Ejecución` es el comando que se debe introducir desde la consola para ejecutar el test específico.