#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides = [a, b, c]
    if any(
        item <= 0
        for item in sides
    ):
        raise TriangleError()
    x1 = min(sides)
    sides.remove(x1)
    x2 = min(sides)
    sides.remove(x2)
    if(x1+x2 <= sides[0]):
        raise TriangleError()
    if a == b == c:
        return 'equilateral'
    elif a == b or a == c or b == c:
        return 'isosceles'
    else:
        return 'scalene'
    

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
