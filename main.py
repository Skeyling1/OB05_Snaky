import pygame
pygame.init()

WIDTH = 800
HIGHT = 600
screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Snaky")

#начальные положения персонажа
x = 20
y = 20
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
        for number in range(self.segment_number):
            screen.blit(self.body, (x, y+number*2))



#создаем объект персонажа
head = BodyXsegment(10, (x, y))



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((55, 55, 55))

    head.moving()


    keys = pygame.key.get_pressed()

    x += direction_x
    y += direction_y

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


    pygame.time.delay(10)
    pygame.display.flip()

