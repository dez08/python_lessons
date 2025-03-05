# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.__str__()
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        TournamentTest.all_result = {}

    def setUp(self):
        self.run_1 = Runner('Усейн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament_1(self):
        self.tour_1 = Tournament(90, self.run_1, self.run_3)
        TournamentTest.all_result = self.tour_1.start()
        self.assertTrue(TournamentTest.all_result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament_2(self):
        self.tour_2 = Tournament(90, self.run_2, self.run_3)
        TournamentTest.all_result = self.tour_2.start()
        self.assertTrue(TournamentTest.all_result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament_3(self):
        self.tour_3 = Tournament(90, self.run_1, self.run_2, self.run_3)
        TournamentTest.all_result = self.tour_3.start()
        self.assertTrue(TournamentTest.all_result[3] == 'Ник')

    def tearDown(self):
        print(TournamentTest.all_result)


if __name__ == '__main__':
    unittest.main()
