import main
import unittest

def test_condition():
	unittest.TestCase.assertEqual(main.condition("y"), True, "the number of alphabeic characters is wrong")

test_condition()