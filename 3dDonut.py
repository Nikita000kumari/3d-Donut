import pygame as pg
import numpy as np
from math import sin, cos, pi

WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
GREEN = (255, 20, 147)

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

class Object:
    def __init__(self):
        self.nodes = np.zeros((0, 4))

    def add_nodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        self.nodes = np.hstack((node_array, ones_column))

    def rotate(self, matrix):
        self.nodes = np.matmul(self.nodes, matrix.T)

# Rotation matrices
def rotation_matrix_x(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[1,0,0,0],
                     [0,c,-s,0],
                     [0,s,c,0],
                     [0,0,0,1]])

def rotation_matrix_y(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c,0,s,0],
                     [0,1,0,0],
                     [-s,0,c,0],
                     [0,0,0,1]])

def rotation_matrix_z(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c,-s,0,0],
                     [s,c,0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

# Build donut once
R1, R2 = 70, 140
xyz = []
for theta in np.arange(0, 2*pi, 0.4):
    for phi in np.arange(0, 2*pi, 0.15):
        x = (R2 + R1*cos(theta)) * cos(phi)
        y = R1 * sin(theta)
        z = (R2 + R1*cos(theta)) * sin(phi)
        xyz.append((x, y, z))

donut = Object()
donut.add_nodes(np.array(xyz))

# Main loop
running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BLACK)

    # Rotate the donut
    donut.rotate(rotation_matrix_x(0.03))
    donut.rotate(rotation_matrix_y(0.02))
    donut.rotate(rotation_matrix_z(0.01))

    # Draw points
    for node in donut.nodes:
        x, y, z, _ = node
        pg.draw.circle(screen, GREEN, (WIDTH//2 + int(x), HEIGHT//2 + int(z)), 2)

    pg.display.update()

pg.quit()
