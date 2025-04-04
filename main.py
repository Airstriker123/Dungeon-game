from assets.characters import Character

import pygame
import sys
import os
import random

# Day 1 :0 21
#completed character!
class Game:
    def __init__(self
                 ):
        pygame.init()  # Start pygame
        self.screen = pygame.display.set_mode((800, 600),pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_caption("Dungeon Game")  # game name
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "images", "icon.png")))

        # Create your character once
        self.main_character = Character("Hero", 100, 10, 10, 8, 12, 50)

    def run(self)\
            :
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                # Get key presses and move the character
                keys = pygame.key.get_pressed()
                self.main_character.move(keys)

                # Update animation
                self.main_character.update_animation()

                # bg color
                self.screen.fill((10, 255, 130))

                # Draw character
                self.main_character.draw(self.screen)

                # Update display
                pygame.display.flip()
                self.clock.tick(60)  # Max FPS




# run game
game = Game(

)
game.run(

)

