from PythonOOP.Testing.L_01_Worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    def test_of_worker_initialization(self):
        # Arrange and act
        worker = Worker("Test", 100, 10)
        # Assert
        self.assertEqual(worker.name, "Test")
        self.assertEqual(worker.salary, 100)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_worker_energy_incremented_after_rest(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        # Act
        worker.rest()
        # Assert
        self.assertEqual(worker.energy, 11)

    def test_worker_works_with_negative_energy_raises(self):
        # Arrange
        worker = Worker("Test", 100, 0)
        # Act
        # Control exception using "with"
        with self.assertRaises(Exception) as ex:
            worker.work()
        # Assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_worker_money_are_increased_after_work_and_energy_decreased(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(worker.money, 100)
        self.assertEqual(worker.energy, 9)

    def test_get_info_returns_proper_string(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(worker.get_info(), "Test has saved 0 money.")

    def test_get_info_returns_proper_string_working(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(worker.get_info(), "Test has saved 100 money.")


if __name__ == "__main__":
    unittest.main()
