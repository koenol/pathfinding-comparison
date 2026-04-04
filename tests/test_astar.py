"""Tests for A* pathfinder"""
import unittest
from src.astar import Astar

class TestAstar(unittest.TestCase):
	"""Tests for Astar class"""
	def setUp(self):
		self.astar = Astar()
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
		self.astar.find_path(grid, start, goal)

	def test_diagonal_movement_3x3_map(self):
		"""A* should find the goal when only diagonal path is available"""
		grid = [
			[".", "@", "@"],
			["@", ".", "@"],
			["@", "@", "."],
		]
		path = self.astar.find_path(grid, (0, 0), (2, 2))
		self.assertEqual(path, [(0, 0), (1, 1), (2, 2)])
		self.assertEqual(len(path), 3)

	def test_expanded_nodes_open_map(self):
		"""A* should expand only 3 nodes on open 3x3 map from (0,0) to (2,2)"""
		grid = [
			[".", ".", "."],
			[".", ".", "."],
			[".", ".", "."],
		]
		self.astar.find_path(grid, (0, 0), (2, 2))
		self.assertEqual(self.astar.stats["expanded_nodes"], 3)

	def test_blocked_path(self):
		"""A* should return empty path and 3 expanded nodes when goal is blocked"""
		grid = [
			[".", "@", "."],
			[".", "@", "."],
			[".", "@", "."],
		]
		path = self.astar.find_path(grid, (0, 0), (2, 2))
		self.assertEqual(path, [])
		self.assertEqual(self.astar.stats["expanded_nodes"], 3)

	def test_verify_path_is_same(self):
		"""If start and goal are the same the returned path should be equal to x,y coordinates"""
		path = self.astar.find_path(self.open_grid, (1, 1), (1, 1))
		self.assertEqual(path, [(1, 1)])

	def test_pathfinder_prioritize_diagonal_movement(self):
		"""A* should prioritize diagonal movement"""
		path = self.astar.find_path(self.open_grid, (0, 0), (2, 2))
		self.assertEqual(path, [(0, 0), (1, 1), (2, 2)])

if __name__ == "__main__":
	unittest.main()
