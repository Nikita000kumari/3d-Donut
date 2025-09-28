import pygame as pg
import numpy as np
from math import sin, cos, pi

# Setup
pg.init()
WIDTH, HEIGHT = 800, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("3D Donut")
clock = pg.time.Clock()

# Donut points
R1, R2 = 70, 140
xyz = []
for theta in np.arange(0, 2*pi, 0.4):
    for phi in np.arange(0, 2*pi, 0.15):
        x = (R2 + R1*cos(theta)) * cos(phi)
        y = R1 * sin(theta)
        z = (R2 + R1*cos(theta)) * sin(phi)
        xyz.append([x, y, z, 1])  # homogeneous coords

nodes = np.array(xyz)

# Rotation matrices
def rot_x(a):
    c, s = cos(a), sin(a)
    return np.array([[1,0,0,0],
                     [0,c,-s,0],
                     [0,s,c,0],
                     [0,0,0,1]])

def rot_y(a):
    c, s = cos(a), sin(a)
    return np.array([[c,0,s,0],
                     [0,1,0,0],
                     [-s,0,c,0],
                     [0,0,0,1]])

def rot_z(a):
    c, s = cos(a), sin(a)
    return np.array([[c,-s,0,0],
                     [s,c,0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

# Main loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    screen.fill((0,0,0))  # clear screen

    # Rotate donut
    nodes = nodes @ rot_x(0.03).T @ rot_y(0.02).T @ rot_z(0.01).T

    # Draw donut points
    for n in nodes:
        x, y, z, _ = n
        pg.draw.circle(screen, (255,20,147), 
                       (WIDTH//2 + int(x), HEIGHT//2 + int(z)), 2)

    pg.display.update()

pg.quit()
