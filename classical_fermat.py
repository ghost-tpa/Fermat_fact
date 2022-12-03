# python
# Created by Tuan Anh Phan on 28.11.2022
from lib_math_crypto import generateLargePrime as genPrime
from lib_math_crypto import isPrime
from math import isqrt
from fractions import Fraction as Frac
def main():
    p, q = genKey(100)
    N = p * q
    print(p)
    print(q)
    p_get, q_get = factorizeFerma_1(N, 100)
    print(p_get)
    print(q_get)

def factorizeFerma_1(n, m):
    k = Frac(m * m, 8).__ceil__()
    x = isqrt(n) + k
    counter = 0
    t = x + counter
    temp = isqrt((t * t) - n)
    while temp * temp != (t * t) - n:
        counter += 1
        t = x + counter
        temp = isqrt((t * t) - n)
        print("Counter: ", counter)

    return t - temp, t + temp

def genKey(m: int, bit_length=2048):
    assert bit_length % 4 == 0
    p = genPrime(bit_length // 2)
    q = nextPrime(p + m * isqrt(p))
    return p, q

def nextPrime(num: int) -> int:
    if num % 2 == 0:  # prime must be odd
        num += 1
    for i in range(2, pow(2, 1000), 2):
        num += i
        if isPrime(num):
            return num


if __name__ == '__main__':
    main()
