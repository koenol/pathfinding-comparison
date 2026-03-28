"""Tests for map handler class"""
import unittest
from src.map_handler import MapHandler

class TestMapHandler(unittest.TestCase):
	"""Tests for MapHandler"""
	def setUp(self):
		self.map_handler = MapHandler()

	def test_positions_are_stored_correctly(self):
		"""Set start and goal then compare that the positions are stored correctly"""
		self.map_handler.update_selected_position(1, 1)
		self.map_handler.update_selected_position(1, 2)
		self.assertEqual(self.map_handler.get_start_position(), (1, 1))
		self.assertEqual(self.map_handler.get_goal_position(), (1, 2))

	def test_positions_are_not_overwritten(self):
		"""Test positions are not overwritten"""
		self.map_handler.update_selected_position(1, 1)
		self.map_handler.update_selected_position(1, 2)
		self.map_handler.update_selected_position(1, 3)
		self.assertEqual(self.map_handler.get_start_position(), (1, 1))
		self.assertEqual(self.map_handler.get_goal_position(), (1, 2))
		
	def test_initial_positions(self):
		"""Start and Goal should be set to None at the start"""
		self.assertIsNone(self.map_handler.get_start_position())
		self.assertIsNone(self.map_handler.get_goal_position())

	def test_set_path_stores_path(self):
		"""Test path is stored"""
		path = [(0, 0), (1, 0), (2, 0)]
		self.map_handler.set_path(path)
		self.assertEqual(self.map_handler.path, path)

	def test_reset_all(self):
		"""Reset should clear all the information"""
		self.map_handler.update_selected_position(1, 2)
		self.map_handler.update_selected_position(3, 4)
		self.map_handler.set_path([(1, 2), (2, 2), (3, 4)])
		self.map_handler.reset_positions()
		self.assertIsNone(self.map_handler.get_start_position())
		self.assertIsNone(self.map_handler.get_goal_position())
		self.assertEqual(self.map_handler.path, [])

if __name__ == "__main__":
	unittest.main()
