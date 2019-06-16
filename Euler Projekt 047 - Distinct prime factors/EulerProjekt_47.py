# -*- coding: utf-8 -*-

import yaml
import unittest
import os


# def load_primes():
#     """Read a yaml file of primes into an accessible list"""
#     with open('primes.yaml', 'r') as stream:
#         _loaded = yaml.safe_load(stream).tolist()
#
#     return _loaded


def load_primes():
    """Read a file of primes into a sorted list"""
    filepath = os.path.join(os.path.dirname(__file__), "primes.txt")
    primes = list()

    print("Checking existance of generated prime file")
    if not os.path.exists(filepath):
        raise ValueError("File does not exist, error...")
    else:
        print("File exists, parsing...")
        f = open(filepath, 'r')
        for num in f.read().split():
            primes.append(int(num))
        print("Parsing complete!")
        primes.sort()
    f.close()

    return primes


def permute_factors(factors):
    """Generate permutations of the progressions of factors"""
    if factors == None:
        return None

    if type(factors) == int:
        return factors + 1

    if type(factors) == list:
        if factors == [0, 0, 0, 0]:
            return [0, 0, 0, 1]

    raise TypeError("permute_factors(n) only functions for type(n) as None, int, or list: int")


class TestPermute(unittest.TestCase):
    def test_none(self):
        """Test behaviour if nothing is passed"""
        self.assertIsNone(permute_factors(None))

    def test_integer(self):
        """Test behaviour if a single integer is passed"""
        self.assertEqual(permute_factors(4), 5)
        self.assertEqual(permute_factors(9), 10)
        self.assertEqual(permute_factors(999), 1000)
        self.assertEqual(permute_factors(658), 659)

    def test_list(self):
        """Test behaviour if a list of integers is passed"""
        self.assertEqual(permute_factors([0, 0, 0, 0]), [0, 0, 0, 1])
        self.assertEqual(permute_factors([0, 0, 0, 1]), [[0, 0, 1, 1], [0, 0, 0, 2]])

    def test_other(self):
        """Test behaviour if an unintended type is passed"""
        self.assertRaises(TypeError, permute_factors, "string")


if __name__ == '__main__':
    unittest.main(exit=False)
    print("IM IN")
    a = load_primes()
    print("IM DONE")