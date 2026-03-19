"""Tests for map generation"""

import unittest
from src.map_generator import MapGenerator

class TestMapGenerator(unittest.TestCase):
	"""Tests fcor MapGenerator class"""
	def setUp(self):
		self.map_generator = MapGenerator()

	def test_cell_size(self):
		"""Assert cell size is equal to 1"""
		self.assertEqual(self.map_generator.cell_size, 1)

	def test_all_maps_loaded(self):
		"""Assert all maps are loaded"""
		self.assertEqual(len(self.map_generator.maps), 36)

if __name__ == "__main__":
	unittest.main()
