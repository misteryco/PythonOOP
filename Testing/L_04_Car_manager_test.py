from PythonOOP.Testing.L_04_Car_manager import Car
import unittest


class TestCarManager(unittest.TestCase):
    def setUp(self):
        self.car_test = Car(make="Make", model="Model", fuel_capacity=10, fuel_consumption=2.5)

    def test_init(self):
        self.assertEqual(self.car_test.make, "Make")
        self.assertEqual(self.car_test.model, "Model")
        self.assertEqual(self.car_test.fuel_consumption, 2.5)
        self.assertEqual(self.car_test.fuel_capacity, 10)
        self.assertEqual(self.car_test.fuel_amount, 0)

    def test_make(self):
        self.assertEqual(self.car_test.make, "Make")

    def test_make_setter(self):
        # Act
        self.car_test.make = "N_Make"
        self.assertEqual(self.car_test.make, "N_Make")
        with self.assertRaises(Exception) as ex:
            self.car_test.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter(self):
        # Act
        self.car_test.model = "N_Model"
        self.assertEqual(self.car_test.model, "N_Model")
        with self.assertRaises(Exception) as ex:
            self.car_test.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter(self):
        # Act
        self.car_test.fuel_consumption = 1
        self.assertEqual(self.car_test.fuel_consumption, 1)
        with self.assertRaises(Exception) as ex:
            self.car_test.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter(self):
        # Act
        self.car_test.fuel_capacity = 1
        self.assertEqual(self.car_test.fuel_capacity, 1)
        with self.assertRaises(Exception) as ex:
            self.car_test.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter(self):
        # Act
        self.car_test.fuel_amount = 1
        self.assertEqual(self.car_test.fuel_amount, 1)
        with self.assertRaises(Exception) as ex:
            self.car_test.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel(self):
        self.car_test.refuel(1)
        self.assertEqual(self.car_test.fuel_amount, 1)
        self.car_test.refuel(20)
        self.assertEqual(self.car_test.fuel_amount, 10)
        with self.assertRaises(Exception) as ex:
            self.car_test.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive(self):
        self.car_test.refuel(10)
        self.car_test.drive(300)
        self.assertEqual(self.car_test.fuel_amount, 2.5)
        with self.assertRaises(Exception) as ex:
            self.car_test.drive(500)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
