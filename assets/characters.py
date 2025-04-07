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
                 ):
        self.name = name
        self.health = health
        self.defence = defence
        self.speed = speed
        self.strength = strength
        self.attack = attack
        self.mana = mana

        self.frames_left = []
        self.frames_right = []
        self.frames_idle = []
        self.current_frames = []  # used to switch between left/right
        self.facing_right = False

        # Load sprite sheet (default)
        sprite_sheet = pygame.image.load(os.path.join("assets", "images", "main_character.png")).convert_alpha()
        self.frame_width = sprite_sheet.get_width() // 3
        self.frame_height = sprite_sheet.get_height() // 3

        for row in range(3):
            for col in range(3):
                frame = sprite_sheet.subsurface(pygame.Rect(
                    col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height
                )
                )
                scaled = pygame.transform.scale(frame, (130, 130))
                self.frames_idle.append(scaled)

        # Load right sprite sheet
        sprite_sheet_right = pygame.image.load(os.path.join("assets", "images", "main_character_right.png")).convert_alpha()
        for row in range(3):
            for col in range(3):
                frame = sprite_sheet_right.subsurface(pygame.Rect(
                    col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height
                )
                )
                scaled = pygame.transform.scale(frame, (130, 130))
                self.frames_right.append(scaled)
           #load left sprite
        sprite_sheet_left = pygame.image.load(
        os.path.join("assets", "images", "main_character_left.png")).convert_alpha()
        for row in range(3):
            for col in range(3):
                frame = sprite_sheet_left.subsurface(pygame.Rect(
                    col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height
                )
                )
                scaled = pygame.transform.scale(frame, (130, 130))
                self.frames_left.append(scaled)



        self.current_frames = self.frames_idle

        self.current_frame = 0
        self.frame_counter = 0
        self.animation_speed = 10

        self.rect = self.frames_left[0].get_rect(center=(400, 300))

    def update_animation(self) -> None:
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.current_frames)

    def draw(self, surface) -> None:
        surface.blit(self.current_frames[self.current_frame], self.rect)

    #player controller
    def move(self, keys) -> None:
        moving = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            if self.current_frames != self.frames_left:
                self.current_frames = self.frames_left
                self.current_frame = 0
            moving = True

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            if self.current_frames != self.frames_right:
                self.current_frames = self.frames_right
                self.current_frame = 0
            moving = True

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            moving = True

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            moving = True

        # idle
        if not moving:
            if self.current_frames != self.frames_idle:
                self.current_frames = self.frames_idle
                self.current_frame = 0





