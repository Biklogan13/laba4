import pygame
from pygame.draw import *

def back1(sur:pygame.Surface):
    rect(sur, (143, 198, 246), (0, 0, 1000, 500))
    rect(sur, (103, 217, 108), (0, 500, 1000, 500))


def back2(sur:pygame.Surface):
    rect(sur, (100, 100, 100), (0, 0, 1000, 1000))


def drawman(sur:pygame.Surface, x:int):
    ellipse(sur, (185, 155, 191), (x + 220, 350, 150, 300))
    circle(sur, (231, 208, 185), (x + 295, 320), 50)
    lines(sur, (0, 0, 0), False, ((x + 335, 620), (x + 370, 820), (x + 420, 820)), width=2)
    lines(sur, (0, 0, 0), False, ((x + 255, 620), (x + 150, 820), (x + 100, 820)), width=2)
    line(sur, (0, 0, 0), (x + 250, 380), (x + 150, 480), width=2)
    line(sur, (0, 0, 0), (x + 340, 380), (x + 470, 480), width=2)
    polygon(sur, (227, 201, 67), ((x + 160, 480), (x + 110, 460), (x + 165, 420)))
    circle(sur, (255, 0, 0), (x + 145, 425), 18)
    circle(sur, (95, 0, 0), (x + 120, 445), 18)
    circle(sur, (255, 255, 255), (x + 120, 420), 18)


def drawwoman(sur:pygame.Surface, x:int):
    polygon(sur, (255, 95, 177), ((x + 620, 350), (x + 540, 650), (x + 700, 650)))
    circle(sur, (231, 208, 185), (x + 620, 320), 50)
    lines(sur, (0, 0, 0), False, ((x + 600, 650), (x + 550, 820), (x + 500, 825)), width=2)
    lines(sur, (0, 0, 0), False, ((x + 640, 650), (x + 690, 820), (x + 740, 820)), width=2)
    line(sur, (0, 0, 0), (x + 605, 410), (x + 470, 480), width=2)
    lines(sur, (0, 0, 0), False, ((x + 635, 410), (x + 680, 455), (x + 740, 440)), width=2)
    line(sur, (0, 0, 0), (x + 720, 490), (x + 800, 300), width=2)
    polygon(sur, (255, 0, 0), ((x + 800, 300), (x + 850, 250), (x + 790, 230)))
    circle(sur, (255, 0, 0), (x + 835, 240), 18)
    circle(sur, (255, 0, 0), (x + 807, 230), 18)


def drawsmile(sur:pygame.Surface):
    circle(sur, (0, 0, 0), (500, 500), 252)
    circle(sur, (230, 230, 0), (500, 500), 250)
    circle(sur, (0, 0, 0), (400, 430), 55)
    circle(sur, (255, 0, 0), (400, 430), 53)
    circle(sur, (0, 0, 0), (400, 430), 25)
    circle(sur, (0, 0, 0), (600, 430), 40)
    circle(sur, (255, 0, 0), (600, 430), 38)
    circle(sur, (0, 0, 0), (600, 430), 20)
    rect(sur, (0, 0, 0), (350, 600, 300, 50))
    polygon(sur, (0, 0, 0), ((548, 400-23.333+2), (555, 400+2), (760, 340+2), (753, 340-23.333+2)))
    polygon(sur, (0, 0, 0), ((477, 388-3), (466, 410-3), (246, 300-3), (257, 278-3)))


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

print("Введите p для отрисовки пары, s для отрисовки смайлика")

a = input()
if a == 'p':
    back1(screen)
    drawman(screen, 400)
    drawwoman(screen, -350)
elif a == 's':
    back2(screen)
    drawsmile(screen)

pygame.display.update()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
