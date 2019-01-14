import pygame
import Body.Object.PLAYERS  as pls
import Body.Object.Bomb.bomb as bmb
import Body.Object.BOX.BOX as bx
import Body.Object.OBJECT_LIST as obj
import json
import os

def game(game_map):
    def redraw():
        windows.blit(bg,(0,0))
        for player in players:
            player.draw(windows)
        bomb1.draw(windows)
        bomb2.draw(windows)
        unbox.draw(windows)
        box.draw(windows)
        pygame.display.update()


    #########BOX##############
    
    with open('Body\\Object\\BOX\\map_loc.json') as load:
        map_adrs = json.load(load)
    
    with open(map_adrs[str(game_map)]) as load:
        all_loc = json.load(load)

    unbox_loc = all_loc[0]
    box_loc = all_loc[1]
    player1_loc = all_loc[2][0]
    player2_loc = all_loc[2][1]

    unbox = bx.Box_List()
    unbox.update(unbox_loc, 'undestroyable')

    box = bx.Box_List()
    box.update(box_loc, 'destroyable')
    #########################

    ###############Players_Setting###############
    player1 = pls.Player1(40*player1_loc[0],40*player1_loc[1],40,40,'player1')
    player2 = pls.Player2(40*player2_loc[0],40*player2_loc[1],40,40,'player2')
    players = [player1, player2]
    #############################################

    #########Bomb_Setting###########
    bomb1 = bmb.Bomb_List1(player1)
    bomb2 = bmb.Bomb_List2(player2)
    ################################


    ######obj_List############
    obj_list = obj.Object_loc()
    ##########################
    ################ Global Setting #################
    pygame.init()

    msec = 75
    bg_size = (600,520)
    pygame.display.set_caption("First Game")
    bg = pygame.image.load(r'Body\Object\BackGround\map.jpg')
    windows = pygame.display.set_mode(bg_size)
    #################################################

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
        obj_list.appendlist(unbox.list)
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
        bomb1.clean(msec, players, box)
        bomb2.clean(msec, players, box)
        bomb1.update(keys)
        bomb2.update(keys)


        redraw()
