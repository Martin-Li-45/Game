import pygame
import utils

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(utils.IRON_GREY)

        self.rect = self.image.get_rect(topleft=(x, y))