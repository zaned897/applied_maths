"""In this code we will explore some functions composed of multiple variables"""
#%%
import numpy as np
from matplotlib import pyplot as plt


# a function of multiple variables has the form f(x,y,z,...) or f(x1,x2,x3,...)
# lets start building the space x, y 
x = np.linspace(
    start=-2*np.pi,
    stop=2*np.pi,
    num=100
)
y = x 
x, y = np.meshgrid(x, y)

# now lets evaluate the function in the space f(x,y) = x**2 + y**2
z = x**2 + y**2

#%% results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('$f(x_1,x_2)=x_1^2 + x_2^2$')

