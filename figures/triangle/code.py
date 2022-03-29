from math import sqrt

_a = 7
_b = 2
_c = 8


def triangle_perimeter(q=_a, w=_b, e=_c):
    return q + w + e


def triangle_area(q=_a, w=_b, e=_c):
    per = (q + w + e)
    return sqrt(per * (per - q) * (per - w) * (per - e))
