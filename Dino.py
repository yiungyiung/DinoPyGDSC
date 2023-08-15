import pygame

# pygame setup
pygame.init()
# (w,h)$topleft(0,0)$botright(800,400)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("gamename")  # set game name
clock = pygame.time.Clock()

# Game Variables
running = True


# Surface and images
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Cactus
cactus = pygame.image.load('graphics/Cactus.png').convert_alpha()
cactus = pygame.transform.scale(cactus, (50, 70))
cactusrect = cactus.get_rect(midbottom=(700, 300))

# Player
Dino = pygame.image.load('graphics/Dino1.png').convert_alpha()
Dino = pygame.transform.scale(Dino, (100, 100))
Dinorect = Dino.get_rect(midbottom=(50, 315))

# Dino = pygame.transform.flip(Dino, True, False)

DinoGravity = 0

# Fonts
scorefont = pygame.font.Font("font/Pixeltype.ttf", 50)

txt_surface = scorefont.render("Dino Reworked", False, (0, 0, 255))
scorerect = txt_surface.get_rect(center=(400, 100))
while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if running:
            if event.type == pygame.KEYDOWN:
                print(Dinorect.bottom)
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and Dinorect.bottom >= 315:
                    DinoGravity = -10
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = True

    if running:
        # RENDER YOUR GAME HERE

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(txt_surface, scorerect)

        # Cactus Logic
        screen.blit(cactus, cactusrect)
        cactusrect.left -= 5
        if (cactusrect.right < 0):
            cactusrect.left = 700
        if cactusrect.colliderect(Dinorect):
            print("hit player")
            running = False
            cactusrect.left = 700

        # Player Logic
        screen.blit(Dino, Dinorect)
        DinoGravity += 0.3
        Dinorect.y += DinoGravity
        if Dinorect.bottom > 315:
            Dinorect.bottom = 315

    else:
        screen.fill("black")
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60
# test questions
# pygame.draw.line(screen, "black", (0,0), (800,400))
# if event.type == pygame.MOUSEBUTTONDOWN:
#   if(Dinorect.collidepoint(pygame.mouse.get_pos())):
#       print("mouse hit dino")
# keys=pygame.keys.get_pressed()
# keys[pygame.K_SPACE]
