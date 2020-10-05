#!/usr/bin/env python


import unittest
from validation import validate_user

class TestValidationUser(unittest.TestCase):
	def test_valid(self):
		self.assertEqual(validate_user('validation', 3), True)

	def test_too_short(self):
		self.assertEqual(validate_user('inv', 5), False)

	def test_invalid_characters(self):
		self.assertEqual(validate_user('invalid user', 1), False)

	def test_invalid_minlen(self):
		self.assertRaises(ValueError, validate_user, 'username', -1)
unittest.main()
