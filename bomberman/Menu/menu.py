import pygame
import Menu.Option as opt
import json


with open("Menu\\Background\\bg_adrs.json") as load:
    bg_adrs = json.load(load)
def menu():

    def redraw():
        windows.blit(bg,(0,0))
        optr.print_option(windows)
        pygame.display.update()
        
    pygame.init()
    msec = 75
    bg_size = (1200,800)
    pygame.display.set_caption("***Menu***")
    bg = pygame.image.load(bg_adrs["cover"])
    windows = pygame.display.set_mode(bg_size)

    optr = opt.option()

    run = True
    while run:
        pygame.time.delay(msec)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            
            for j in range(2):
                for i in range(4):
                    loading = pygame.image.load(bg_adrs['loading'+str(i)])
                    windows.blit(loading,(0,0))
                    pygame.display.update()
                    pygame.time.delay(500)
            return optr.mode
            run = False

        optr.operate(keys)
        redraw()

        

        