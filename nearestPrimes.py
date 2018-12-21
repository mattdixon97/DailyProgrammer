'''
Find the nearest prime greater than and less than a number

https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/
'''

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int((n**0.5) + 1)):
        if n % i == 0:
            return False
    return True

def nearestPrimes(n):
    i = n - 1
    j = n + 1
    while not isPrime(i):
        i -= 1
    while not isPrime(j):
        j += 1
    print(i, '<', n, '<', j)
