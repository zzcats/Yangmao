import unittest
from BuyService.CosmosDB.database_dao import DatabaseDAO
from BuyService.CosmosDB import test_items
from BuyService.CosmosDB.image_tool import image_decoder, store_single_disk

endpoint = ""
key = ''
database_name = 'yangmao'
container_name = "product"
instance=DatabaseDAO(endpoint,key,database_name,container_name);

class MyTestCase(unittest.TestCase):
    def test_add(self):
        item= test_items.get_item_1()
        instance.add_item(item)
        self.assertEqual(True, True)

    def test_read(self):
        item = instance.read_item('1_052dacef-933a-4eae-ab75-7a0203a371d2');
        store_single_disk(image_decoder(item['picture']), 'D:\\Capture3.PNG')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()