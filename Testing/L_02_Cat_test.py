from PythonOOP.Testing.L_02_Cat import Cat
import unittest


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_check_setup(self):
        self.assertEqual(self.cat.name, "Tom")

    def test_cat_size_increased_and_fed_after_eat(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_After_fed_raises(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_fall_asleep_if_not_fed_raises(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
