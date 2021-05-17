import numpy as np
import math
n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

xo, yo = (x0+xn2)/2, (y0+yn2)/2
theta = 2*math.pi/n
A = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
b = np.array([x0-xo, y0-yo]).T

new = np.dot(A, b)
print(new[0]+xo, new[1]+yo)