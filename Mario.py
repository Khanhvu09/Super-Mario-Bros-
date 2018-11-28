import pygame 
from pygame.sprite import Sprite

class Mario(Sprite):
    def __init__(self):
        super(Mario, self).__init__()
        self.x = 0
        self.y = 400
        self.speed = 8
        self.should_move_right = False
        self.should_move_left = False
        self.should_move_jump = False
        self.image = pygame.image.load('mario_38.png')
        self.images = ['mario_38.png', 'mario_39.png', 'mario_40.png']
        self.rImages = ['mario_35.png', 'mario_34.png', 'mario_33.png']
        self.counter = 0
        # self.marios = []
        # self.marios.append(pygame.image.load('mario_38.png'))
        # self.marios.append(pygame.image.load('mario_39.png'))
        # self.marios.append(pygame.image.load('mario_40.png'))
        # self.img = self.marios[0]
        # self.cur_mario = 0

    def shouldMove(self, direction, start = True):
        if direction == "right":
            self.should_move_right = start 
            # self.cur_mario += 1
            # if self.cur_mario > 2:
            #     self.cur_mario = 0
        # self.img = self.marios[self.cur_mario]
        if direction == "left":
            self.should_move_left = start 
      
    def draw_me(self):
        
        if self.should_move_right:
            self.x += self.speed
            self.image = pygame.image.load(self.images[self.counter])
            self.counter = (self.counter + 1) % len(self.images)
            # y = y + 5
        elif self.should_move_left:
            self.x -= self.speed
            self.image = pygame.image.load(self.rImages[self.counter])
            self.counter = (self.counter + 1) % len(self.rImages)