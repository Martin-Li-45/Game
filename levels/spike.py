import pygame
import utils


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = utils.SPIKE_IMAGE
        
        self.rect = self.image.get_rect(topleft=(x, y))