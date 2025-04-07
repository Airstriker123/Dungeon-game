import pygame
import os
import sys

class Level:
    def __init__(self
                 ):
        #get display surface
        self.display_surfaces = pygame.display.get_surface()
        #sprite setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    def run(self
            ):
        #update and draw game
        pass
