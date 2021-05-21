from django.test import TestCase
from django.test import Client
from cliente.forms import *
from cliente.models import Cuenta,Region


class TestForm(TestCase):

    def setUp(self):
        Region.objects.create(
            reg_id='MT',
            reg_nombre='Metropolitana'
        )

    def test_formValid(self):
        mt = Region.objects.get(reg_id='MT')
        form = ClienteCreateForm(data={
            'cuent_rut' : '194326926',
            'cuent_pass' : 'Nezukochuquita',
            'cuent_nombre' : 'Federico',
            'cuent_ape' : 'lilium',
            'cuent_fecnac' : '1992-02-03',
            'cuent_email' : 'coso@gmail.com',
            'desp_telef' : '12345567',
            'desp_region': mt,
            'com_nombre' : 'Santiago',
            'desp_direccion':'san pablo #310'
        })

        self.assertTrue(form.is_valid())

    def test_formInvalid(self):
        mt = Region.objects.get(reg_id='MT')
        form = ClienteCreateForm(data={
            'cuent_rut' : '19432692-6',
            'cuent_pass' : 'Nezukochuquita',
            'cuent_nombre' : 'Federico',
            'cuent_ape' : 'lilium',
            'cuent_fecnac' : '1992-02-03',
            'cuent_email' : 'coso@gmail.com',
            'desp_telef' : '12345567',
            'desp_region': mt,
            'com_nombre' : 'Santiago',
            'desp_direccion':'san pablo #310'
        })

        self.assertFalse(form.is_valid())