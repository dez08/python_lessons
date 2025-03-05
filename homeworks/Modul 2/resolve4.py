# Задача "Всё не так уж просто"
def ip_simple(n):
    simple = 'Простое'
    for i in range(2, n + 1):
        if n % i == 0 and n != i:
            simple = 'Составное'
            break
    return simple


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    n = i
    if i == 1:
        continue
    else:
        if ip_simple(n) == 'Простое':
            primes.append(n)
        else:
            not_primes.append(n)
print(primes)
print(not_primes)
