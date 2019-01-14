import pygame
import Menu.Option as opt




def menu():

    def redraw():
        windows.blit(bg,(0,0))
        optr.print_option(windows)
        pygame.display.update()
        
    pygame.init()
    msec = 75
    bg_size = (600,520)
    pygame.display.set_caption("First Game")
    bg = pygame.image.load(r'Menu\Background\sample.jpg')
    windows = pygame.display.set_mode(bg_size)

    optr = opt.option(1)

    run = True
    while run:
        pygame.time.delay(msec)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            windows.fill((0,0,0))
            #pygame.time.delay(3000)
            game_mode = optr.mode
            run = False

        optr.operate(keys)
        redraw()

        

        