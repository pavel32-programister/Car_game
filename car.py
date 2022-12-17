import pygame as pg
from random import randrange

class Car():
    def __init__(self, screen, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.width = 50
        self.height = 100
        self.speed = 0
        self.image = pg.Surface((50, 50))
        self.image.fill((255, 255, 255))
    
    def update(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


class Main_Car(Car, pg.sprite.Sprite):
    image = pg.image.load(f"images\car1.png")
    def __init__(self, screen, x, y, *groups):
        super().__init__(screen, *groups)
        self.image = Main_Car.image
        self.speed = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.speed
    
    def bumped(self):
        return self.rect.x > 650 or self.rect.x < 100

class Enemy(Car, pg.sprite.Sprite):
    images = [pg.image.load(f"images\car{i+1}.png") for i in range(1, 3)]
    def __init__(self, screen, speed, *groups):
        super().__init__(screen, *groups)
        self.speed = speed
        self.image = Enemy.images[randrange(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.x = randrange(100, 650)
        self.rect.y = 0

    def move(self):
        self.rect.y += self.speed
    
    def bumped(self):
        return self.rect.y >= 800
    
    def update(self):
        super().update()
        self.move()
        if self.bumped():
            self.kill()