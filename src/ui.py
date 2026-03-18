"""UI"""

import pygame

class UI:
	def __init__(self, map_names):
		self.map_names = map_names
		self.selected_map = map_names[0]
		self.dropdown_open = False
		self.dropdown_rect = pygame.Rect(10, 10, 250, 30)
		self.height = 26
		self.text_color = (240, 240, 240)
		self.font = pygame.font.Font(None, 24)
		self.max_visible_options = 10
		self.scroll_offset = 0

	def draw_selector(self, screen: pygame.Surface):
		"""Draw the map selector"""
		self.dropdown_rect.x = screen.get_width() - self.dropdown_rect.width - 10
		text = self.font.render(f"Map: {self.selected_map}", True, self.text_color)
		screen.blit(text, (self.dropdown_rect.x + 10, self.dropdown_rect.y + 5))

		arrow = "v" if not self.dropdown_open else "^"
		arrow_surface = self.font.render(arrow, True, self.text_color)
		screen.blit(
			arrow_surface,
			(self.dropdown_rect.right - 20, self.dropdown_rect.y + 5)
		)

	def draw_dropdown_list(self, screen: pygame.Surface):
		"""Draw the dropdown list"""
		if not self.dropdown_open:
			return

		offset_start_idx = self.scroll_offset
		end_idx = min(len(self.map_names), offset_start_idx + self.max_visible_options)
		visible_maps = self.map_names[offset_start_idx:end_idx]

		for visible_idx, map_name in enumerate(visible_maps):
			option_rect = pygame.Rect(
				self.dropdown_rect.x,
				self.dropdown_rect.bottom + visible_idx * self.height,
				self.dropdown_rect.width,
				self.height,
			)

			option_text = self.font.render(map_name, True, self.text_color)
			screen.blit(option_text, (option_rect.x + 8, option_rect.y + 4))

	def max_offset(self):
		"""Return max offset for dropdown menu"""
		return max(0, len(self.map_names) - self.max_visible_options)

	def get_visible_list(self):
		"""Return current visible dropdown list"""
		visible_count = min(len(self.map_names), self.max_visible_options)
		return pygame.Rect(
			self.dropdown_rect.x,
			self.dropdown_rect.bottom,
			self.dropdown_rect.width,
			visible_count * self.height,
		)

	def handle_event(self, event: pygame.event.Event):
		"""Handle mouse tracking for dropdown menu"""
		if event.type == pygame.MOUSEWHEEL:
			mouse_pos = pygame.mouse.get_pos()
			if self.dropdown_rect.collidepoint(mouse_pos):
				self.scroll(-event.y)
			return None

		if event.type != pygame.MOUSEBUTTONDOWN:
			return None

        # 4 scroll up, 5 scroll down
		if event.button in (4, 5):
			if self.dropdown_rect.collidepoint(event.pos) or self.get_visible_list().collidepoint(event.pos):
				# 4 scroll up
				direction = -1 if event.button == 4 else 1
				self.scroll(direction)
			return None

		if self.dropdown_rect.collidepoint(event.pos):
			self.dropdown_open = not self.dropdown_open
			return None

		start_idx = self.scroll_offset
		end_idx = min(len(self.map_names), start_idx + self.max_visible_options)
		for visible_idx, map_name in enumerate(self.map_names[start_idx:end_idx]):
			option_rect = pygame.Rect(
				self.dropdown_rect.x,
				self.dropdown_rect.bottom + visible_idx * self.height,
				self.dropdown_rect.width,
				self.height,
			)
			if option_rect.collidepoint(event.pos):
				self.selected_map = map_name
				self.dropdown_open = False
				return map_name
		self.dropdown_open = False
		return None
	
	def scroll(self, dir: int):
		"""List scroll"""
		self.scroll_offset = max(0, min(self.max_offset(), self.scroll_offset + dir))