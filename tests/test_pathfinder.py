"""Tests for Pathfinder base class"""
import math
import unittest

from src.pathfinder import Pathfinder


class TestPathfinder(unittest.TestCase):
	"""Tests for Pathfinder"""
	def setUp(self):
		self.pathfinder = Pathfinder()
		self.grid = [
			[".", "S", "@"],
			["W", "T", "O"],
		]

	def test_octile_distance(self):
		"""Octile distance calc"""
		self.assertAlmostEqual(self.pathfinder.h((0, 0), (0, 0)), 0.0)
		self.assertAlmostEqual(self.pathfinder.h((0, 0), (1, 1)), math.sqrt(2))
		correct_value = (3 + 4) + (math.sqrt(2) - 2) * 3
		self.assertAlmostEqual(self.pathfinder.h((0, 0), (3, 4)), correct_value)

	def test_is_in_bounds(self):
		"""Bounds check"""
		self.assertTrue(self.pathfinder.is_in_bounds(self.grid, (0, 0)))
		self.assertTrue(self.pathfinder.is_in_bounds(self.grid, (2, 1)))
		self.assertFalse(self.pathfinder.is_in_bounds(self.grid, (-1, 0)))
		self.assertFalse(self.pathfinder.is_in_bounds(self.grid, (0, -1)))
		self.assertFalse(self.pathfinder.is_in_bounds(self.grid, (3, 0)))
		self.assertFalse(self.pathfinder.is_in_bounds(self.grid, (0, 2)))

	def test_is_passable(self):
		"""Check whether all tiles is return correct passable value"""
		self.assertTrue(self.pathfinder.is_passable(self.grid, (0, 0)))
		self.assertTrue(self.pathfinder.is_passable(self.grid, (1, 0)))
		self.assertFalse(self.pathfinder.is_passable(self.grid, (2, 0)))
		self.assertFalse(self.pathfinder.is_passable(self.grid, (2, 1)))
		self.assertFalse(self.pathfinder.is_passable(self.grid, (1, 1)))
		self.assertFalse(self.pathfinder.is_passable(self.grid, (0, 1)))

if __name__ == "__main__":
	unittest.main()
