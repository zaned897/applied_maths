"""In this code we will explore a function $f(x,y) = xsin(y) + ycos(x)$"""
from numpy import cos, sin, pi, linspace, meshgrid
from matplotlib import pyplot as plt

x = linspace(
	start=-2*pi,
	stop=2*pi,
	num=200
)
y = x
x, y = meshgrid