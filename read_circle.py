#!/usr/bin/env python

import math
import cairo

surface = cairo.ImageSurface.create_from_png('circle.png')

from pprint import pprint

data = surface.get_data()

pprint(data)
