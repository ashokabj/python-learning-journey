# Prime Number Finder using List Comprehension

limit = int(input("Find prime numbers up to: "))

primes = [
    num
    for num in range(2, limit + 1)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
]

print("\nPrime Numbers:")
print(primes)