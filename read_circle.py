#!/usr/bin/env python

from PIL import Image


def debug(x, y, color=None):
    nim = Image.open('debug.png')
    npix = im.load()
    if color == None: color = (255, 0, 0)
    npix[x, y] = color
    nim.save('debug.png', 'png')

def spiral(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            yield (x, y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

def spiral_search(pix, cx, cy, width, height, color):
    x = (cx, cy)
    for dt in spiral(width-1, height-1):
        dx = cx + dt[0]
        dy = cy + dt[1]

        debug(dx, dy, (0, 0, 255))
        if x != pix[dx, dy]:
            x = pix[dx, dy]
            print x
        if pix[dx, dy] == color:
            return (dx, dy)

def spiral_edge(pix, cx, cy, width, height):
    color = pix[cx, cy]
    for dt in spiral(width-1, height-1):
        dx = cx + dt[0]
        dy = cy + dt[1]

        debug(dx, dy)
        if pix[dx, dy] != color:
            return (dx, dy)
    

im = Image.open('circle.png')
pix = im.load()
center = (im.size[0] / 2, im.size[1] / 2)

print spiral_edge(pix, center[0], center[1], im.size[0], im.size[1])

print spiral_search(pix, center[0], center[1], im.size[0], im.size[1], (0xc0, 0xc0, 0xc0))
