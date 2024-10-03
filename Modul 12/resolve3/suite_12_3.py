# Домашнее задание по теме "Систематизация и пропуск тестов".

import resolve1, resolve2
import unittest

# Часть 1. TestSuit.

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(resolve1.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(resolve2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# Часть 2. Пропуск тестов.
#
# В resolve1, resolve2 прописано использование декораторов для пропуска:
# @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')