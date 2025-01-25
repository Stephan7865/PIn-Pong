from pygame import *

win_width = 1800
win_height = 900
window = display.set_mode((win_width, win_height))
display.set_caption('Пин-Понг')
background = transform.scale(image.load('pin pong.png'),(win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, weight, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (weight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 65:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_width - 65:
            self.rect.y += self.speed
Ball=GameSprite('ball1.png', 900, 450,110,110,10)
die1= Player('плашка.png', 50, 50,40,200,10)
die2= Player('плашка.png', 1700, 730,40,200,10)

font.init()
font1 = font.SysFont('Arial', 36)
lose1 = font1.render('Левый игрок проиграл', True, (219, 15, 15))
lose2 = font1.render('Правый игрок проигал', True, (219, 15, 15))


speed_y = Ball.speed
speed_x = Ball.speed
game = True
FPS=60
clock = time.Clock()
final = False
while game:
    window.blit(background, (0, 0))
    die1.reset()
    die2.reset()
    Ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not final:
        die1.update_1()
        die2.update_2()
        Ball.rect.y += speed_y
        Ball.rect.x += speed_x
        if Ball.rect.y < 0 or Ball.rect.y > 800:
            speed_y *= -1
        if sprite.collide_rect(Ball, die1) or sprite.collide_rect(Ball, die2):
            speed_x *= -1
        if Ball.rect.x < 0:
            final = True
            window.blit(lose1, (750,400))
        if Ball.rect.x > 1750:
            final = True
            window.blit(lose2, (750,400))
        


        

        display.update()
        time.delay(1)
    time.delay(50)
