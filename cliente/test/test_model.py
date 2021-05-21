from django.test import TestCase
from cliente.models import Cuenta,Region


class TestModels(TestCase):
    def setUp(self):

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



    def testCuenta(self):
        usuario_1 =  Cuenta.objects.get(cuent_rut='19282692-6')
        self.assertEquals(usuario_1.cuent_rut, '19282692-6')

    def testRegion(self):
        region_1 =  Region.objects.get(reg_id='MT')
        self.assertEquals(region_1.reg_id, 'MT')