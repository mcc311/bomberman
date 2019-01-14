import pygame


class Bomb:
    def __init__(self,pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y 
        self.timer = 0
        self.Type = 'bomb'
        self.attack_range = 1
    def draw(self,win):
        pygame.draw.rect(win, (0,255,0), (self.pos_x+10, self.pos_y + 10, 20, 20) )

    def kill(self, player_list):
        for player in player_list:
            if  (player.pos_x == self.pos_x - 40*self.attack_range and player.pos_y == self.pos_y) or\
                (player.pos_x == self.pos_x + 40*self.attack_range and player.pos_y == self.pos_y) or\
                (player.pos_x == self.pos_x  and player.pos_y == self.pos_y + 40*self.attack_range) or\
                (player.pos_x == self.pos_x  and player.pos_y == self.pos_y - 40*self.attack_range):
                player.alive = False
                player_list.pop(player_list.index(player))

    def destroy(self, box_list):
        for box in box_list.list:
            if  (box.pos_x == self.pos_x - 40*self.attack_range and box.pos_y == self.pos_y) or\
                (box.pos_x == self.pos_x + 40*self.attack_range and box.pos_y == self.pos_y) or\
                (box.pos_x == self.pos_x  and box.pos_y == self.pos_y + 40*self.attack_range) or\
                (box.pos_x == self.pos_x  and box.pos_y == self.pos_y - 40*self.attack_range):
                box_list.list.pop(box_list.list.index(box))
                



class Bomb_List:
    def __init__(self, player):
        self.list = []
        self.player = player

    def draw(self, windows):
        for bomb in self.list:
            bomb.draw(windows)

    def clean(self,msec,player_list, box_list):
        for bomb in self.list:
            if bomb.timer >= 2000:
                bomb.kill(player_list)
                bomb.destroy(box_list)
                self.list.pop(self.list.index(bomb))
                

            else:
                bomb.timer += msec


class Bomb_List1(Bomb_List):
    def update(self,keys):
        if keys[pygame.K_q]:
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
        if keys[pygame.K_RETURN]:
            if len(self.list) < 2:
                if len(self.list):
                    for bomb in self.list:
                        if self.player.pos_x == bomb.pos_x and self.player.pos_y == bomb.pos_y:
                            break
                        else:
                            self.list.append(Bomb(self.player.pos_x, self.player.pos_y))
                else:
                    self.list.append(Bomb(self.player.pos_x, self.player.pos_y))    



