import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill("red")
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0,300)) 
    pygame.display.update()
    clock.tick(60)