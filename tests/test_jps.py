"""Tests for Jump Point Search (JPS) pathfinder"""
import unittest
from src.jps import Jps

class TestJps(unittest.TestCase):
	"""Tests for Jps class."""
	def setUp(self):
		self.jps = Jps()
		self.open_grid = [
			[".", ".", "."],
			[".", ".", "."],
			[".", ".", "."],
		]

	def test_pathfinder_can_navigate_around_blocking_object(self):
		"""Pathfinder should be able to navigate blocked path"""
		grid = [
			[".", ".", "."],
			[".", "@", "."],
			[".", ".", "."],
		]
		start = (0, 1)
		goal = (2, 1)
		path = self.jps.find_path(grid, start, goal)
		self.assertEqual(path[0], start)
		self.assertEqual(path[-1], goal)
		self.assertEqual(len(path), 5)
		self.assertNotIn((1, 1), path)

	def test_verify_path_is_same(self):
		"""If start and goal are the same the returned path should be equal to x,y coordinates"""
		path = self.jps.find_path(self.open_grid, (1, 1), (1, 1))
		self.assertEqual(path, [(1, 1)])

	def test_max_manhattan_distance_on_512x512_map_jps(self):
		"""Max(Manhattan Distance) should be equal to 1022 on 512x512 map"""
		start = (0, 0)
		goal = (511, 511)
		self.assertEqual(self.jps.h(start, goal), 1022)

if __name__ == "__main__":
	unittest.main()
