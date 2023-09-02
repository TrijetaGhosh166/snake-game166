import pygame
from pygame.locals import *
import time
import random
#initilize
pygame.init()
#display
white = (255, 255, 255)
red=(255, 0, 0)
blue = (0, 25, 51)
green = (102, 204, 0)
yellow = (255, 255, 0)

win_width = 800
win_height = 600
#window display
window = pygame.display.set_mode((win_width, win_height))
#caption
pygame.display.set_caption("snake Game")
time.sleep(2)

snake = 10
snake_speed = 10
clock = pygame.time.Clock()
#font style and size
font_style = pygame.font.SysFont("corbel", 26)
score_font = pygame.font.SysFont("impact", 30)


def user_score(score):
    # store score value ,visibility true with color
    number = score_font.render("score: " + str(score), True, white)
    #display pos and data
    window.blit(number, [0, 0])


def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])


def message(msg):
    #msg font
    mesg = font_style.render(msg, True, red)
    #display cordinate
    window.blit(mesg, [win_width / 6, win_height / 3])


def game_loop():
    game_over = False
    game_close = False
# pos of x1 and y1 (snake pos)
    x1 = win_width / 2
    y1 = win_height / 2
#snake length
    x1_change = 0
    y1_change = 0
#snake length list
    snake_length_list = []
    snake_length = 1
#snake food value
    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not game_over:
        while game_close:
            window.fill(blue)
            message("lost !! press A to play again, Q to quit")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake
            #overgame        

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, yellow, [foodx, foody, snake, snake])
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        for x in snake_length_list[:-1]:
            if x == snake_size:
                game_close = True

        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
