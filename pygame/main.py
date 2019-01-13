import pygame
import PLAYERS as pls
import bomb as bmb
import BOX as bx
import FUNCTION as fnc
import json

def redraw():
    windows.blit(bg,(0,0))
    player1.draw(windows)
    player2.draw(windows)
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

######obj_List############
obj_list = fnc.Object_loc()
obj_list.appendlist(box.list)

##########################

pygame.init()

msec = 50
bg_size = (600,520)
pygame.display.set_caption("First Game")
bg = pygame.image.load('background.jpg')

windows = pygame.display.set_mode(bg_size)
player1 = pls.Player1(80,40,40,40,'player1')
player2 = pls.Player2(440,440,40,40,'player2')
bomb1 = bmb.Bomb_List1(player1)
bomb2 = bmb.Bomb_List2(player2)

run = True
###########MAIN_Loop####################
while run:

    ########## system check ###########
    pygame.time.delay(msec)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    ###################################

    player1.update(keys, bg_size)
    player2.update(keys, bg_size)
    player1.box_detect(box_loc)
    player2.box_detect(box_loc)


    ##bomb
    bomb1.clean(msec)
    bomb2.clean(msec)
    bomb1.update(keys)
    bomb2.update(keys)


    redraw()

    




    