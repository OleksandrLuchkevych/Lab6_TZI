import random
import sympy
import time

def generate_large_prime(n_bits, t):
    start_time = time.time()
    iterations = 0
    while True:
        candidate = random.getrandbits(n_bits) | (1 << (n_bits - 1)) | 1
        iterations += 1
        
        if sympy.isprime(candidate):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Просте число: {candidate}")
            print(f"Кількість ітерацій для генерації: {iterations}")
            print(f"Час, витрачений на генерацію: {elapsed_time:.4f} секунд")
            return candidate, iterations, elapsed_time

def primes_in_range(start, end):
    start_time = time.time()
    primes = list(sympy.primerange(start, end + 1))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Прості числа в діапазоні [{start}, {end}]: {primes}")
    print(f"Час, витрачений на пошук простих чисел: {elapsed_time:.4f} секунд")
    return primes, elapsed_time

def find_primitive_roots(prime):
    start_time = time.time()
    roots = []
    count = 0
    for root in range(2, prime):
        if sympy.is_primitive_root(root, prime):
            roots.append(root)
            count += 1
            if count == 100:
                break
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Перші 100 початкових коренів для числа {prime}: {roots}")
    print(f"Час, витрачений на пошук коренів: {elapsed_time:.4f} секунд")
    return roots, elapsed_time

# Приклад використання програми
n_bits = 65  # Кількість біт (повинно бути більше 64)
t = 10  # Кількість перевірок за тестом Рабіна-Міллера
start_range = 100
end_range = 1000
prime = 101

# A) Генерація великого простого числа
print("Генерація великого простого числа:")
generate_large_prime(n_bits, t)

# B) Виведення всіх простих чисел у заданому діапазоні
print("\nПрості числа в заданому діапазоні:")
primes_in_range(start_range, end_range)

# C) Знаходження перших 100 початкових коренів
print("\nПошук перших 100 початкових коренів:")
find_primitive_roots(prime)
