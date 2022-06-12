import pygame, random
import maingame
import constant

def start_game():
    global SCREEN, clock
    pygame.init() #run pygame
    SCREEN = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT)) #Window
    pygame.display.set_caption('Memory Game') #Title
    clock = pygame.time.Clock() # Track time
    bg = pygame.Surface((constant.WIDTH,constant.HEIGHT))
    SCREEN.fill(constant.WHITE)
    maingame.display_text('Memory Game',600,250,100)
    maingame.display_text('Play',350,500,80)
    maingame.display_text('Exit',850,500,80)
    pygame.display.flip()
    running = True
    while(running):
        for event in pygame.event.get(): # QUIT
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                global mousex, mousey
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex>280 and mousex<420) and (mousey>450 and mousey<550):
                    SCREEN.fill(constant.BLACK)
                    maingame.levelone(maingame.playtime)
                elif (mousex>780 and mousex<915) and (mousey>455 and mousey<550):
                    pygame.quit()
                    quit()
    pygame.quit()