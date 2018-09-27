import numpy as np
from b_wire import b_wire
import matplotlib.pyplot as plt
def secret_plot_function(func, x, y, step):
    X, Y = np.mgrid[min(x):max(x):step, min(y):max(y):step]
    U = b_wire(X,Y)
    M = np.sqrt(U[0]**2+U[1]**2) # magnitude
    plt.figure(figsize = (10,10))
    plt.quiver(X, Y, U[0]/M, U[1]/M,M,cmap=plt.cm.plasma)
    plt.colorbar()
    plt.show()