import pygame
import PLAYERS as pls
import bomb as bmb
import BOX as bx
import OBJECT_LIST as obj
import json

def redraw():
    windows.blit(bg,(0,0))
    for player in players:
        player.draw(windows)
    bomb1.draw(windows)
    bomb2.draw(windows)
    box.draw(windows)
    pygame.display.update()


#########BOX##############
with open('box_loc.json') as load:
    box_loc = json.load(load)
box = bx.Box_List()
box.update(box_loc)
#########################

###############Players_Setting###############
player1 = pls.Player1(0,0,40,40,'player1')
player2 = pls.Player2(560,480,40,40,'player2')
players = [player1, player2]
#############################################

#########Bomb_Setting###########
bomb1 = bmb.Bomb_List1(player1)
bomb2 = bmb.Bomb_List2(player2)
################################


######obj_List############
obj_list = obj.Object_loc()
##########################
5
pygame.init()

msec = 75
bg_size = (600,520)
pygame.display.set_caption("First Game")
bg = pygame.image.load('background.jpg')
windows = pygame.display.set_mode(bg_size)

run = True
###########MAIN_Loop####################
while run:


    ########## system check ########
    pygame.time.delay(msec)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    ################################


    ########### object check #######
    obj_list.clear_list()
    obj_list.appendlist(box.list)
    obj_list.appendlist(bomb1.list)
    obj_list.appendlist(bomb2.list)
    obj_list.appendlist(player1)
    obj_list.appendlist(player2)
    ################################


    ########## player move #########
    player1.update(keys, bg_size, obj_list)
    player2.update(keys, bg_size, obj_list)
    ################################


    ##bomb
    bomb1.clean(msec, players)
    bomb2.clean(msec, players)
    bomb1.update(keys)
    bomb2.update(keys)


    redraw()

    



    