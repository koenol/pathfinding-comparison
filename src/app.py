"""Simple 2D map generator"""

import pygame
from map_generator import MapGenerator

def main():
	pygame.init()
	screen = pygame.display.set_mode((1920, 1080))
	pygame.display.set_caption("Pathfinding Algorithm Comparison")
	map_generator = MapGenerator()
	grid = map_generator.generate_map()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		map_generator.draw_map(screen, grid)
		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()
