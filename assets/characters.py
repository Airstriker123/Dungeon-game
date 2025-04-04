import pygame
import os

class Character:
    def __init__(self,
                 name,
                 health,
                 defence,
                 speed,
                 strength,
                 attack,
                 mana
                 )-> None:
        self.name = name
        self.health = health
        self.defence = defence
        self.speed = speed
        self.strength = strength
        self.attack = attack
        self.mana = mana
        sprite_sheet = pygame.image.load(os.path.join("assets", "images", "main_character.png")).convert_alpha()
        self.frame_width = sprite_sheet.get_width() // 3
        self.frame_height = sprite_sheet.get_height() // 3
        self.frames = []

        for row in range(3):
            for col in range(3):
                frame = sprite_sheet.subsurface(pygame.Rect(
                    col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height
                ))
                scaled_frame = pygame.transform.scale(frame, (130, 130))  # character size
                self.frames.append(scaled_frame)

        self.current_frame = 0
        self.frame_counter = 0
        self.animation_speed = 5


        self.rect = self.frames[0].get_rect(center=(400, 300))

    def update_animation(self)-> None:

        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self, surface)-> None:

        surface.blit(self.frames[self.current_frame], self.rect)
    def move(self, keys) -> None: # movement management
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed


