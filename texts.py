import pygame
import utils


class Text:
    def __init__(self):
        self.font = pygame.font.Font(utils.PATH_FONT, utils.SIZE_FONT)

    def get_text(self, screen, text, coordinates_text):
        self.text_surface = self.font.render(text, False, 'Black')
        screen.blit(self.text_surface, coordinates_text)