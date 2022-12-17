import pygame as pg
import time
import random


GRAY=(200, 200, 200)
BLACK=(0, 0, 0)
GREEN=(0, 255, 0)

pg.init()
display = pg.display.set_mode((800, 800))
pg.display.set_caption("Гонщик легальный")

car_img = pg.image.load("images\car1.png")
car_width = 50

def policecar(police_startx, police_starty, police):
    if police == 0:
        police_come = pg.image.load("images\car2.png") 
    if police == 1: 
        police_come = pg.image.load("images\car3.png")
    if police == 2:
        police_come = pg.image.load("images\car1.png") 
    display.blit(police_come, (police_startx, police_starty))

def crash():
    message_display("Game Over")

def text_object(text, font):
    text_surface=font.render(text, True, BLACK)
    return text_surface,text_surface.get_rect()

def message_display(text):
    large_text = pg.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_object(text, large_text)
    textrect. center = ((400), (300))
    display.blit(textsurf,textrect)
    pg.display.update()
    time.sleep(3)
    loop()

def car(x, y):
    display.blit(car_img, (x, y))

def loop():
    x = 400
    y = 540
    x_change = 0 
    y_change = 0
    policecar_speed = 9
    police = 0
    police_start_x = random.randrange(100, (700-car_width))
    police_start_y = -600
    police_width = 50
    police_height = 100
    bumped = False
    while not bumped:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -1
                if event.key == pg.K_RIGHT:
                    x_change = 1
            if event.type == pg.KEYUP:
                x_change=0
        x += x_change

        display.fill(GREEN)
        pg.draw.rect(display, GRAY, (100, 0, 600, 800))

        police_start_y -= (policecar_speed / 1.2)
        policecar(police_start_x, police_start_y, police)
        police_start_y += policecar_speed
        car(x, y)
        if x < 100 or x > 700-car_width:
            crash()

        if police_start_y > 600:     
            police_start_y = 0 - police_height 
            police_start_x = random.randrange(130, 700)
            police = random.randrange(0,2)

        if y < police_start_y + police_height:
            if x > police_start_x and x < police_start_x + police_width \
                or x + car_width > police_start_x and x + car_width < police_start_x + police_width:
                crash()

        pg.display.update()
loop()
pg.quit() 
quit()