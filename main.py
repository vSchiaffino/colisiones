import pygame
from copy import deepcopy
from pygame.locals import *
from trigonometria import partir_mov, rotar_poligono
from hb import Hb
from pared import Pared


def eventos():
    global obstaculos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                teclas[0] = True
            if event.key == pygame.K_RIGHT:
                teclas[1] = True
            if event.key == pygame.K_DOWN:
                teclas[2] = True
            if event.key == pygame.K_LEFT:
                teclas[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                teclas[0] = False
            if event.key == pygame.K_RIGHT:
                teclas[1] = False
            if event.key == pygame.K_DOWN:
                teclas[2] = False
            if event.key == pygame.K_LEFT:
                teclas[3] = False
    hb = obstaculos[4]
    if teclas[0]:
        clock.tick()
        hb.mover(10, obstaculos)
        clock.tick()
        #print(clock.get_time())
    if teclas[1]:
        clock.tick()
        hb.rotar(10, obstaculos)
        clock.tick()
        #print(clock.get_time())
    if teclas[2]:
        clock.tick()
        hb.mover(-10, obstaculos)
        clock.tick()
        #print(clock.get_time())
    if teclas[3]:
        clock.tick()
        hb.rotar(-10, obstaculos)
        clock.tick()
        #print(clock.get_time())



pygame.init()

w = 800
h = 600

# creo un robot
alto1 = 10
alto2 = 5
alto = 60
ancho = 40
anchodiv = 10
puntos = [[0, 0],[anchodiv, -alto1],[anchodiv * 2, -alto1 - alto2],[anchodiv * 3, -alto1],[ancho, 0],[ancho, alto],[0, alto]]
# creo un robot x
hb = Hb(puntos)
# ta

# un obstaculo random
puntos = [
    [400, 400],
    [400, 500],
    [450, 550],
]
r = Hb(puntos)

obstaculos = [
    Pared(0, 0, w, 0),
    Pared(w, 0, w, h),
    Pared(w, h, 0, h),
    Pared(0, h, 0, 0),
    hb,
    r
]


teclas = [False, False, False, False]
clock = pygame.time.Clock()
if __name__ == "__main__":
    s = pygame.display.set_mode((w, h))

    while True:
        eventos()
        
        s.fill((0, 255, 0))
        pp = []
        for p in hb.puntos:
            pp.append((int(p[0]), int(p[1])))
        pygame.draw.polygon(s, (255, 0, 0), pp)
        mov = partir_mov(50, hb.ang)
        c1 = hb.get_center()
        c2 = [c1[0] + mov[0], c1[1] + mov[1]]
        pygame.draw.lines(s, (100, 0, 0), False, [c1, c2])
        # robots
        pygame.draw.polygon(s, (255, 255, 0), obstaculos[5].puntos)
        pygame.display.flip()
        pygame.time.wait(50)
