"""Tests for Jump Point Search (JPS) pathfinder"""
import unittest
from src.jps import Jps

class TestJps(unittest.TestCase):
	"""Tests for Jps class"""
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
		self.assertEqual(len(path), 3)

	def test_diagonal_movement_3x3_map(self):
		"""JPS should find the goal when only diagonal path is available"""
		grid = [
			[".", "@", "@"],
			["@", ".", "@"],
			["@", "@", "."],
		]
		path = self.jps.find_path(grid, (0, 0), (2, 2))
		self.assertEqual(path, [(0, 0), (1, 1), (2, 2)])
		self.assertEqual(len(path), 3)

	def test_expanded_nodes_open_map(self):
		"""JPS should expand only 2 nodes on open 3x3 map from (0,0) to (2,2)"""
		grid = [
			[".", ".", "."],
			[".", ".", "."],
			[".", ".", "."],
		]
		self.jps.find_path(grid, (0, 0), (2, 2))
		self.assertEqual(len(self.jps.expanded_nodes), 2)

	def test_blocked_path(self):
		"""JPS should return empty path and 1 expanded nodes when goal is blocked"""
		grid = [
			[".", "@", "."],
			[".", "@", "."],
			[".", "@", "."],
		]
		path = self.jps.find_path(grid, (0, 0), (2, 2))
		self.assertEqual(path, [])
		self.assertEqual(len(self.jps.expanded_nodes), 1)

	def test_verify_path_is_same(self):
		"""If start and goal are the same the returned path should be equal to x,y coordinates"""
		path = self.jps.find_path(self.open_grid, (1, 1), (1, 1))
		self.assertEqual(path, [(1, 1)])

	def test_pathfinder_prioritize_diagonal_movement(self):
		"""JPS should prioritize diagonal movement"""
		path = self.jps.find_path(self.open_grid, (0, 0), (2, 2))
		self.assertEqual(path, [(0, 0), (1, 1), (2, 2)])

if __name__ == "__main__":
	unittest.main()
