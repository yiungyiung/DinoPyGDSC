import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
xpos=200
ypos=200
gravity = 0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                gravity=-10
            #xpos,ypos=pygame.mouse.get_pos()
    screen.fill("yellow")
    
    pygame.draw.circle(screen,"red",(xpos,ypos),50)
    gravity+=0.3
    ypos+=gravity
    if ypos>300:
        ypos=300
        gravity=0
    #xpos=xpos-1
    pygame.display.update()
    clock.tick(60)

