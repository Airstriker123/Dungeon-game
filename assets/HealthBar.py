import pygame
from .characters import Character

class HealthBar:
    def __init__(self, character: Character):
        self.character = character
        self.width = 100
        self.height = 15
        self.offset = 10  # space above the character

    def draw(self, surface):
        max_health = self.character.health  # Assuming full health at start
        current_health = self.character.health

        # Position the health bar above the character
        x = self.character.rect.centerx - self.width // 2
        y = self.character.rect.top - self.offset - self.height

        # Background (red)
        pygame.draw.rect(surface, (255, 0, 0), (x, y, self.width, self.height))

        # Foreground (green)
        health_ratio = current_health / max_health
        pygame.draw.rect(surface, (0, 255, 0), (x, y, self.width * health_ratio, self.height))
