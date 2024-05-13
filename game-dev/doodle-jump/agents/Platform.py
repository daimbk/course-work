import pygame
import random
from src.config import VIRTUAL_WIDTH, VIRTUAL_HEIGHT

class Platform:
    def __init__(self):
        self.width = 50
        self.height = 8
        self.image = self.load_platform_image()

    def load_platform_image(self):
        # load platform image
        original_platform_image = pygame.image.load('assets/images/platform.png').convert_alpha()
        original_platform_rect = original_platform_image.get_rect()

        # resize platform
        scale_factor = 0.5
        new_width = int(original_platform_rect.width * scale_factor)
        new_height = int(original_platform_rect.height * scale_factor)

        return pygame.transform.scale(original_platform_image, (new_width, new_height))

    def spawn(self, last_platform_y):
        new_platform_y = last_platform_y - 50 # vertical position of the new platform
        new_platform_x = random.randint(0, VIRTUAL_WIDTH - self.width) # random x position for the new platform
        new_platform_rect = pygame.Rect(new_platform_x, new_platform_y, self.width, self.height)

        return new_platform_rect, new_platform_y

    def render(self, virtual_screen, platform_rect):
        virtual_screen.blit(self.image, platform_rect)

    def destroy_platforms(self, platforms):
        # destroy platforms that reach bottom of the screen
        platforms = [
            platform for platform in platforms if platform.top <= VIRTUAL_HEIGHT]
        return platforms
