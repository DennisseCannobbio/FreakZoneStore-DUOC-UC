from django.test import TestCase
from .models import Conn, CS, CSInstance, Plat

# Create your tests here.
class ConsoleTest(TestCase):
    def create_plat(self, plat_nom="TestStaytion Switch"):
        return Plat.objects.create(plat_nom)

    def test_plat_creation(self):
        p = self.create_plat()
        self.assertTrue(isinstance(p, Plat))
        self.assertEqual(p.__str__(), p.plat_nom)