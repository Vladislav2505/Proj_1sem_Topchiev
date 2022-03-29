from math import pi

_default_radius = 5


def circle_perimeter(rad=_default_radius):
    return 2 * pi * rad


def circle_area(rad=_default_radius):
    return pi * rad ** 2