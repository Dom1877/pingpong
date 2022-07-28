import pygame
from pygame import *
pygame.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()    
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update(self):
        keys = key.get_pressed()    
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

clock = time.Clock()
FPS = 60

player_1 = Player( 30, 200, 4, 50, 150) 
player_2 = Player( 520, 200, 4, 50, 150)

'''speed_x = 3
speed_y = 3'''

bg = (75, 159, 181)
win_width = 600
win_height = 500
display.set_caption("Pong")
window = display.set_mode((win_width, win_height))
window.fill(bg)

finish = False

running = True
while running:
    for e in event.get():
        if e.type  == QUIT:
            running = False
    display.update()
