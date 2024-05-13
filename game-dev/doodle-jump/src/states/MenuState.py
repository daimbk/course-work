import pygame
from .State import State
from lib.utils import draw_text
from src.config import *


class MenuState(State):
    def __init__(self, stateManager):
        self.options = ['Start', 'Quit']
        self.selected = 0
        self.stateManager = stateManager

    def load(self):
        self.titleFont = pygame.font.Font('assets/fonts/font.ttf', 30)
        self.buttonFont = pygame.font.Font('assets/fonts/font.ttf', 28)
        self.highlighted = 1

    def unload(self):
        pass

    def init(self):
        pass

    def free(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self, dt):
        pass

    def render(self, virtual_screen, dt=0.0):
        virtual_screen.fill((0, 0, 0))
        draw_text('Doodle Jump', self.titleFont, VIRTUAL_WIDTH / 2,
                  VIRTUAL_HEIGHT / 4, (255, 255, 255), virtual_screen)
        draw_text('Play', self.buttonFont, VIRTUAL_WIDTH / 2,
                  VIRTUAL_HEIGHT / 2, (255, 255, 255), virtual_screen)
        draw_text('Quit', self.buttonFont, VIRTUAL_WIDTH / 2,
                  VIRTUAL_HEIGHT / 2 + 50, (255, 255, 255), virtual_screen)
        draw_text('>', self.buttonFont, VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT /
                  2 + (self.highlighted - 1) * 50, (255, 255, 255), virtual_screen)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.highlighted == 1:
                    from src.states.StartState import StartState
                    print("Start Game")
                    self.stateManager.changeState(
                        StartState(self.stateManager))

                elif self.highlighted == 2:
                    print("Quit Game")
                    pygame.quit()
                    exit()

            elif event.key == pygame.K_UP:
                self.highlighted = max(1, self.highlighted - 1)

            elif event.key == pygame.K_DOWN:
                self.highlighted = min(2, self.highlighted + 1)
