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

from unittest import TestCase
from os import getenv, remove as file_remove
from datetime import datetime
from bhexpress.api_client import ApiException
from bhexpress.api_client.bhe.boletas import Boleta

class TestBheBoletas(TestCase):

    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Boleta()
        # Variables CASO 1
        cls.lis_anio = getenv('TEST_LISTAR_ANIO', datetime.now().strftime('%Y')).strip()
        cls.lis_periodo = getenv('TEST_LISTAR_PERIODO', datetime.now().strftime('%Y%m')).strip()
        cls.lis_fecha_desde = getenv('TEST_LISTAR_FECHADESDE', datetime.now().strftime('%Y-%m-%d')).strip()
        cls.lis_fecha_hasta = getenv('TEST_LISTAR_FECHAHASTA', datetime.now().strftime('%Y-%m-%d')).strip()
        cls.lis_codigo_receptor = getenv('TEST_LISTAR_CODIGORECEPTOR', '').strip()
        # Variables CASO 2
        cls.emit_fecha_emision = getenv('TEST_EMITIR_FECHA_EMIS', datetime.now().strftime('%Y-%m-%d')).strip()
        cls.emit_rut_emisor = getenv('TEST_EMITIR_EMISOR', '').strip()
        cls.emit_rut_receptor = getenv('TEST_EMITIR_RECEPTOR', '').strip()
        cls.emit_razon_social = getenv('TEST_EMITIR_RZNSOC_REC', '').strip()
        cls.emit_direccion_receptor = getenv('TEST_EMITIR_DIR_REC', '').strip()
        cls.emit_comuna_receptor = getenv('TEST_EMITIR_COM_REC', '').strip()
        # Variables CASO 3
        cls.pdf_probar = getenv('TEST_PDF_PROBAR', '0').strip()
        # Variables CASO 4
        cls.email_num_bhe = getenv('TEST_EMAIL_NUMEROBHE', '').strip()
        cls.email_destinatario = getenv('TEST_EMAIL_CORREO', '').strip()
        # Variables CASO 5
        cls.anul_probar = getenv('TEST_ANULAR_PROBAR', '0').strip()
    
    # CASO 1: Listado de boletas
    def test1_listar(self):
        print('')
        print('test1_listar():')
        print('')
        try:
            boletas = self.client.listar(periodo = self.lis_periodo, receptor_codigo = self.lis_codigo_receptor)
            if len(boletas['results']) == 0:
                print('La lista de BHEs en BHExpress está vacía.')
            if self.verbose:
                print('test1_listar(): boletas', boletas)
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
    
    # CASO 2: Emitir una boleta
    def test2_emitir(self):
        print('')
        print('test2_emitir():')
        print('')
        if self.emit_rut_receptor == '':
            print('test2_emitir(): no probó funcionalidad')
            return
        datos = {
            'Encabezado': {
                'IdDoc': {
                    'FchEmis': self.emit_fecha_emision,
                    'TipoRetencion': 2
                },
                'Emisor': {
                    'RUTEmisor': self.emit_rut_emisor
                },
                'Receptor': {
                    'RUTRecep': self.emit_rut_receptor,
                    'RznSocRecep': self.emit_razon_social,
                    'DirRecep': self.emit_direccion_receptor,
                    'CmnaRecep': self.emit_comuna_receptor
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
        try:
            emitir = self.client.emitir(datos)
            if self.verbose:
                print('test2_emitir(): emitir', emitir)
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
    
    # CASO 3: bajar pdf de una boleta
    def test3_pdf(self):
        print('')
        print('test3_pdf():')
        print('')
        try:
            if self.pdf_probar == '0':
                print('test3_pdf(): no probó funcionalidad.')
                return
            lista_bhe = self.client.listar()
            boleta_numero = lista_bhe['results'][0]['numero']
            html = self.client.pdf(boleta_numero)
            filename = 'bhe_emitidas_test_pdf_%(boleta_numero)s.pdf' % {'boleta_numero': boleta_numero}
            with open(filename, 'wb') as f:
                f.write(html)
            file_remove(filename)
            if self.verbose:
                print('test3_pdf(): filename', filename)
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
    
    # CASO 4: enviar por email
    def test4_email(self):
        print('')
        print('test4_email():')
        print('')
        if self.email_num_bhe == '' or self.email_destinatario == '':
            print('test4_email(): no probó funcionalidad.')
            return
        try:
            email = self.client.email(self.email_num_bhe, self.email_destinatario)
            if self.verbose:
                print('test4_email(): email', email)
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
    
    # CASO 5: anular
    def test5_anular(self):
        print('')
        print('test5_anular():')
        print('')
        try:
            if self.anul_probar == '0':
                print('test5_anular(): no probó funcionalidad.')
                return
            lista_bhe = self.client.listar()
            if len(lista_bhe['results']) == 0:
                print('test5_anular(): no hay boleta para anular.')
            else:
                boleta_numero = lista_bhe['results'][0]['numero']
                anular = self.client.anular(boleta_numero, 3)
                if self.verbose:
                    print('test5_anular(): anular', anular)
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
