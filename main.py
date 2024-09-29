import pygame
import random


pygame.init()

WIDTH = 600
HIGHT = 400
screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Snaky")

#начальные положения змеи
x = 200
y = 200
direction_x = 0
direction_y = 0


class BodyXsegment:
    def __init__(self, segment_number, start_position):
        self.segment_number = segment_number
        self.start_position = start_position
        self.body = pygame.Surface((20, 20))
        self.body.fill((255, 255, 255))
        self.rect = self.body.get_rect()

    def moving(self):
        f = coordinate[self.segment_number * 30]  # координата с отстованием, кратным номеру сегмента
        self.rect = self.body.get_rect(topleft=(f[0], f[1]))
        screen.blit(self.body, self.rect)


class Food:
    def __init__(self, start_position):
        self.start_position = start_position
        self.body = pygame.Surface((20, 20))
        self.body.fill((186, 0, 0))
        self.rect = self.body.get_rect()

    def appearing(self, x_food, y_food):
        self.rect = self.body.get_rect(topleft=(x_food, y_food))
        screen.blit(self.body, self.rect)


#создаем начальные сегменты персонажа
snake = []
for n in range(3):
    segment = BodyXsegment(n, (x, y))
    snake.append(segment)

#задаем начальные координаты сегментов
coordinate = []
for i in range(100):
    coordinate.insert(0, (x, y))

#создаем объект еды
x_food = random.randint(0, WIDTH-20)
y_food = random.randint(0, HIGHT-20)
food = Food((x_food, y_food))

def collidefood():
    if snake[0].rect.colliderect(food.rect):
        global y_food
        global x_food
        x_food = random.randint(0, WIDTH-20)
        y_food = random.randint(0, HIGHT-20)
        segment = BodyXsegment(len(snake), (x, y))
        snake.append(segment)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((55, 55, 55))

    for segment in snake:
        segment.moving()

    food.appearing(x_food, y_food)
    collidefood()

    coordinate.insert(0, (x, y))

    x += direction_x
    y += direction_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        direction_x = 1
        direction_y = 0

    elif keys[pygame.K_LEFT]:
        direction_x = -1
        direction_y = 0

    elif keys[pygame.K_UP]:
        direction_x = 0
        direction_y = -1

    elif keys[pygame.K_DOWN]:
        direction_x = 0
        direction_y = 1
 
    #проверка столкновения с стенками
    if x > WIDTH or x < 0 or y > HIGHT or y < 0:
        run = False

    # проверка столкновения с телом
    if len(snake) > 3:
        for segment in snake:
            if segment == snake[0]:
                continue
            elif segment.rect.collidepoint(snake[0].rect.center):
                run = False




    pygame.time.delay(5)
    pygame.display.flip()

pygame.quit()