import pygame
pygame.init()

WIDTH = 800
HIGHT = 600
screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Snaky")

#начальные положения персонажа
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
            screen.blit(self.body, (x, y))



#создаем объект персонажа
head = BodyXsegment(0, (x, y))
body1 = BodyXsegment(20, (x, y))

coordinate = {}

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((55, 55, 55))

    head.moving()
    body1.moving()


    keys = pygame.key.get_pressed()

    x += direction_x
    y += direction_y

    if keys[pygame.K_RIGHT]:
        direction_x = 1
        direction_y = 0
        coordinate = {"RIGHT" : (x, y)}

    elif keys[pygame.K_LEFT]:
        direction_x = -1
        direction_y = 0
        coordinate = {"LEFT" : (x, y)}

    elif keys[pygame.K_UP]:
        direction_x = 0
        direction_y = -1
        coordinate = {"UP" : (x, y)}

    elif keys[pygame.K_DOWN]:
        direction_x = 0
        direction_y = 1
        coordinate = {"DOWN" : (x, y)}

#проверка столкновения с стенками


#проверка столкновения с едой



    #print(coordinate)
    pygame.time.delay(10)
    pygame.display.flip()

