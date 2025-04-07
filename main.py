from assets.characters import Character
from assets.level import Level

import pygame
import sys
import os
import random

# Day 3
#completed character!
class Game:
    def __init__(self):
        pygame.init()  # Start pygame
        self.screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level()

        pygame.display.set_caption("Dungeon Game")  # game name
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "images", "icon.png"
                                                               )
                                                  )
                                )

        # Create your character once
        self.main_character = Character("Hero", 100, 10, 10, 8, 12, 50)
    #game animations
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Get key presses and move the character
            keys = pygame.key.get_pressed()
            self.main_character.move(keys)
            self.main_character.update_animation()

            # Fill screen
            self.screen.fill((100, 100, 100))
            self.level.run()

            # Draw character
            self.main_character.draw(self.screen)

            # Update display
            pygame.display.flip()
            self.clock.tick(60)  # Max FPS
            # main game loop



        (pygame

        .quit(

        )

    )

(
       Game(

)
     .run(

    )
)
