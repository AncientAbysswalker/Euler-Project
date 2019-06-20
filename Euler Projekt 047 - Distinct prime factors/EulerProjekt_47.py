# -*- coding: utf-8 -*-

import unittest
import numpy
import os

def load_primes(root=os.path.dirname(__file__)):
    """Read a compressed binary file of sorted primes into a list"""
    file_path = os.path.join(root, "primes.npy")

    # Try to load and return primes, and throw exceptions if something is amiss
    try:
        return numpy.load(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist, or is not at the indicated location")
    except Exception:
        raise Exception("There was an error reading the file")


def recursive_factorization(n, p, index=0):
    """Generate factors of a number recursively"""

    if n in p:
        return [n]

    quotient, remainder = n // p[index], n % p[index]

    if remainder == 0:
        if quotient == 1:
            return [p[index]]
        else:
            return [p[index]] + recursive_factorization(quotient, p, index)
    else:
        return recursive_factorization(n, p, index + 1)


def recursive_distinct_factors(n, p, index=0, adder=1):
    """Generate factors of a number recursively"""

    # if n in p:
    #     return n != p[index]

    quotient, remainder = n // p[index], n % p[index]

    if remainder == 0:
        if quotient == 1:
            return adder
        else:
            return adder + recursive_distinct_factors(quotient, p, index, 0)
    else:
        return recursive_distinct_factors(n, p, index + 1)


def list_to_quantity_dict(factor_list):
    """Convert a list of numbers to a dictionary with numbers as key and count as value"""
    factor_dict = dict()

    for factor in factor_list:
        factor_dict[factor] = factor_dict.get(factor, 0) + 1

    return factor_dict


def consecutive_distinct_prime_factors(n):
    """Determine the first n consecutive numbers that have n distinct prime factors are"""

    # Load primes and determine smallest number to have n distinct prime factors
    primes = load_primes()
    sequential_count = 0
    current_number = numpy.prod(primes[:n])

    while current_number < primes[-1]:
        _temp = list_to_quantity_dict(recursive_factorization(current_number, primes))
        if len(_temp) == n:
            sequential_count += 1
        else:
            sequential_count = 0

        if sequential_count == n:
            return [current_number - n + i + 1 for i in range(n)]

        current_number += 1


def consecutive_distinct_prime_factors2(n):
    """Determine the first n consecutive numbers that have n distinct prime factors are"""

    # Load primes and determine smallest number to have n distinct prime factors
    primes = load_primes()
    sequential_count = 0
    current_number = numpy.prod(primes[:n])

    while current_number < primes[-1]:
        if recursive_distinct_factors(current_number, primes) == n:
            sequential_count += 1
        else:
            sequential_count = 0

        if sequential_count == n:
            return [current_number - n + i + 1 for i in range(n)]

        current_number += 1


class TestRecursiveFactors(unittest.TestCase):
    """Test behaviour of generating prime factors recursively"""
    primes = load_primes()

    def test_recursive_factors_4(self):
        self.assertEqual(recursive_factorization(4, TestRecursiveFactors.primes), [2, 2])

    def test_recursive_factors_9(self):
        self.assertEqual(recursive_factorization(9, TestRecursiveFactors.primes), [3, 3])

    def test_recursive_factors_55(self):
        self.assertEqual(recursive_factorization(55, TestRecursiveFactors.primes), [5, 11])

    def test_recursive_factors_356(self):
        self.assertEqual(recursive_factorization(356, TestRecursiveFactors.primes), [2, 2, 89])

    def test_recursive_factors_1823(self):
        self.assertEqual(recursive_factorization(1823, TestRecursiveFactors.primes), [1823])

    def test_recursive_factors_4620(self):
        self.assertEqual(recursive_factorization(4620, TestRecursiveFactors.primes), [2, 2, 3, 5, 7, 11])

    def test_recursive_factors_35468(self):
        self.assertEqual(recursive_factorization(35468, TestRecursiveFactors.primes), [2, 2, 8867])


class TestQuantityDict(unittest.TestCase):
    """Test behaviour of converting a list of numbers to a list of numbers with quantities"""

    def test_quantity_dict_4(self):
        self.assertEqual(list_to_quantity_dict([2, 2]), {2: 2})

    def test_quantity_dict_9(self):
        self.assertEqual(list_to_quantity_dict([3, 3]), {3: 2})

    def test_quantity_dict_55(self):
        self.assertEqual(list_to_quantity_dict([5, 11]), {5: 1, 11: 1})

    def test_quantity_dict_356(self):
        self.assertEqual(list_to_quantity_dict([2, 2, 89]), {2: 2, 89: 1})

    def test_quantity_dict_1823(self):
        self.assertEqual(list_to_quantity_dict([1823]), {1823: 1})

    def test_quantity_dict_4620(self):
        self.assertEqual(list_to_quantity_dict([2, 2, 3, 5, 7, 11]), {2: 2, 3: 1, 5: 1, 7: 1, 11: 1})

    def test_quantity_dict_35468(self):
        self.assertEqual(list_to_quantity_dict([2, 2, 8867]), {2: 2, 8867: 1})


class TestConsecutiveDistinct(unittest.TestCase):
    """Test behaviour of converting a list of numbers to a list of numbers with quantities"""

    def test_consecutive_distinct_2(self):
        self.assertEqual(consecutive_distinct_prime_factors(2), [14, 15])

    def test_consecutive_distinct_3(self):
        self.assertEqual(consecutive_distinct_prime_factors(3), [644, 645, 646])


if __name__ == '__main__':
    # unittest.main(exit=False)

    print(consecutive_distinct_prime_factors2(3))


