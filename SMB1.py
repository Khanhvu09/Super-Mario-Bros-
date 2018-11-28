import pygame 
from Mario import Mario
from pygame.sprite import Group, groupcollide



pygame.init()

screenSize = (600,460)

pygame_screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('Super Mario Brothers')

backgroundImage = pygame.image.load('marioworld.png')


clock = pygame.time.Clock()
mario = Mario()
marios = Group()
marios.add(mario)
gameOn = True
x = mario.x
y = mario.y
print (x) 
print (y) 
bgX = 0
bgY = 0
vel = 5
jumpCount = 10
isJump = 10

while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mario.shouldMove('right')
            if event.key == pygame.K_LEFT:
                mario.shouldMove('left')
            if event.key == pygame.K_SPACE:
                
                # jsJump = True
                # if jumpCount >= -10:
                #     neg = 1
                #     if jumpCount < 0:
                #         neg = -1

                #         y -= (jumpCount ** 2) * 0.5 *neg
                #         jumpCount -= 1
                #     else:
                #         isJump = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mario.shouldMove('right', False)
            elif event.key == pygame.K_LEFT:
                mario.shouldMove('left', False)
            # if event.key == pygame.K_SPACE:
                

    pygame_screen.blit(backgroundImage, [bgX,bgY])

    for mario in marios:
        mario.draw_me()
        pygame_screen.blit(mario.image, [mario.x, mario.y])

    pygame.display.update()

    clock.tick(16)