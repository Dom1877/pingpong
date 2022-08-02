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
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()    
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()    
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

clock = time.Clock()
FPS = 60

racket1 = Player('paddle_left.png', 30, 200, 4, 50, 150) 
racket2 = Player('paddle_right.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER ONE LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER TWO LOSE', True, (180, 0, 0))

speed_x = 3
speed_y = 3

bg = (96, 169, 188)
screen_width, screen_height = 600, 500
display.set_caption("Pong")
screen = display.set_mode((screen_height, screen_width))
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)
screen.fill(bg)

running = True
finish = False




if finish != True:
    racket1.update_left()
    racket2.update_right()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1
    if ball.rect.y > screen_height -50 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x < 0:
        finish = True
        screen.blit(lose1, (200, 200))
        game_over = True
    if ball.rect.x > screen_width:
        finish = True
        screen.blit(lose2, (200, 200))
        game_over = True



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        racket1.reset()
        racket2.reset()
        ball.reset()

    pygame.display.update()
    clock.tick(FPS)
    
