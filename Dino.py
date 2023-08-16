import random as rand

import pygame

# pygame setup
pygame.init()
pygame.mixer.init()
# (w,h)$topleft(0,0)$botright(800,400)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("DinoReworked")  # set game name
clock = pygame.time.Clock()

#audio
jump=pygame.mixer.Sound("assets/audio/jump.wav")
death=pygame.mixer.Sound("assets/audio/death.wav")

# Game Variables
running = True
score=0
starttime = 0
Cactspeed=5
nextscorelim=100

# Surface and images
sky_surface = pygame.image.load('assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()

# Cactus
cactus = pygame.image.load('assets/graphics/Cactus.png').convert_alpha()
cactus = pygame.transform.scale(cactus, (50, 70))
cactusrect = cactus.get_rect(midbottom=(700, 300))

# Player
Dino = pygame.image.load('assets/graphics/Dino1.png').convert_alpha()
pygame.display.set_icon(Dino)
Dino = pygame.transform.scale(Dino, (100, 100))
Dinorect = Dino.get_rect(midbottom=(50, 315))
DinoGravity = 0
# Dino = pygame.transform.flip(Dino, True, False)

#cloud
cloud1=pygame.image.load("assets/graphics/cloud.png").convert_alpha()
cloud1 =pygame.transform.scale(cloud1,(50,25))
cloud1rect=cloud1.get_rect(center=(700,100))

#deathscreen
deathsc=pygame.image.load("assets/graphics/Death.jpg").convert()
deathsc=pygame.transform.scale(deathsc,(800,400))

# Fonts
font = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
deathfont = pygame.font.Font("assets/font/Pixeltype.ttf", 75)
score_txt=font.render(str(score), False, (0, 0, 255))
score_rect=score_txt.get_rect(center=(700,50))

txt_surface = font.render("Dino Reworked", False, (0, 0, 255))
namerect = txt_surface.get_rect(center=(400, 50))

gameover_txt=deathfont.render("Game Over", False, (255,0,0))
gameover_rect=gameover_txt.get_rect(midbottom=(420,150))

gameover_txt1=deathfont.render("Press Enter to continue", False, (255,0,0))
gameover_rect1=gameover_txt.get_rect(midbottom=(280,150+75))

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if running:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and Dinorect.bottom >= 315:
                    DinoGravity = -10
                    jump.play()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = True
                    starttime=pygame.time.get_ticks()
                    
    if running:
        # RENDER YOUR GAME HERE
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(txt_surface, namerect)

        #cloud
        screen.blit(cloud1,cloud1rect)
        cloud1rect.left-=2
        if(cloud1rect.right<0):
            cloud1rect.left=800
            cloud1rect.top=rand.choice([50,100,150,25])

        # Cactus Logic
        screen.blit(cactus, cactusrect)
        cactusrect.left -= Cactspeed
        if score>nextscorelim:
            Cactspeed+=1
            nextscorelim=nextscorelim+100
        if (cactusrect.right < 0):#cactus back to pos
            cactusrect.left = 700
            score+=1
        if cactusrect.colliderect(Dinorect):#cactus collision
            print("hit player")
            running = False
            cactusrect.left = 700
            Dinorect.bottom = 315
            Cactspeed=5
            death.play()

        # Player Logic
        screen.blit(Dino, Dinorect)
        DinoGravity += 0.3
        Dinorect.y += DinoGravity
        if Dinorect.bottom > 315:
            Dinorect.bottom = 315

        #Score
        score=int((pygame.time.get_ticks()-starttime)/100)
        #print(score)
        score_txt=font.render(str(score), False, (0, 0, 255))
        screen.blit(score_txt,score_rect)

    else:
        score=0
        screen.blit(deathsc,(0,0))
        screen.blit(gameover_txt,gameover_rect)
        screen.blit(gameover_txt1,gameover_rect1)



    pygame.display.update()
    clock.tick(60)  # limits FPS to 60
# test questions
# pygame.draw.line(screen, "black", (0,0), (800,400))
# if event.type == pygame.MOUSEBUTTONDOWN:
#   if(Dinorect.collidepoint(pygame.mouse.get_pos())):
#       print("mouse hit dino")
# keys=pygame.keys.get_pressed()
# keys[pygame.K_SPACE]
#pygame.display.set_icon(pygame_icon)
