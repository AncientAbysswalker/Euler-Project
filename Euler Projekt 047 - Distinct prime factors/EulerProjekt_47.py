# -*- coding: utf-8 -*-

import yaml
import unittest
import numpy
import os


# def load_primes():
#     """Read a yaml file of primes into an accessible list"""
#     with open('primes.yaml', 'r') as stream:
#         _loaded = yaml.safe_load(stream).tolist()
#
#     return _loaded


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


def recursive_factorization(n, p, last=0):
    """Generate factors of a number recursively"""

    ls = []

    print(n, last)

    if n in p:
        return [n]

    if n % p[last] == 0:
        ls = [p[last]]
        if n / p[last] == 1:
            return ls
        else:
            ls.extend(recursive_factorization(n // p[last], p, last))
            return ls
    else:
        return recursive_factorization(n, p, last + 1)

    #
# def permute_factor_sets(factor_sets):
#     """Generate permutations of the progressions of factors"""
#
#     # Handling for nothing passed
#     if factor_sets is None:
#         return None
#
#     # Handling for only one integer passed
#     if type(factor_sets) == int:
#         return factor_sets + 1
#
#     # Intended pathway for function to take
#     if type(factor_sets) == list:
#         if all(isinstance(x, int) for x in factor_sets):
#             return increment_factors(factor_sets)
#         elif all(isinstance(x, list) for x in factor_sets):
#             new_factor_sets = []
#             for factors in factor_sets:
#                 _temp = increment_factors(factors)
#                 for new_factors in _temp:
#                     if new_factors not in new_factor_sets:
#                         new_factor_sets.append(new_factors)
#                 print(new_factor_sets)
#             return sorted(new_factor_sets)
#
#     raise TypeError("permute_factors(n) only functions for type(n) as None, int, or list: int")
#
#
# def increment_factors(factors):
#     """Increment factors and remove duplicates"""
#     identity_matrix = []
#     results = []
#     size = len(factors)
#
#     for i in range(size):
#         identity_matrix.append([0] * size)
#         identity_matrix[i][i] = 1
#
#     for identity_row in identity_matrix:
#         _temp = sorted([sum(x) for x in zip(factors, identity_row)])
#         if _temp not in results:
#             results.append(_temp)
#
#     print(results)
#
#     return sorted(results)
#
#
# class TestIncrement(unittest.TestCase):
#     """Test behaviour of increment_factors()"""
#
#     def test_list(self):
#         """Test behaviour if a list of integers is passed"""
#         self.assertEqual(increment_factors([0, 0, 0, 0]), [[0, 0, 0, 1]])
#         self.assertEqual(increment_factors([0, 1, 1, 1]), [[0, 1, 1, 2], [1, 1, 1, 1]])
#
#
# class TestPermute(unittest.TestCase):
#     """Test behaviour of permute_factor_sets()"""
#
#     def test_none(self):
#         """Test behaviour if nothing is passed"""
#         self.assertIsNone(permute_factor_sets(None))
#
#     def test_integer(self):
#         """Test behaviour if a single integer is passed"""
#         self.assertEqual(permute_factor_sets(4), 5)
#         self.assertEqual(permute_factor_sets(9), 10)
#         self.assertEqual(permute_factor_sets(999), 1000)
#         self.assertEqual(permute_factor_sets(658), 659)
#
#     def test_list(self):
#         """Test behaviour if a list of integers is passed"""
#         self.assertEqual(permute_factor_sets([0, 0]), [[0, 1]])
#         self.assertEqual(permute_factor_sets([0, 1]), [[0, 2], [1, 1]])
#         self.assertEqual(permute_factor_sets([[0, 1]]), [[0, 2], [1, 1]])
#         self.assertEqual(permute_factor_sets([0, 0, 0, 0]), [[0, 0, 0, 1]])
#         self.assertEqual(permute_factor_sets([0, 0, 0, 1]), [[0, 0, 0, 2], [0, 0, 1, 1]])
#         self.assertEqual(permute_factor_sets([0, 0, 1, 1]), [[0, 0, 1, 2], [0, 1, 1, 1]])
#         self.assertEqual(permute_factor_sets([0, 0, 1, 3]), [[0, 0, 1, 4], [0, 0, 2, 3], [0, 1, 1, 3]])
#         self.assertEqual(permute_factor_sets([[0, 0, 0, 4], [0, 0, 1, 3], [0, 1, 1, 2], [1, 1, 1, 1]]),
#                          [[0, 0, 0, 5], [0, 0, 1, 4], [0, 0, 2, 3], [0, 1, 1, 3], [0, 1, 2, 2], [1, 1, 1, 2]])
#
#     def test_other(self):
#         """Test behaviour if an unintended type is passed"""
#         self.assertRaises(TypeError, permute_factor_sets, "string")


if __name__ == '__main__':
    unittest.main(exit=False)
    primes = load_primes()
    print(recursive_factorization(4, primes))
    print(recursive_factorization(5, primes))
    print(recursive_factorization(6, primes))
    print(recursive_factorization(16, primes))
    print(recursive_factorization(14, primes))
    print(recursive_factorization(55, primes))
    print(recursive_factorization(72, primes))