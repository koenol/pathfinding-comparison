"""Simple 2D map generator"""

import pygame
from map_generator import MapGenerator

def main():
	pygame.init()
	screen = pygame.display.set_mode((1024, 768))
	pygame.display.set_caption("Pathfinding Algorithm Comparison")
	map_generator = MapGenerator()
	grid = map_generator.load_first_map()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill((26, 29, 35))
		map_generator.generate_map(screen, grid)
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
