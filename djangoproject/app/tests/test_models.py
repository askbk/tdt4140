from django.test import TestCase
from app.models import Address

class AddressTest(TestCase):
    def create_address(self):
        return Address.objects.create(postal_code=1111, city="Tulleby", street_address="Tullegate 1", country = "Tulleland")

    def test_address_creation(self):
        w = self.create_address()
        self.assertTrue(isinstance(w, Address))
        self.assertEqual(1111, w.postal_code)
        self.assertEqual("Tulleby", w.city)
        self.assertEqual("Tullegate 1", w.street_address)
        self.assertEqual("Tulleland", w.country)
        self.assertEqual("Tullegate 1 - 1111, Tulleby", w.__str__())
