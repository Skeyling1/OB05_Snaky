import pygame
import random


pygame.init()

WIDTH = 800
HIGHT = 600
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
        if self.segment_number == 0:
            screen.blit(self.body, (x, y))
        else:
            f = coordinate[0 - 25]
            if moving == 'RIGHT':
                screen.blit(self.body, (f[0], y))
            elif moving == 'LEFT':
                screen.blit(self.body, (f[0], y))
            elif moving == 'UP':
                screen.blit(self.body, (x, f[1]))
            elif moving == 'DOWN':
                screen.blit(self.body, (x, f[1]))


class Food:
    def __init__(self, start_position):
        self.start_position = start_position
        self.body = pygame.Surface((20, 20))
        self.body.fill((186, 0, 0))
        self.rect = self.body.get_rect()
    def appearing(self):

        screen.blit(self.body, (300, 300))



#создаем объект персонажа
head = BodyXsegment(0, (x, y))
body1 = BodyXsegment(1, (x, y))

#создаем объект еды
food = Food((300, 300))

coordinate = []
for i in range(25):
    coordinate.insert(0, (i, i))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((55, 55, 55))
    moving = 'RIGHT'

    head.moving()
    body1.moving()
    food.appearing()

    coordinate.insert(0, (x, y))


    keys = pygame.key.get_pressed()

    x += direction_x
    y += direction_y

    if keys[pygame.K_RIGHT]:
        direction_x = 1
        direction_y = 0
        moving = 'RIGHT'

    elif keys[pygame.K_LEFT]:
        direction_x = -1
        direction_y = 0
        moving = 'LEFT'

    elif keys[pygame.K_UP]:
        direction_x = 0
        direction_y = -1
        moving = 'UP'

    elif keys[pygame.K_DOWN]:
        direction_x = 0
        direction_y = 1
        moving = 'DOWN'

#проверка столкновения с стенками


#проверка столкновения с едой



    #print(coordinate)
    pygame.time.delay(10)
    pygame.display.flip()

pygame.quit()