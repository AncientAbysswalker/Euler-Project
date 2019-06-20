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


def count_distinct_factors(n, p):
    """Count distinct factors of a number iteratively"""

    factor_count = 0

    for i in range(len(p)):
        if p[i] ** 2 > n:
            return factor_count + 1

        is_factor = False
        while n % p[i] == 0:
            is_factor = True
            n /= p[i]

        if is_factor:
            factor_count += 1

        if n == 1:
            return factor_count


def consecutive_distinct_prime_factors(n):
    """Determine the first n consecutive numbers that have n distinct prime factors"""

    # Load primes and set starting value
    primes = load_primes()
    sequential_count = 0
    current_number = numpy.prod(primes[:n])

    # iterate through natural numbers until we meet our condition and return a list of sequentials
    while current_number < primes[-1]:
        if count_distinct_factors(current_number, primes) == n:
            sequential_count += 1
        else:
            sequential_count = 0

        if sequential_count == n:
            return [current_number - n + i + 1 for i in range(n)]

        current_number += 1


class TestCountDistinctFactors(unittest.TestCase):
    """Test behaviour of counting distinct factors"""
    primes = load_primes()

    def test_count_factors_4(self):
        self.assertEqual(count_distinct_factors(4, TestCountDistinctFactors.primes), 1)

    def test_count_factors_9(self):
        self.assertEqual(count_distinct_factors(9, TestCountDistinctFactors.primes), 1)

    def test_count_factors_55(self):
        self.assertEqual(count_distinct_factors(55, TestCountDistinctFactors.primes), 2)

    def test_count_factors_356(self):
        self.assertEqual(count_distinct_factors(356, TestCountDistinctFactors.primes), 2)

    def test_count_factors_1823(self):
        self.assertEqual(count_distinct_factors(1823, TestCountDistinctFactors.primes), 1)

    def test_count_factors_4620(self):
        self.assertEqual(count_distinct_factors(4620, TestCountDistinctFactors.primes), 5)

    def test_count_factors_35468(self):
        self.assertEqual(count_distinct_factors(35468, TestCountDistinctFactors.primes), 2)


class TestConsecutiveDistinct(unittest.TestCase):
    """Test behaviour of determining n consecutive numbers with n distinct prime factors"""

    def test_consecutive_distinct_2(self):
        self.assertEqual(consecutive_distinct_prime_factors(2), [14, 15])

    def test_consecutive_distinct_3(self):
        self.assertEqual(consecutive_distinct_prime_factors(3), [644, 645, 646])


if __name__ == '__main__':
    """Determine the first 4 consecutive numbers that have 4 distinct prime factors. Includes unit tests"""
    unittest.main(exit=False)
    print(consecutive_distinct_prime_factors(3))


