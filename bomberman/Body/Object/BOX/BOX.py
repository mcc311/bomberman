import pygame
import random 
import json

with open("Body\\Object\\BOX\\box_adrs.json") as load:
    img_adrs = json.load(load)

box_img = pygame.image.load(img_adrs['box'])

stone_img = []
for i in range(3):
    stone_img.append(pygame.image.load(img_adrs['stone'+str(i)]))


class Box:
    def __init__(self,pos_x,pos_y, Type):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 40
        self.height = 40
        self.Type = Type

    def draw(self,windows):
        if self.Type == 'undestroyable':
            windows.blit(stone_img[0],(self.pos_x, self.pos_y))
        if self.Type == 'destroyable':
            windows.blit(box_img,(self.pos_x, self.pos_y  ))


class Box_List:
    def __init__(self):
        self.list = []

    def update(self, locs, Type):
        for loc in locs:
            self.list.append(Box(loc[0]*40, loc[1]*40,Type))

    def draw(self, windows):
        for box in self.list:
            box.draw(windows)



