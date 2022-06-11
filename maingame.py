import pygame, random
import constant

playtime = 0
mousex = 0
mousey = 0
imagelist = []
tilelist = []
twoclicks = []
clickedbox = []
matched = []

# Adding images to a list
imagelist.append(constant.aard)
imagelist.append(constant.axii)
imagelist.append(constant.igni)
tilelist.append(constant.tile)

# Making 6 pairs
imagelist *=4
tilelist*=12

def display_text(writetext,textx,texty,size):
    "Loading text to be used in other functions"
    font = pygame.font.Font(constant.fontname,size)
    text = font.render(writetext,True,constant.WHITE,constant.BLACK)
    textRect = text.get_rect()
    textRect.center = (textx, texty)
    SCREEN.blit(text, textRect)
    pygame.display.flip()

def timer(gametime,playtime):
    "Countdown timer"
    timeleft=((playtime+gametime)-pygame.time.get_ticks())//1000
    font = pygame.font.Font(constant.fontname, 50)
    time = font.render(' Time: 0:' + str(timeleft)+"  ",True,constant.WHITE, constant.BLACK)
    timeRect = time.get_rect()
    timeRect.center = (1000,100)
    SCREEN.blit(time, timeRect)
    pygame.display.flip()
    return(timeleft)

def drawallcovers():
    "Drawing all cover tiles"
    tX=0  # tile row x coordinate
    tY=0  # tile row y coordinate
    j=0   # tilelist index

    for i in range(0,4):    # Creating 1st row of tiles
        i+=j
        SCREEN.blit(tilelist[j], (tX,tY))
        tX+=200
    for i in range(5,9):  # Creating 2nd row of tiles
        i+=j
        SCREEN.blit(tilelist[j], (tX-800,tY+200))
        tX+=200
    for i in range(9,13): # Creating 3rd row of tiles
        i+=j
        SCREEN.blit(tilelist[j], (tX-1600,tY+400))
        tX+=200

def drawallpairs():
    "Drawing all image pairs"
    iX=0 # image row x coordinate
    iY=0 # image row y coordinate
    k=0  # imagelist index

    for i in range(0,4): # Creating 1st row of images
        SCREEN.blit(imagelist[k], (iX,iY))
        k+=1
        iX+=200
    for i in range(5,9):  # Creating 2nd row of images
        SCREEN.blit(imagelist[k], (iX-800,iY+200))
        k+=1
        iX+=200
    for i in range(9,13): # Creating 3rd row of images
        SCREEN.blit(imagelist[k], (iX-1600,iY+400))
        k+=1
        iX+=200

def displaycover(index):
    "Drawing one cover at a time"
    if(index==0):
        SCREEN.blit(tilelist[0], (0,0))
    elif(index==1):
        SCREEN.blit(tilelist[1], (200,0))
    elif(index==2):
        SCREEN.blit(tilelist[2], (400,0))
    elif(index==3):
        SCREEN.blit(tilelist[3], (600,0))
    elif(index==4):
        SCREEN.blit(tilelist[4], (0,200))
    elif(index==5):
        SCREEN.blit(tilelist[5], (200,200))
    elif(index==6):
        SCREEN.blit(tilelist[6], (400,200))
    elif(index==7):
        SCREEN.blit(tilelist[7], (600,200))
    elif(index==8):
        SCREEN.blit(tilelist[8], (0,400))
    elif(index==9):
        SCREEN.blit(tilelist[9], (200,400))
    elif(index==10):
        SCREEN.blit(tilelist[10], (400,400))
    elif(index==11):
        SCREEN.blit(tilelist[11], (600,400))
    
def displayimage(index):
    "Drawing one image at a time"
    if(index==0):
        SCREEN.blit(imagelist[0], (0,0))
    elif(index==1):
        SCREEN.blit(imagelist[1], (200,0))
    elif(index==2):
        SCREEN.blit(imagelist[2], (400,0))
    elif(index==3):
        SCREEN.blit(imagelist[3], (600,0))
    elif(index==4):
        SCREEN.blit(imagelist[4], (0,200))
    elif(index==5):
        SCREEN.blit(imagelist[5], (200,200))
    elif(index==6):
        SCREEN.blit(imagelist[6], (400,200))
    elif(index==7):
        SCREEN.blit(imagelist[7], (600,200))
    elif(index==8):
        SCREEN.blit(imagelist[8], (0,400))
    elif(index==9):
        SCREEN.blit(imagelist[9], (200,400))
    elif(index==10):
        SCREEN.blit(imagelist[10], (400,400))
    elif(index==11):
        SCREEN.blit(imagelist[11], (600,400))

def box_pos(mousex,mousey):
    "Getting position of clicked box and giving it a number"
    boxx = int(mousex/constant.BOXSIZE)
    boxy = int(mousey/constant.BOXSIZE)
    
    if len(twoclicks)==2:
        del twoclicks[:3]

    if(boxx==0 and boxy==0):
        box = 0
        displayimage(0)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==1 and boxy==0):
        box = 1
        displayimage(1)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==2 and boxy==0):
        box = 2
        displayimage(2)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==3 and boxy==0):
        box = 3
        displayimage(3)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==0 and boxy==1):
        box = 4
        displayimage(4)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==1 and boxy==1):
        box = 5
        displayimage(5)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==2 and boxy==1):
        box = 6
        displayimage(6)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==3 and boxy==1):
        box = 7
        displayimage(7)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==0 and boxy==2):
        box = 8
        displayimage(8)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==1 and boxy==2):
        box = 9
        displayimage(9)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==2 and boxy==2):
        box = 10
        displayimage(10)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==3 and boxy==2):
        box = 11
        displayimage(11)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    return box

def won(score,playtime,gametime):
    timeleft=(gametime-pygame.time.get_ticks())//1000
    playtime=(60-timeleft)
    score+=timeleft
    SCREEN.fill(constant.BLUE)
    display_text("You Won",600,300,80)
    display_text("Score: "+str(score),600,400,50)
    display_text("Time: 0:"+str(playtime),600,500,50)
    display_text("Play Level 2",300,700,50)
    display_text("Play Again",580,700,50)
    display_text("Exit",800,700,50)
    pygame.display.flip()
    pygame.time.wait(1000)
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex>175 and mousex<420) and (mousey>675 and mousey<725):
                    timeleft=(gametime-pygame.time.get_ticks())//1000
                    timeleftwin = timeleft
                    playtime=(60-timeleftwin)*1000
                    SCREEN.fill(constant.BLACK)
                    leveltwo(playtime)
                if (mousex>475 and mousex<685) and (mousey>650 and mousey<750):
                    timeleft=(gametime-pygame.time.get_ticks())//1000
                    timeleftwin = timeleft
                    playtime=(60-timeleftwin)*1000
                    print(playtime)
                    SCREEN.fill(constant.BLACK)
                    levelone(playtime)
                elif (mousex>760 and mousex<840) and (mousey>675 and mousey<725):
                    pygame.quit()
                    quit()

def lost(gametime,playtime):
    SCREEN.fill(constant.RED)
    display_text("You Lost",600,250,80)
    display_text("Play Again",350,500,50)
    display_text("Exit",850,500,50)
    pygame.display.flip()
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex>280 and mousex<420) and (mousey>450 and mousey<550):
                    timeleft=(gametime-pygame.time.get_ticks())//1000
                    timeleftwin = timeleft
                    playtime=(60-timeleftwin)*1000
                    SCREEN.fill(constant.BLACK)
                    levelone(playtime)
                elif (mousex>780 and mousex<915) and (mousey>455 and mousey<550):
                    pygame.quit()
                    quit()

def levelone(playtime):
    drawallcovers()
    shuffle = random.shuffle(imagelist) # Shuffle the image position      
    score=0
    gametime = 61500
    matched = []
    display_text("Score: "+str(score),1000,200,50)
    running = True
    while(running): #Game loop
        # Events
        for event in pygame.event.get(): # QUIT
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex<800 and mousey<600):
                    box_pos(mousex,mousey)
                    if(len(twoclicks)==2):
                        if(imagelist[twoclicks[0]])==(imagelist[twoclicks[1]]):
                            matched.append(imagelist[twoclicks[0]])
                            matched.append(imagelist[twoclicks[1]])
                            score+=20
                            display_text("Score: "+str(score),1000,200,50)
                        else:
                            cover1 = int(twoclicks[0])
                            cover2 = int(twoclicks[1])
                            displayimage(cover1)
                            displayimage(cover2)
                            pygame.display.flip()
                            pygame.time.wait(450)
                            displaycover(cover1) 
                            displaycover(cover2)
        timer(gametime,playtime)
        timeleft=((gametime+playtime)-pygame.time.get_ticks())//1000
        if(timeleft)<=0:
            lost(gametime,playtime)
        if(len(matched)==12):
            pygame.time.wait(500)
            won(score,playtime,gametime)
            running = False
        clock.tick(constant.FPS)
        pygame.display.flip()
    pygame.quit()

def leveltwo(playtime):
    shuffle = random.shuffle(imagelist) # Shuffle the image position   
    drawallpairs()
    pygame.display.flip()
    pygame.time.wait(8000)
    drawallcovers()      
    score=0
    gametime = 69500
    matched = []
    display_text("Score: "+str(score),1000,200,50)
    running = True
    while(running): #Game loop
        # Events
        for event in pygame.event.get(): # QUIT
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex<800 and mousey<600):
                    box_pos(mousex,mousey)
                    if(len(twoclicks)==2):
                        if(imagelist[twoclicks[0]])==(imagelist[twoclicks[1]]):
                            matched.append(imagelist[twoclicks[0]])
                            matched.append(imagelist[twoclicks[1]])
                            score+=20
                            display_text("Score: "+str(score),1000,200,50)
                        else:
                            cover1 = int(twoclicks[0])
                            cover2 = int(twoclicks[1])
                            displayimage(cover1)
                            displayimage(cover2)
                            pygame.display.flip()
                            pygame.time.wait(450)
                            displaycover(cover1) 
                            displaycover(cover2)
        timer(gametime,playtime)
        timeleft=((gametime+playtime)-pygame.time.get_ticks())//1000
        if(timeleft)<=0:
            lost(gametime,playtime)
        if(len(matched)==12):
            pygame.time.wait(500)
            won(score,playtime,gametime)
            running = False
        clock.tick(constant.FPS)
        pygame.display.flip()
    pygame.quit()

def start_game():
    global SCREEN, clock
    pygame.init() #run pygame
    SCREEN = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT)) #Window
    pygame.display.set_caption('Memory Game') #Title
    clock = pygame.time.Clock() # Track time
    bg = pygame.Surface((constant.WIDTH,constant.HEIGHT))
    SCREEN.fill(constant.WHITE)
    display_text('Memory Game',600,250,100)
    display_text('Play',350,500,80)
    display_text('Exit',850,500,80)    
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
                    levelone(playtime) 
                elif (mousex>780 and mousex<915) and (mousey>455 and mousey<550):
                    pygame.quit()
                    quit()
    pygame.quit()    
start_game()
