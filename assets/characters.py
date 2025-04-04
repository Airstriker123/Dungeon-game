import pygame
import os
import random
import time


class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 defence: int,
                 speed: int,
                 strength: int,
                 attack: int,
                 mana: int

                 ):
        self.name = name
        self.health = health
        self.defence = defence
        self.speed = speed
        self.strength = strength
        self.attack = attack
        self.mana = mana

        character_image = pygame.image.load(os.path.join("assets", "images", "main_character.png"))

        self.image = pygame.transform.scale(character_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.direction = "right"

    def draw(self,
             surface
             ):
        surface.blit(self.image, self.rect)

    def move(self,
             keys
             ):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed





