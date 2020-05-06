import unittest
from CosmosDB.database_dao import DatabaseDAO
from CosmosDB import test_items
from CosmosDB.image_tool import image_decoder, store_single_disk
from constants.key_constants import KeyConstants

endpoint = KeyConstants.db_endpoint
key = KeyConstants.db_key
database_name = 'yangmao'
container_name = "product"
instance=DatabaseDAO(endpoint,key,database_name,container_name);


class MyTestCase(unittest.TestCase):
    def test_add(self):
        item= test_items.get_item_1()
        res=instance.add_item(item)
        print(res)
        self.assertEqual(True, True)

    def test_read(self):
        item = instance.read_item('1_052dacef-933a-4eae-ab75-7a0203a371d2');
        store_single_disk(image_decoder(item['picture']), 'D:\\Capture3.PNG')
        self.assertEqual(True, True)

    def test_query(self):
        item = instance.select_by_name('锅');
        self.assertEqual(True, True)

    def test_list(self):
        page_number = 2
        page_count = 2
        item = instance.list_item(page_number,page_count);
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
