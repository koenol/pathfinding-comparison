"""Simple 2D map generator"""

import pygame
from map_generator import MapGenerator
from ui import UI

def main():
	pygame.init()
	screen = pygame.display.set_mode((1024, 768))
	pygame.display.set_caption("Pathfinding Algorithm Comparison")
	map_generator = MapGenerator()
	map_names = map_generator.list_maps()
	ui = UI(map_names)
	grid = map_generator.load_first_map()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			selected_map = ui.handle_event(event)
			if selected_map:
				grid = map_generator.load_map_by_name(selected_map)

		screen.fill((25, 25, 30))
		ui.draw_selector(screen)
		map_generator.generate_map(screen, grid)
		ui.draw_dropdown_list(screen)
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
