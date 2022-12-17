from random import randrange
import pygame as pg
from time import sleep
from car import Main_Car, Enemy

GRAY=(200, 200, 200)
BLACK=(0, 0, 0)
GREEN=(0, 255, 0)
FPS = 60

def message_display(text, display, x=400, y=300):
    large_text = pg.font.Font("freesansbold.ttf", 80)
    text_surface = large_text.render(text, True, BLACK)
    text_surf, text_rect = text_surface, text_surface.get_rect()
    text_rect.center = (x, y)
    display.blit(text_surf, text_rect)
    pg.display.update()

def main():
    pg.init()
    display = pg.display.set_mode((800, 800))
    pg.display.set_caption("Гонщик легальный")
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()
    main_car = Main_Car(display, 400, 700)
    all_sprites.add(main_car)
    enemy_cnt = 0
    score = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    main_car.speed -= max(score // 500, 2)
                if event.key == pg.K_RIGHT:
                    main_car.speed += max(score // 500, 2)
        clock.tick(FPS)
        main_car.move()
        enemy_cnt = len(enemy_sprites)

        while enemy_cnt < max(score // 750, 2):
            enemy = Enemy(display, randrange(1, max(score // 500, 2)))
            enemy_sprites.add(enemy)
            all_sprites.add(enemy)
            enemy_cnt += 1

        display.fill(GREEN)
        pg.draw.rect(display, GRAY, (100, 0, 600, 800))
        all_sprites.update()
        message_display('Счёт = ' + str(score) + "км", display, 400, 100)
        if (main_car.bumped()) or (pg.sprite.spritecollide(main_car, enemy_sprites, False)):
            message_display("GAME OVER", display)
            sleep(2)
            main()

        pg.display.update()
        score += 1

if __name__ == '__main__':
    main()
    pg.quit()
    quit()