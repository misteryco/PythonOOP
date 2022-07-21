from PythonOOP.Testing.L_03_List import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.int_list = IntegerList(5, 6, 7)

    def test_constructor(self):
        self.assertEqual(self.int_list._IntegerList__data, [5, 6, 7])

    def test_constructor_with_not_int(self):
        a_int_list = IntegerList(5.2, "6", 7)
        self.assertEqual(a_int_list._IntegerList__data, [7])

    def test_get_data_method(self):
        self.assertEqual(self.int_list.get_data(), [5, 6, 7])

    def test_add_operation(self):
        self.int_list.add(8)
        self.assertEqual(self.int_list.get_data(), [5, 6, 7, 8])

    def test_add_operation_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.add(8.8)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(20)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        self.int_list.remove_index(0)
        self.assertEqual(self.int_list.get_data(), [6, 7])

    def test_get_index(self):
        self.assertEqual(self.int_list.get(0), 5)

    def test_get_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert(self):
        self.int_list.insert(0, 1000)
        self.assertEqual(self.int_list.get_data(), [1000, 5, 6, 7])

        with self.assertRaises(IndexError) as ir:
            self.int_list.insert(100, 1000)
        self.assertEqual("Index is out of range", str(ir.exception))

        with self.assertRaises(ValueError) as vr:
            self.int_list.insert(0, "5")
        self.assertEqual("Element is not Integer", str(vr.exception))

    def test_get_biggest(self):
        self.assertEqual(self.int_list.get_biggest(), 7)

    def test_index(self):
        self.assertEqual(self.int_list.get_index(5), 0)

    def test_index_raises(self):
        with self.assertRaises(ValueError) as vr:
            self.int_list.get_index(100)
        self.assertEqual("100 is not in list", str(vr.exception))


if __name__ == "__main__":
    unittest.main()
