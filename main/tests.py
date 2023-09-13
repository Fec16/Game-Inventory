from django.test import TestCase
from .models import Item

class ItemTestCase(TestCase):
    
    def setUp(self):
        self.item = Item.objects.create(
            name = "Mora",
            amount = 1000,
            type = "Common Currencies",
            quality = "3 stars",
            description = "Common currency. The one language everybody speaks.",
        )

    def test_item(self):
        item_from_databases = Item.objects.get(id = self.item.id)

        self.assertEqual(item_from_databases.name, "Mora")
        self.assertEqual(item_from_databases.amount, 1000)
        self.assertEqual(item_from_databases.type, "Common Currencies")
        self.assertEqual(item_from_databases.quality, "3 stars")
        self.assertEqual(item_from_databases.description, "Common currency. The one language everybody speaks.")