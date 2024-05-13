import pygame
from src.config import VIRTUAL_WIDTH, VIRTUAL_HEIGHT

class Character:
    def __init__(self):
        self.image, self.rect = self.load_character_image()
        self.speed = 3
        self.jump_speed = 0
        self.max_jump_height = 400
        self.gravity = 1
        self.left = False
        self.right = False
        self.score = 0

    def load_character_image(self):
        # load the character image and resize it
        scale_factor = 0.1

        original_character_image = pygame.image.load('assets/images/character.png').convert_alpha()
        original_character_rect = original_character_image.get_rect()

        new_width = int(original_character_rect.width * scale_factor)
        new_height = int(original_character_rect.height * scale_factor)
        character_image = pygame.transform.scale(original_character_image, (new_width, new_height))

        # init character at middle
        character_rect = character_image.get_rect(midbottom=(VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT - 50))

        return character_image, character_rect

    def jump(self):
        self.jump_speed = -15

        # play jump sound effect
        jump_sound = pygame.mixer.Sound('assets/sounds/mario-jump-sound-effect.mp3')
        jump_sound.play()

    def move_screen_up(self, platforms, character_rect, distance):
        # move all platforms upward to emulate screen going up
        for platform in platforms:
            platform.y += distance

        character_rect.y -= distance

    def update(self, platforms):
        # check collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform) and self.jump_speed >= 0:
                self.jump()
                self.move_screen_up(platforms, self.rect, -self.jump_speed)
                self.score += 1

        # apply gravity
        self.jump_speed += self.gravity
        self.rect.y += self.jump_speed

        # cap maximum jump height
        if self.rect.bottom <= VIRTUAL_HEIGHT - self.max_jump_height:
            self.jump_speed = 0

        return self.score

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def render(self, virtual_screen):
        virtual_screen.blit(self.image, self.rect)
