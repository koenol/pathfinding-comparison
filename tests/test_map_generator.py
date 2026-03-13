"""Tests for map generation"""

import unittest
from src.map_generator import MapGenerator

class TestMapGenerator(unittest.TestCase):
	def test_generate_map_default_size(self):
		"""Test default map generation grid size is 10x10"""
		generator = MapGenerator()
		grid = generator.generate_map()

		self.assertEqual(len(grid), 10)
		for row in grid:
			self.assertEqual(len(row), 10)

	def test_generate_map_size(self):
		"""Test map size generation using input"""
		generator = MapGenerator(grid_size=5)
		grid = generator.generate_map()

		self.assertEqual(len(grid), 5)
		for row in grid:
			self.assertEqual(len(row), 5)

	def test_generate_map_size_zero(self):
		"""Test map size generation when grid size == 0"""
		generator = MapGenerator(grid_size=0)
		grid = generator.generate_map()

		self.assertEqual(len(grid), 0)
		for row in grid:
			self.assertEqual(len(row), 0)


if __name__ == "__main__":
	unittest.main()
