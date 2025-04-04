import pygame
import sys
import os
import random


class Game:
    def __init__(self

                 ):
        pygame.init()  # start pygame
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption("Dungeon Game")  # Name title
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "images", "icon.png")))

    def run(self
            ):
        while self.running:
            for event in pygame.event.get( ):
                if event.type == pygame.QUIT:
                    self.running = False

            # Game logic goes here (e.g., update positions, check collisions)
            #funcs ---
            # Fill the screen with a color (for example, black)
            self.screen.fill((0, 0, 0))

            pygame.display.flip()  # Update the display
            self.clock.tick(60)  #max fps = 60

        pygame.quit()  # Quit pygame properly when the loop ends


# Start the game
game = Game(

)
game.run(

)
