import pygame


class Bomb:
    def __init__(self,pos_x, pos_y):
        self.pos_x = (pos_x+20)//40 * 40
        self.pos_y = (pos_y+20)//40 * 40 
        self.timer = 0
    
    def draw(self,win):
        pygame.draw.rect(win, (0,255,0), (self.pos_x+10, self.pos_y + 10, 20, 20) )


class Bomb_List:
    def __init__(self, player):
        self.list = []
        self.player = player

    def draw(self, windows):
        for bomb in self.list:
            bomb.draw(windows)



    def clean(self,msec):
        for bomb in self.list:
            if bomb.timer >= 2000:
                self.list.pop(self.list.index(bomb))
            else:
                bomb.timer += msec


class Bomb_List1(Bomb_List):
    def update(self,keys):
        if keys[pygame.K_z]:
            if len(self.list) < 2:
                if len(self.list):
                    for bomb in self.list:
                        if self.player.pos_x == bomb.pos_x and self.player.pos_y == bomb.pos_y:
                            break
                        else:
                            self.list.append(Bomb(self.player.pos_x, self.player.pos_y))
                else:
                    self.list.append(Bomb(self.player.pos_x, self.player.pos_y))    

class Bomb_List2(Bomb_List):
    def update(self,keys):
        if keys[pygame.K_SPACE]:
            if len(self.list) < 2:
                if len(self.list):
                    for bomb in self.list:
                        if self.player.pos_x == bomb.pos_x and self.player.pos_y == bomb.pos_y:
                            break
                        else:
                            self.list.append(Bomb(self.player.pos_x, self.player.pos_y))
                else:
                    self.list.append(Bomb(self.player.pos_x, self.player.pos_y))    



