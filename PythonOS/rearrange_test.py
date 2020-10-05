#!/usr/bin/env python


from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):

	def test_basic(self):
		testcase = 'lovelace, Ada'
		expected = 'Ada lovelace'
		self.assertEqual(rearrange_name(testcase), expected)


	def test_empty(self):
		testcase = ''
		expected = ''
		self.assertEqual(rearrange_name(testcase), expected)

	def double_name(self):
		testcase = 'Hridoy, Rakib H.'
		expected = 'Rakib H. Hridoy'
		self.assertEqual(rearrange_name(testcase), expected)

	def test_one_name(self):

		testcase = 'Volitoire'
		expected = 'Volitoire'
		self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
