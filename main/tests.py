from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/whatthesigmaa/')
        self.assertEqual(response.status_code, 404)

    def test_level_category(self):
        pack = Product.objects.create(
            name='Memancing Pack 001',
            price = 20000000,
            pack_category = 'Mancing',
            level_category = 'Pro',
            description = 'Memancing Pack 001 berisi tools dan bahan untuk memancing (advance)'
        )
        self.assertTrue(pack.is_pro_category)