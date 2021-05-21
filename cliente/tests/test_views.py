from django.test import TestCase, Client
from django.urls import reverse
from cliente.models import Cuenta,Region
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.reg = reverse('cliente:reg')
        Region.objects.create(
            reg_id='MT',
            reg_nombre='Metropolitana'
        )
        mt = Region.objects.get(reg_id='MT')
        Cuenta.objects.create(
            cuent_rut = '19282692-6',
            cuent_email = 'coso@gmail.com',
            cuent_pass = 'Nezukochuquita',
            cuent_nombre = 'Federico',
            cuent_ape = 'lilium',
            cuent_fecnac = '1992-02-03',
            desp_telef = '12345567',
            desp_region= mt,
            com_nombre = 'Santiago',
            desp_direccion="san pablo #310"
        )



    def test_reg_acceso(self):
        response= self.client.get(self.reg)
      
        self.assertEquals(response.status_code, 200)#200 es el codigo http para decir que todo esta bien
        self.assertTemplateUsed(response, 'cliente/cuenta_form.html')



    
    
    

    # def test_reg(self):
    #     response = Client.


    # def test_create_cuenta(self):
    #     responde = Cuenta.objects.create(
    #         cuent_rut = '19282746-6',
    #         cuent_email = 'coso@gmail.com',
    #         cunt_pass = 'Nezukochuquita',
    #         cuent_pass = 'Federico',
    #         cuent_ape = 'lilium',
    #         cuent_fecnac = '23/03/1992',
    #         desp_telef = '12345567',
    #         desp_region='MT',
    #         com_nombre = 'Santiago',
    #         desp_direccion='blablablabla'
    #     )
