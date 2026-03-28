"""Tests for UI class"""
import unittest

import pygame

from src.ui import UI

class TestUI(unittest.TestCase):
	"""Test UI"""
	@classmethod
	def setUpClass(cls):
		pygame.init()

	@classmethod
	def tearDownClass(cls):
		pygame.quit()

	def setUp(self):
		self.map_names = [f"map_{i}.map" for i in range(15)]
		self.ui = UI(self.map_names)

	def test_first_map_is_loaded(self):
		"""First map name should match first map"""
		self.assertEqual(self.ui.selected_map, self.map_names[0])

if __name__ == "__main__":
	unittest.main()
