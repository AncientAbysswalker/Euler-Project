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


def permute_factor_sets(factor_sets):
    """Generate permutations of the progressions of factors"""

    # Handling for nothing passed
    if factor_sets is None:
        return None

    # Handling for only one integer passed
    if type(factor_sets) == int:
        return factor_sets + 1

    # Intended pathway for function to take
    if type(factor_sets) == list:
        if all(isinstance(x, int) for x in factor_sets):
            return increment_factors(factor_sets)
        elif all(isinstance(x, list) for x in factor_sets):
            new_factor_sets = []
            for factors in factor_sets:
                _temp = increment_factors(factors)
                for new_factors in _temp:
                    if new_factors not in new_factor_sets:
                        new_factor_sets.append(new_factors)
                print(new_factor_sets)
            return sorted(new_factor_sets)

    raise TypeError("permute_factors(n) only functions for type(n) as None, int, or list: int")


def increment_factors(factors):
    """Increment factors and remove duplicates"""
    identity_matrix = []
    results = []
    size = len(factors)

    for i in range(size):
        identity_matrix.append([0] * size)
        identity_matrix[i][i] = 1

    for identity_row in identity_matrix:
        _temp = sorted([sum(x) for x in zip(factors, identity_row)])
        if _temp not in results:
            results.append(_temp)

    print(results)

    return sorted(results)


class TestIncrement(unittest.TestCase):
    """Test behaviour of increment_factors()"""

    def test_list(self):
        """Test behaviour if a list of integers is passed"""
        self.assertEqual(increment_factors([0, 0, 0, 0]), [[0, 0, 0, 1]])
        self.assertEqual(increment_factors([0, 1, 1, 1]), [[0, 1, 1, 2], [1, 1, 1, 1]])


class TestPermute(unittest.TestCase):
    """Test behaviour of permute_factor_sets()"""

    def test_none(self):
        """Test behaviour if nothing is passed"""
        self.assertIsNone(permute_factor_sets(None))

    def test_integer(self):
        """Test behaviour if a single integer is passed"""
        self.assertEqual(permute_factor_sets(4), 5)
        self.assertEqual(permute_factor_sets(9), 10)
        self.assertEqual(permute_factor_sets(999), 1000)
        self.assertEqual(permute_factor_sets(658), 659)

    def test_list(self):
        """Test behaviour if a list of integers is passed"""
        self.assertEqual(permute_factor_sets([0, 0]), [[0, 1]])
        self.assertEqual(permute_factor_sets([0, 1]), [[0, 2], [1, 1]])
        self.assertEqual(permute_factor_sets([[0, 1]]), [[0, 2], [1, 1]])
        self.assertEqual(permute_factor_sets([0, 0, 0, 0]), [[0, 0, 0, 1]])
        self.assertEqual(permute_factor_sets([0, 0, 0, 1]), [[0, 0, 0, 2], [0, 0, 1, 1]])
        self.assertEqual(permute_factor_sets([0, 0, 1, 1]), [[0, 0, 1, 2], [0, 1, 1, 1]])
        self.assertEqual(permute_factor_sets([0, 0, 1, 3]), [[0, 0, 1, 4], [0, 0, 2, 3], [0, 1, 1, 3]])
        self.assertEqual(permute_factor_sets([[0, 0, 0, 4], [0, 0, 1, 3], [0, 1, 1, 2], [1, 1, 1, 1]]),
                         [[0, 0, 0, 5], [0, 0, 1, 4], [0, 0, 2, 3], [0, 1, 1, 3], [0, 1, 2, 2], [1, 1, 1, 2]])

    def test_other(self):
        """Test behaviour if an unintended type is passed"""
        self.assertRaises(TypeError, permute_factor_sets, "string")


if __name__ == '__main__':
    unittest.main(exit=False)
    print("IM IN")
    a = load_primes()
    print("IM DONE")