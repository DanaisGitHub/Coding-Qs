You are given a list of 2D points representing the coordinates of several points on a 2D plane. 
Write a function find_min_area_rectangle(points) that finds the minimum area rectangle formed by any four points from the given list. 
The function should return the minimum area of the rectangle.

The find_min_area_rectangle(points) function should take the following input:

points: A list of tuples representing the coordinates of points on the 2D plane. Each tuple contains two integers (x, y).
The function should return a single float representing the minimum area of the rectangle formed by any four points. If no rectangle can be formed, return 0. 
You can assume that the input list will contain at least four points.

You may use any standard library functions or import additional modules if needed.

Example:

points = [(1, 1), (1, 3), (3, 1), (3, 3), (2, 2), (4, 1)]

min_area = find_min_area_rectangle(points)
print(min_area)  # Output: 4.0

In the given example, the points (1, 1), (1, 3), (3, 1), (3, 3) form a rectangle with a minimum area of 4.0.

Write your function in X Language.P