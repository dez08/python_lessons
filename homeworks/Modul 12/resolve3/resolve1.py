# Домашнее задание по теме "Простые Юнит-Тесты"

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_1 = Runner('Vlad')
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_2 = Runner('Ivan')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = Runner('Vlad')
        run_2 = Runner('Ivan')
        for _ in range(10):
            run_1.walk()
            run_2.run()
        self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == '__main__':
    unittest.main()