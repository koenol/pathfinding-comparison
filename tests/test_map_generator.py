"""Tests for map generation"""

import unittest
from src.map_generator import MapGenerator

class TestMapGenerator(unittest.TestCase):
	def setUp(self):
		self.map_generator = MapGenerator()

	def test_cell_size(self):
		self.assertEqual(self.map_generator.cell_size, 1)

if __name__ == "__main__":
	unittest.main()
