import pygame

class Box:
    def __init__(self,pos_x,pos_y, Type):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 40
        self.height = 40
        self.Type = Type

    def draw(self,windows):
        if self.Type == 'undestroyable':
            pygame.draw.rect(windows,(0,0,0),(self.pos_x, self.pos_y, self.width, self.height))
        if self.Type == 'destroyable':
            pygame.draw.rect(windows,(123,123,123),(self.pos_x, self.pos_y, self.width, self.height))


class Box_List:
    def __init__(self):
        self.list = []

    def update(self, locs, Type):
        for loc in locs:
            self.list.append(Box(loc[0]*40, loc[1]*40,Type))

    def draw(self, windows):
        for box in self.list:
            box.draw(windows)



