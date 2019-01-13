import pygame 


class Players:
    def __init__(self,pos_x,pos_y, width, height, Type):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.Type = Type
        self.alive = True
        self.vel = 40
        self.counter = True
    def draw(self,windows):
        pygame.draw.rect(windows, (255,0,0), (self.pos_x,self.pos_y, self.width, self.height))

    def box_detect(self, box_locs):
        for loc in box_locs:
            if self.pos_x == loc[0] and self.pos_y == loc[1]:
                if self.direction == 'left':
                    self.pos_x += self.width
                if self.direction == 'right':
                    self.pos_x -= self.width
                if self.direction == 'up':
                    self.pos_y += self.height
                if self.direction == 'down':
                    self.pos_y -= self.height


                
    

class Player1(Players):
    def update(self,keys,bg_size,locs):
        if keys[pygame.K_a]:
            self.direction = 'left'
            if locs.collision_detect(self):
                self.pos_x -= self.vel
                if self.pos_x <= 0:
                    self.pos_x = 0
        if keys[pygame.K_d]:
            self.direction = 'right'
            if locs.collision_detect(self):
                self.pos_x += self.vel
                if self.pos_x >= bg_size[0] - self.width:
                    self.pos_x = bg_size[0] - self.width
        if keys[pygame.K_w]:
            self.direction = 'up'
            if locs.collision_detect(self):
                self.pos_y -= self.vel
                if self.pos_y <= 0:
                    self.pos_y = 0
        if keys[pygame.K_s]:
            self.direction = 'down'
            if locs.collision_detect(self):
                self.pos_y += self.vel
                if self.pos_y >= bg_size[1] - self.height:
                    self.pos_y = bg_size[1] - self.height
    
class Player2(Players):
    def update(self,keys,bg_size, locs):
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

