from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        self.tesObj = Item.objects.create(
            name = "Arabica",
            price = 50000,
            amount = 100,
            description = "Kopi Arabica: Rasakan Keajaiban Rasa dalam Setiap Titis."
        )
    
    def test_model_method(self):
        obj = Item.objects.get(id=self.tesObj.id)
        self.assertEqual(obj.name, "Arabica")
        self.assertEqual(obj.price, 50000)
        self.assertEqual(obj.amount, 100)
        self.assertEqual(obj.description, "Kopi Arabica: Rasakan Keajaiban Rasa dalam Setiap Titis."
        )