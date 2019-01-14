import pygame

class option():
    def __init__(self, mode):
        self.mode = 1

    def operate(self, keys):
        if keys[pygame.K_LEFT]:
            self.mode -= 1
            if self.mode <= 0:
                self.mode = 0
        if keys[pygame.K_RIGHT]:
            self.mode += 1
            if self.mode >= 2:
                self.mode = 2

    def print_option(self, windows):       
        pygame.draw.rect(windows,(155,155,25), (75+ self.mode*150,280,150,80))