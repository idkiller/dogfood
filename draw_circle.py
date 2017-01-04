#!/usr/bin/env python

import math
import cairo

# gold = 0xffd700
# silver = c0c0c0

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)

ctx.scale (WIDTH, HEIGHT) # Normalizing the canvas

ctx.rectangle(0, 0, 1, 1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill()

#ctx.translate (0.1, 0.1) # Changing the current transformation matrix
#ctx.move_to(0, 0)

ctx.arc(0.5, 0.5, 5.0/256, 0, 2 * math.pi)
ctx.set_source_rgb(1, 215 / 255.0, 0)
ctx.fill()

ctx.arc(0.5, 0.5, 100.0/256, 0, 2 * math.pi)
ctx.set_line_width(0.02)
ctx.set_source_rgb(0.75, 0.75, 0.75)
ctx.stroke()

ctx.arc(0.5, 0.5, 100.0/256, 0, 0)
cx, cy = ctx.get_current_point()
ctx.arc(cx, cy, 5.0/256, 0, 2* math.pi)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

surface.write_to_png ("circle.png") # Output to PNG
