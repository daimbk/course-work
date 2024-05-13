
'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
from .State import State
from lib.utils import draw_text
from lib.score_utils import *
from agents.Character import Character
from agents.Platform import Platform
from src.config import *


class StartState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.gameStarted = False
        self.score = 0
        self.high_score = load_high_score()
        self.character = Character()
        self.platform = Platform()

    def load(self):
        # initialize our nice-looking retro text fonts having various sizes
        self.small_font = pygame.font.Font('assets/fonts/font.ttf', 14)
        self.largeFont = pygame.font.Font('assets/fonts/font.ttf', 32)

        # platform init
        self.platforms = []
        self.last_platform_y = VIRTUAL_HEIGHT - 100

        # spawn initial platform below character
        initial_platform = pygame.Rect(self.character.rect.x - self.platform.width // 2, self.character.rect.bottom, self.platform.width, self.platform.height)
        self.platforms.append(initial_platform)

# --------------------------------------------------------------------------------------------------

    def unload(self):
        pass

# --------------------------------------------------------------------------------------------------

    def init(self):
        # initialize the highlighted menu item
        self.highlighted = 1


# --------------------------------------------------------------------------------------------------


    def free(self):
        pass

# --------------------------------------------------------------------------------------------------

    def pause(self):
        pass

# --------------------------------------------------------------------------------------------------

    def resume(self):
        pass

# --------------------------------------------------------------------------------------------------

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.character.left = True
            elif event.key == pygame.K_RIGHT:
                self.character.right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.character.left = False
            elif event.key == pygame.K_RIGHT:
                self.character.right = False

# --------------------------------------------------------------------------------------------------

    def update(self, dt):
        if self.score > self.high_score:
            # update the high score if new record
            self.high_score = self.score
            # save to file
            save_high_score(self.high_score)

        # check continuous key presses for moving left and right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.move_left()
        if keys[pygame.K_RIGHT]:
            self.character.move_right()

        # character jump movement, each jump on platform returns +1 score
        self.score = self.character.update(self.platforms)

        # check if game over
        if self.gameStarted:
            if self.character.rect.top > VIRTUAL_HEIGHT:
                # play death sound effect
                death_sound = pygame.mixer.Sound('assets/sounds/death-sound.mp3')
                death_sound.play()

                from src.states.GameOverState import GameOverState
                self.stateManager.changeState(GameOverState(self.stateManager))

        # spawn platforms
        if len(self.platforms) < 8:
            new_platform, self.last_platform_y = self.platform.spawn(self.last_platform_y)
            self.platforms.append(new_platform)

        # destroy platforms below the visible screen
        self.platforms = self.platform.destroy_platforms(self.platforms)

        self.gameStarted = True

# --------------------------------------------------------------------------------------------------

    def render(self, virtual_screen, dt=0.0):
        # load background image
        background_image = pygame.image.load('assets/images/background.png').convert()
        background_image = pygame.transform.scale(background_image, (VIRTUAL_WIDTH, VIRTUAL_HEIGHT)) # scale to screen size
        virtual_screen.blit(background_image, (0, 0))

        # display score and high score
        draw_text(f"Score: {self.score}", self.small_font, VIRTUAL_WIDTH - 40, 20, (0, 0, 0), virtual_screen)
        draw_text(f"High Score: {self.high_score}", self.small_font, VIRTUAL_WIDTH - 60, 40, (0, 0, 0), virtual_screen)

        # draw character
        self.character.render(virtual_screen)

        # draw platforms
        for platform in self.platforms:
            self.platform.render(virtual_screen, platform)

# --------------------------------------------------------------------------------------------------
