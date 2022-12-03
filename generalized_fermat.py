# python 3.11
# Created by Tuan Anh Phan on 22.11.2022
# DONE 01.12.2022
from lib_math_crypto import generateLargePrime
from math import isqrt
from fractions import Fraction as Frac
from classical_fermat import factorizeFerma_1, nextPrime

def main():
    alpha = Frac(11, 7)
    beta = 1000
    p, q = gen_weak_primes(alpha, beta)
    print("DONE GENERATION KEYS")
    N = p * q
    if isinstance(alpha, Frac):
        N_temp = N * alpha.numerator * alpha.denominator
        p_get, q_get = float_alpha_fact(N_temp, alpha, beta)
        p_hacked = Frac(q_get, alpha.denominator).__ceil__()
        q_hacked = Frac(p_get, alpha.numerator).__ceil__()
        print(p == p_hacked)
        print(q == q_hacked)
    elif isinstance(alpha, int):
        N_temp = N * alpha
        p_get, q_get = factorizeFerma_1(N_temp, beta)
        p_real = p_get // alpha
        print(p == p_real)

def float_alpha_fact(n, alpha, beta):
    counter = 0
    k = Frac(alpha.denominator * beta * beta, 8).__ceil__()
    x = isqrt(n) + k
    t = x + counter
    temp = isqrt((t * t) - n)
    while temp * temp != (t * t) - n:
        counter += 1
        t = x + counter
        temp = isqrt((t * t) - n)
        print("Counter: ", counter)

    return t - temp, t + temp

def gen_weak_primes(alpha, beta: int, bit_length: int = 2048):
    """
    (p / q) = alpha
    :return:
    """
    assert bit_length % 4 == 0
    if isinstance(alpha, Frac):
        q = generateLargePrime(bit_length // 2)
        p = nextPrime((alpha * q).__floor__() + (beta * isqrt((alpha * q).__ceil__())))
        return p, q

    elif isinstance(alpha, int):
        p = generateLargePrime(bit_length // 2)
        q = nextPrime((alpha * p) + (beta * isqrt(alpha * p)))
        return p, q
    else:
        exit("ERROR alpha")


if __name__ == '__main__':
    main()
