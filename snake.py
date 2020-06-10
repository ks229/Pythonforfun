import pygame as pg
import time
import random

pg.init()

red = pg.Color(255,0,0)
white = pg.Color(255,255,255)
black = pg.Color(0,0,0)
blue = pg.Color(0,0,225)

screen_width = 400
screen_height = 400

window = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('Fast mouse')
pg.display.update()

counter  = 0
#SNAKE PARAMETERS
snake_x = screen_width/4
snake_y = screen_height/4
snake_w = 10
snake_h = 10

x_change = 0
y_change = 0

font_style = pg.font.SysFont(None, 30)
score_font = pg.font.SysFont("comicsans",30)

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    window.blit(mesg,[screen_width/8,screen_height/8])

clock = pg.time.Clock()
snake_speed = 10

snake_list = []

def snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(window,red,[x[0],x[1],snake_block,snake_block])


food_x = round(random.randrange(0,screen_width - snake_w)/10)*10
food_y = round(random.randrange(0,screen_height - snake_h)/10)*10
food_h = 10
food_w = 10

def score(score):
    value = score_font.render("Your Score :" + str(score),True,white)
    window.blit(value,[10, 10])


game = True
while game:
    score(counter)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type ==pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change = -10
                y_change = 0
            if event.key == pg.K_RIGHT:
                x_change = 10
                y_change = 0
            if event.key == pg.K_DOWN:
                x_change = 0
                y_change = 10
            if event.key == pg.K_UP:
                x_change = 0
                y_change = -10
    snake_x += x_change
    snake_y += y_change
    if snake_x >= screen_width or snake_x < 0:
        game = False
    if snake_y >= screen_height or snake_y < 0:
        game = False
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0,screen_width - snake_h)/10)*10
        food_y = round(random.randrange(0,screen_height - snake_w -30)/10)*10
        counter += 1
        snake_speed += 1

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > counter+1:
        del snake_list[0]
    for x in snake_list[:-1]:
            if x == snake_head:
                game = False

    window.fill(black)
    score(counter)
    snake(10,snake_list)
    pg.draw.rect(window,white,[food_x,food_y,food_h,food_w])
    pg.display.update()
    clock.tick(snake_speed)
window.fill(black)
message('YOU lOST.Your score : ' + str(counter),white)
pg.display.update()
time.sleep(2)
pg.quit()
quit()
