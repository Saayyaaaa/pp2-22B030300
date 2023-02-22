import math

num_sides = int(input())
side_length = int(input())

def polygon_area(n_sides, length):
    area = (n_sides * (length ** 2)) / (4 * math.tan((math.pi) / n_sides))
    print(int(area))

polygon_area(num_sides, side_length)