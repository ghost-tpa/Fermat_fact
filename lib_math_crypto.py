from math import sqrt, floor, isqrt, ceil
from random import randrange

"""
Module này dùng để sinh số nguyên tố ngẫu nhiên phục vụ cho mã hóa với khóa công khai
"""

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def isPrimeTrialDiv(num):
    """
    Hàm này kiểm tra số có phải là số nguyên tố hay không
    Nếu số num chia hết cho sqrt(num) thì không phải là số nguyên tố và ngược lại
    :param num: số int
    :return: bool - True nếu là số nguyên tố, False nếu ngược lại
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):  # +1 vì for chạy tới num-1
        if num % i == 0:
            return False
    return True


def primeSieve(sieveSize):
    """
    Sàng Eratosthenes
    :param sieveSize: int
    :return: list các số nguyên tố
    """
    sieve = [True] * sieveSize
    sieve[0] = False  # 0 và 1 không phải là số nguyên tố
    sieve[1] = False

    # thuật toán sàng
    for i in range(2, int(sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    primes = []
    # lấy các số nguyên tố còn lại trong sàng
    for i in range(sieveSize):
        if sieve[i]:
            primes.append(i)

    return primes


def rabinMiller(num):
    """
    Hàm kiểm tra rabin- miller, dựa trên nguyên lý xác xuất và các kiến thức về số học
    để kiểm tra xác xuất số num có phải là số nguyên tố hay không, sai số rất lớn nếu
    test ít lần. O(log(n))
    :param num: int - số cần kiểm tra
    :return: boolvar - True nếu là số nguyên tố và ngược lại
    """
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num - 1  # nếu num là số ngto thì num - 1 là số chẵn được viết dưới dạng 2^t * x
    t = 0
    while s % 2 == 0:
        # giải thuật chia tới khi nào tìm thấy số lẻ thì thôi
        s //= 2  # phép chia nguyên
        t += 1
    for trials in range(15):  # thực hiện test 5 lần -> 15
        a = randrange(2, num - 1)
        v = pow(a, s, num)  # a^s mod (num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


"""
    Thông thường chúng ta có thể xác định được những số không phải là nguyên tố bằng bằng
cách xác định được nó có chia hết cho vài số từ 1-10. Cách này nhanh hơn phép kiểm tra 
Miller-Rabin nhưng nó không phải luôn luôn đúng.
"""
LOW_PRIMES = primeSieve(100)  # các số nguyên tố nhỏ hơn 100

def isPrime(num):
    """
    Chúng ta kiểm tra nhanh trước khi dùng kiểm tra Rabin-Miller, [sẽ tính xác xuất sai
    số nếu rảnh]
    :param num: int - số cần kiểm tra có phải là số nguyên tố hay không.
    :return: boolvar - True nếu là số nguyên tố và ngược lại
    """
    if num < 2:
        return False
    for prime in LOW_PRIMES:
        if num == prime:
            return True
        if num % prime == 0:
            return False
    return rabinMiller(num)

def generateLargePrime(keysize=1024):
    """
    Hàm trả về số nguyên tố cực lớn
    :param keysize: size = 2^ keysize
    :return: int - prime number
    """
    while True:
        num = randrange(2 ** (keysize-1), 2**keysize)  # 2^ 1023 -> 2^ 1024
        if isPrime(num):
            return num


def find_gcd(a: int, b: int) -> int:
    """
    Tim ucln (gcd) của 2 số a, b sử dụng giải thuật Euclid
    """
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

def find_lcm(a: int, b: int) -> int:
    return a // (find_gcd(a, b) * b)

def extended_euclid(a: int, b: int) -> tuple:
    """
        Theo bổ đề Bezout ta có, nếu d = (a,b) [a, b - cho trước] => Tồn tại u, v nguyên sao cho: a*u + b*v = d
    thuật toán này để tìm u, v thỏa mãn điều kiện trên.
    :return:
    """
    u1, u2, u3 = 1, 0, a  # init
    v1, v2, v3 = 0, 1, b  # init
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = u1 - (v1 * q), u2 - (v2 * q), u3 - (v3 * q), v1, v2, v3
    return u1, u2

def find_inv_euclid(a: int, m: int) -> int:
    """
        Sử dụng thuật toán mở rộng Euclid để tìm phần tử nghịch đảo của 1 a theo module m
    Cơ sở lý thuyết: theo bổ đề Bezout ta có, khi d = 1 = (a, b) => tồn tại u, v nguyên sao cho au + bv = 1
    a, u, b, v trong Zm, thay b =m ta có: au + mv = 1, từ đây suy ra, u = a^-1 (nghịch đảo của a trong Zm)
    :return:
    """
    if find_gcd(a, m) != 1:
        exit("gcd(%s, %s) != 1, Exit !!!" % (a, m))
    u1, u2, u3 = 1, 0, a  # init
    v1, v2, v3 = 0, 1, m  # init
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = u1 - (v1 * q), u2 - (v2 * q), u3 - (v3 * q), v1, v2, v3
    return u1 % m

def find_inv_fermat(a: int, m: int) -> int:
    """
        Tìm nghịch đảo của a theo module m dựa trên định lý nhỏ Fermat:
    Cơ sở lý thuyết: p - số  nguyên tố, a - số nguyên, (a, p) = 1 => a ^ (p-1) = 1 (mod p)
    a * a ^ (p - 2) = a * a ^ (- 1) mod p  [vì (a, p) = 1] => a ^ -1 = a ^ (p -2) mod p
    """
    if find_gcd(a, m) != 1:
        exit("gcd(%s, %s) != 1, Exit !!!" % (a, m))
    return pow(a, m-2, m)

def count_div(number):  # ham dem so uoc cua 1 so number
    result = 0
    for index in range(1, floor(sqrt(number)) + 1):
        if number % index == 0:
            result += 1
            j = number // index
            if index != j:  # truong hop number - so chinh phuong (square number)
                result += 1
    return result

def Solve_quadratic_equation(a: int, b: int, c: int):
    """
    aX^2 + bx + c
    """
    assert a != 0, "a must be != 0"
    delta = (b * b) - (4 * (a * c))
    if delta < 0:
        print("This equation dont have solution, return 0, 0")
        return 0, 0
    else:
        return (-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a)

def is_perfect_square(n: int) -> int:
    """
    If n is a perfect square it returns sqrt(n), otherwise returns -1
    """
    h = n & 0xF  # last hexadecimal "digit"

    if h > 9:
        return -1  # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8:
        # take square root if you must
        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1

    return -1

def check_smooth_number(n: int, p: int) -> bool or list:
    """
    check number n is p-smooth or not, n must be > 0, if n is p-smooth number
    return list of all values are divided by n, otherwise return False
    """
    assert n > 0, "n must be greater then 0"
    list_res = []
    max_val = -1  # init
    # when n divided by 2, we solve it separately, so we
    # don't need check this values 4, 6, ...
    while not (n % 2):
        n //= 2
        max_val = 2
        list_res.append(2)
    max_loop = ceil(sqrt(n))
    for index in range(3, max_loop, 2):
        while not (n % index):
            n //= index
            max_val = index
            list_res.append(index)
    # if n is prime number, then it a divisor it self
    if n > 2:
        max_val = max(max_val, n)

    if max_val > p or max_val < 2:
        return False
    else:
        return list_res

def gen_prime_range(start, stop):
    """
    Generates a prime within the given range using the miller_rabin_test
    :return:
    """
    """
        # save variant for generating prime number in range
        p = 0
        flag = True
        while flag:
            p = randrange(start, stop-1, 2)  # step 2 because prime is not even
            if isPrime(p):
                flag = False
        return p
    """
    while True:
        p = randrange(start, stop-1, 2)  # step 2 because prime is not even
        if isPrime(p):
            return p