import numpy as np
def isPrime(number):
    """
    The function takes an integer as input,
    and outputs either itself or zero, depending on whether
    it is a prime.
    """
    a = int(np.sqrt(number)) + 1
    isprime = True
    for i in range(2,a):
        if number % i == 0:
            isprime = False
            break
    return number * isprime
if __name__ == "__main__" :
    primes = [isPrime(x) for x in range(2,2000000)]
    print(sum(primes))
