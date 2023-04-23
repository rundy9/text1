from pygame import *
font.init()
window = display.set_mode((700,500))
display.set_caption('ping')
FPS = 40
clock = time.Clock()
win_txt = font.SysFont('verdana', 70, bold = True).render('YOU WIN!', True, (100, 240, 50))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(img) , (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x ,self.rect.y))

class Player1(GameSprite):
    def update(self):        
        key.pressed = key.get_pressed()
        if key.pressed[K_w] and self.rect.x > 11:
            self.rect.x -= self.speed
        if key.pressed[K_s] and self.rect.x < 640:
            self.rect.x += self.speed

class Player2(GameSprite):
    def update(self):        
        key.pressed = key.get_pressed()
        if key.pressed[K_UP] and self.rect.x > 11:
            self.rect.x -= self.speed
        if key.pressed[K_DOWN] and self.rect.x < 640:
            self.rect.x += self.speed

class Ball(GameSprite):
    def iscollide(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


player1 = Player1(10, 2, 50, 25, 'platform.png', 10)
player2 = Player2(690, 498, 50, 25, 'platform.png', 10)
#ball = 

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:    
            run = False
        if move_r:
            platform.rect.x += 5
        if move_l:
            platform.rect.x -= 5
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.colliderect(platform.rect):
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            speed_y *= -1
        if ball.rect.x > 450 or ball.rect.x < 0:
            speed_x *= -1
    
    if not finish:
        window.blit(background, (0, 0))
        player1.reset()
        player2.update()
        player2.reset()
        player1.update()