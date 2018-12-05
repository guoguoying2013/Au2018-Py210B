import random
import time
import math


class Fraction:
    '''
    Simple class to represent fractions to be completed in class.
    Intentionally left as incomplete after class as of 8:30pm, 5/3/18.
    I highly encourage everyone to complete this class to pass all the pytest
    test cases and run the __main__ part of this module correctly.
    '''
    def __init__(self, num, denom):
        if denom == 0:
            raise ZeroDivisionError
        if not isinstance(num, int) or not isinstance(denom, int):
            raise TypeError
        if denom < 0:
            num *= -1
            denom *= -1
        gcd = math.gcd(num, denom)
        self.num = num // gcd
        self.denom = denom // gcd

    @classmethod
    def from_int(cls, num):
        return cls(num, 1)

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __repr__(self):  # LEARN MORE
        return "Fraction({}, {})".format(self.num, self.denom)

    def __eq__(self, other):
        return self.num * other.denom == self.denom * other.num

    def __lt__(self, other):
        return self.num * other.denom < self.denom * other.num

    def __add__(self, other):
        num = self.num * other.denom + self.denom * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)

    # add more method to hel
    def __sub__(self, other):
        num = self.num * other.denom - self.denom * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __mul__(self, other):
        num = self.num * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)


if __name__ == '__main__':
    # f = Fraction(1, 0)  # ZeroDivisionError
    # f = Fraction(1.0, 2)    # TypeError
    f1 = Fraction(1, 2)  # 1/2
    print(f1)
    f2 = Fraction(2, 4)
    print(f1 == f2)     # True
    l = [Fraction(2, 3), Fraction(1, 2), Fraction(0, 1)]
    print(list(str(f) for f in sorted(l)))    # 0/1, 1/2, 2/3

    # sort key timing test
    N = 10000
    a_list = [Fraction(random.randint(0, 10000), random.randint(1, 10000)) for _ in range(N)]
    # print("Before sorting:", a_list)

    print("Timing for {} items".format(N))
    start = time.clock()
    sorted(a_list)
    reg_time = time.clock() - start
    print("regular sort took: {:.4g}s".format(reg_time))

    start = time.clock()
    sorted(a_list, key=Fraction.sort_key)
    key_time = time.clock() - start
    print("key sort took: {:.4g}s".format(key_time))

    print("performance improvement factor: {:.4f}".format((reg_time / key_time)))

    # Add test
    print(Fraction(1, 3) + Fraction(1, 6))
