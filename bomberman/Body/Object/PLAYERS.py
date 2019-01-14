import pygame 
import json
g_img = []
with open("Body\\Object\\Players\\G\\g_move_img.json") as load:
    all_img = json.load(load)
for img in all_img:
    g_img.append(pygame.image.load(all_img[img]))

class Players:
    def __init__(self,pos_x,pos_y, width, height, Type):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.Type = Type
        self.alive = True
        self.vel = 40
        self.direction = 'up'




class Player1(Players):
    def update(self,keys,bg_size,locs,windows):
        if keys[pygame.K_a]:
            self.direction = 'left'
            if locs.collision_detect(self):
                windows.blit(g_img[5],(self.pos_x - self.width/2, self.pos_y))
                pygame.time.wait(100)
                self.pos_x -= self.vel
                if self.pos_x <= 0:
                    self.pos_x = 0
        if keys[pygame.K_d]:
            self.direction = 'right'
            if locs.collision_detect(self):
                windows.blit(g_img[7],(self.pos_x + self.width/2, self.pos_y))
                pygame.time.wait(100)
                self.pos_x += self.vel
                if self.pos_x >= bg_size[0] - self.width:
                    self.pos_x = bg_size[0] - self.width
        if keys[pygame.K_w]:
            self.direction = 'up'
            if locs.collision_detect(self):
                windows.blit(g_img[3],(self.pos_x, self.pos_y + self.height/2))
                pygame.time.wait(100)
                self.pos_y -= self.vel
                if self.pos_y <= 0:
                    self.pos_y = 0
        if keys[pygame.K_s]:
            self.direction = 'down'
            if locs.collision_detect(self):
                windows.blit(g_img[1],(self.pos_x, self.pos_y - self.height/2))
                pygame.time.wait(100)
                self.pos_y += self.vel
                if self.pos_y >= bg_size[1] - self.height:
                    self.pos_y = bg_size[1] - self.height
    def draw(self,windows):
        if self.direction == 'right':
            windows.blit(g_img[6],(self.pos_x, self.pos_y))
        if self.direction == 'left':
            windows.blit(g_img[4],(self.pos_x, self.pos_y))
        if self.direction == 'up':
            windows.blit(g_img[2],(self.pos_x, self.pos_y))
        if self.direction == 'down':
            windows.blit(g_img[0],(self.pos_x, self.pos_y))
    
class Player2(Players):
    def update(self,keys,bg_size, locs, windows):
        if keys[pygame.K_LEFT]:
            self.direction = 'left'
            if locs.collision_detect(self):
                self.pos_x -= self.vel
                if self.pos_x <= 0:
                    self.pos_x = 0
        if keys[pygame.K_RIGHT]:
            self.direction = 'right'
            if locs.collision_detect(self):
                self.pos_x += self.vel
                if self.pos_x >= bg_size[0] - 40:
                    self.pos_x = bg_size[0] - 40
        if keys[pygame.K_UP]:
            self.direction = 'up'
            if locs.collision_detect(self):
                self.pos_y -= self.vel
                if self.pos_y <= 0:
                    self.pos_y = 0
        if keys[pygame.K_DOWN]:
            self.direction = 'down'
            if locs.collision_detect(self):
                self.pos_y += self.vel
                if self.pos_y >= bg_size[1] - 40:
                    self.pos_y = bg_size[1] - 40

    def draw(self,windows):
        pygame.draw.rect(windows, (255,0,0), (self.pos_x,self.pos_y, self.width, self.height))