"""Map generation and rendering utilities."""

import os
import pygame

class MapGenerator:
	"""Create a MapGenerator Object"""
	def __init__(self):
		self.cell_size = 1
		self.terrain_colors = {
			# PASSABLE TERRAIN. NO FUNC DIFFERENCE BETWEEN . AND G.
			".": (220, 220, 220),
			"G": (200, 210, 180),
			# OUT OF BOUNDS
			"@": (20, 20, 20),
			"O": (35, 35, 35),
			# PASSABLE IN SOME CASES, EFFECTS MAY VARY. T = TREES, S = SWAMP, W = WATER.
			# POSSIBLE PASSABLE CONDITION CHECKS: LAND UNIT, AIR UNIT, WATER UNIT.
			# POSSIBLE EFFECTS: SLOWED (INCREASED TILE COST), UNPASSABLE (CERTAIN UNITS ARE NOT ALLOWED TO TRAVEL BY LAND OR SEA)
			# UNDECIDED WHETHER DIFFENT TYPES OF UNITS ARE TESTED, BY DEF. ONLY LAND UNITS ARE TESTED WHICH ARE NOT SLOWED BY SWAMP AND CANNOT PASS TREE/WATER TILES.
			"T": (30, 100, 30),
			"S": (140, 120, 70),
			"W": (45, 100, 180),
		}
		self.maps = self.load_all_maps()

	def generate_map(
		self,
		screen: pygame.Surface,
		grid: list[list[int | str]],
		offset_x: int = 10,
		offset_y: int = 50,
	):
		"""Draw the map to the screen."""
		for y, row in enumerate(grid):
			for x, tile in enumerate(row):
				color = self.terrain_colors.get(tile)
				rect = pygame.Rect(
					offset_x + x * self.cell_size,
					offset_y + y * self.cell_size,
					self.cell_size,
					self.cell_size,
				)
				pygame.draw.rect(screen, color, rect)

	def get_maps_dir(self):
		"""Return map dir"""
		return os.path.join(os.path.dirname(__file__), "..", "maps")

	def load_map(self, file_path):
		"""Generate ASCII map"""
		with open(file_path, "r", encoding="utf-8") as file:
			lines = [line.rstrip("\n") for line in file]

		height = int(lines[1].split()[1])
		width = int(lines[2].split()[1])
		map_lines = lines[4:4 + height]

		grid = []
		for line in map_lines:
			grid.append(list(line[:width]))
		return grid

	def load_first_map(self):
		"""Load the initial map"""
		if not self.maps:
			return []
		first_map_name = next(iter(self.maps))
		return self.load_map_by_name(first_map_name)

	def load_map_files(self):
		"""Load map files"""
		maps_dir = self.get_maps_dir()
		map_files = []
		for name in os.listdir(maps_dir):
			if name.lower().endswith(".map"):
				map_files.append(name)
		return map_files

	def load_all_maps(self):
		"""Load all maps"""
		loaded_maps = {}
		for map_name in self.load_map_files():
			path = os.path.join(self.get_maps_dir(), map_name)
			loaded_maps[map_name] = self.load_map(path)
		return loaded_maps
		
	def list_maps(self):
		"""Return map files"""
		return list(self.maps.keys())

	def load_map_by_name(self, map_name):
		"""Return map by a keyword"""
		return self.maps[map_name]