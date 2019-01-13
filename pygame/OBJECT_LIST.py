


class Object_loc():
    def __init__(self):
        self.list = []

    def appendlist(self, obj_list):
        if type(obj_list) == list:
            for obj in obj_list:
                self.list.append(obj)
        else:
            self.list.append(obj_list)
        
    def collision_detect(self,player):
        counter = 0
        for obj in self.list:
            if player.Type != obj.Type:
                if player.direction == 'left':
                    if player.pos_x - player.width == obj.pos_x and player.pos_y == obj.pos_y:
                        counter += 1
                if player.direction == 'right':
                    if player.pos_x + player.width == obj.pos_x and player.pos_y == obj.pos_y:
                        counter +=1
                if player.direction == 'up':
                    if player.pos_x == obj.pos_x and player.pos_y - player.height == obj.pos_y:
                        counter +=1
                if player.direction == 'down':
                    if player.pos_x == obj.pos_x and player.pos_y + player.height == obj.pos_y:
                        counter +=1
        return (not counter)

    def clear_list(self):
        self.list = []
                