BHExpress: Cliente de API en Python
=====================================

.. image:: https://badge.fury.io/py/bhexpress.svg
    :target: https://pypi.org/project/bhexpress
.. image:: https://img.shields.io/pypi/status/bhexpress.svg
    :target: https://pypi.org/project/bhexpress
.. image:: https://img.shields.io/pypi/pyversions/bhexpress.svg
    :target: https://pypi.org/project/bhexpress
.. image:: https://img.shields.io/pypi/l/bhexpress.svg
    :target: https://raw.githubusercontent.com/bhexpress/bhexpress-api-client-python/master/COPYING

Cliente para realizar la integración con los servicios web de `BHExpress <https://www.bhexpress.cl>`_ desde Python.

Instalación y actualización
---------------------------

Instalar usando un entorno virtual y PIP con:

.. code:: shell

    python3 -m venv venv
    source venv/bin/activate
    pip install bhexpress

Actualizar usando PIP con:

.. code:: shell

    pip install bhexpress --upgrade

Modo de uso
-----------

Se recomienda ver los ejemplos para más detalles. Lo que se muestra aquí es sólo
una idea, y muy resumida:

Lo más simple, y recomendado, es usar una variable de entorno con el
`token del usuario <https://bhexpress.cl/usuarios/perfil#token>`_,
el cual será reconocida automáticamente por el cliente:

.. code:: python

    from bhexpress.api_client.bhe.boletas import Boleta

    client = Boleta()

    boletas = self.client.listar()
    print(boletas)

Lo que hizo el ejemplo anterior es listar boletas emitidas en un resultado e imprimir dicho resultado en consola.

Ejemplos
--------

Estos ejemplos provienen de la versión PHP. Para crear la versión Python de BHExpress,
se tomó en cuenta dichos ejemplos.
Los ejemplos cubren los siguientes casos:

- `001-boletas_listado.php`: obtener las boletas de un período.
- `002-boleta_emitir.php`: emisitir una BHE.
- `003-boleta_pdf.php`: descargar el PDF de una BHE.
- `004-boleta_email.php`: enviar por email una BHE.
- `005-boleta_anular.php`: anular una BHE.

Los ejemplos, por defecto, hacen uso de variables de entornos, si quieres usar
esto debes tenerlas creadas, por ejemplo, en Windows 10, con:

.. code:: shell
    set BHEXPRESS_API_URL="https://bhexpress.cl"
    set BHEXPRESS_API_TOKEN="" # aquí el token obtenido en https://bhexpress.cl/usuarios/perfil#token
    set BHEXPRESS_EMISOR_RUT="" # aquí el RUT del emisor de las BHE

Ejemplo en la consola de Linux:

.. code:: shell
    export BHEXPRESS_API_URL="https://bhexpress.cl"
    export BHEXPRESS_API_TOKEN="" # aquí el token obtenido en https://bhexpress.cl/usuarios/perfil#token
    export BHEXPRESS_EMISOR_RUT="" # aquí el RUT del emisor de las BHE


Licencia
--------

Este programa es software libre: usted puede redistribuirlo y/o modificarlo
bajo los términos de la GNU Lesser General Public License (LGPL) publicada
por la Fundación para el Software Libre, ya sea la versión 3 de la Licencia,
o (a su elección) cualquier versión posterior de la misma.

Este programa se distribuye con la esperanza de que sea útil, pero SIN
GARANTÍA ALGUNA; ni siquiera la garantía implícita MERCANTIL o de APTITUD
PARA UN PROPÓSITO DETERMINADO. Consulte los detalles de la GNU Lesser General
Public License (LGPL) para obtener una información más detallada.

Debería haber recibido una copia de la GNU Lesser General Public License
(LGPL) junto a este programa. En caso contrario, consulte
`GNU Lesser General Public License <http://www.gnu.org/licenses/lgpl.html>`_.

Enlaces
-------

- `Sitio web API Gateway <https://www.bhexpress.cl>`_.
- `Código fuente en GitHub <https://github.com/bhexpress/bhexpress-api-client-python>`_.
- `Paquete en PyPI <https://pypi.org/project/bhexpress>`_.
- `Documentación en Read the Docs <https://bhexpress.readthedocs.io/es/latest>`_.
