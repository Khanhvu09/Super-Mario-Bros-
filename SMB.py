import pygame 
import pytmx
from Mario import Mario
from pytmx.util_pygame import load_pygame
from pygame.sprite import Group, groupcollide

pygame.init()
clock = pygame.time.Clock()

screen_size = (600,460)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Super Mario Brothers')

mario = Mario()
marios = Group()
marios.add(mario)

mario_image = pygame.image.load('mario_38.png')

clock = pygame.time.Clock()
gameMap = pytmx.load_pygame("marioworld.png")
gameOn = True

while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mario.shouldMove('right')
            elif event.key == pygame.K_LEFT:
                mario.shouldMove('left')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mario.shouldMove('right', False)
            elif event.key == pygame.K_LEFT:
                mario.shouldMove('left', False)

    for layer in gameMap.visible_layers:
        for x, y, gid, in layer:
            tile = gameMap.get_tile_image_by_gid(gid)
            pygame_screen.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))

    

    # if event.type == pygame.K_RIGHT:
    mario.draw_me()
    for mario in marios:
        pygame_screen.blit(mario_image,[mario.x,mario.y])



    pygame.display.update()
    clock.tick(30)

