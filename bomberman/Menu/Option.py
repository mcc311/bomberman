import pygame
import json

with open("Menu\\stage_adrs.json") as load:
    stage_adrs = json.load(load)



class option():
    def __init__(self):
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
        windows.blit(pygame.image.load(stage_adrs["stage"+str(self.mode)]),(375,300,450,390))        
