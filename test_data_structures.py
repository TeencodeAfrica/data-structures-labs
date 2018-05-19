import unittest
from data_structures import ListExamples


class TestDataStructures(unittest.TestCase):
    """Test list functions"""

    def setUp(self):
        self.lst = ListExamples()

    def test_add_item(self):
        self.assertEqual(len(self.lst.add_item()), 5, msg="List should contain five items")
        self.assertEqual(self.lst.add_item()[-2:], ["Teencode", 2018], msg="List should contain 'Teencode' and '2018'")

    def test_retrieve_list_item(self):
        self.assertEqual(self.lst.retrieve_list_item(), "TIA", msg="Should return 'TIA'")

    def test_change_list_item(self):
        self.assertEqual(self.lst.change_list_item(), "Nigeria", msg="Should return 'Nigeria'")

    def test_remove_list_item(self):
        new_list = self.lst.remove_list_item()
        self.assertEqual(new_list[0], "Kenya")
        self.assertEqual(len(new_list), 2)

    def test_convert_list_to_tuple(self):
        self.assertEqual(type(self.lst.convert_list_to_tuple()), tuple, msg="Result should be a Tuple")


if __name__ == '__main__':
    unittest.main()
