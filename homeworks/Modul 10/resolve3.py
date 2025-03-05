# Домашнее задание по теме "Блокировки и обработка ошибок"

from random import randint
import threading, time


class Bank:
    def __init__(self):
        self.balance = int()
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            random_int = randint(50, 500)
            self.balance += random_int
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_int}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            random_int = randint(50, 500)
            print(f'Запрос на {random_int}')
            if random_int <= self.balance:
                self.balance -= random_int
                print(f'Снятие: {random_int}. Баланс: {self.balance}')
            else:
                print('Запрос откланен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')