import matplotlib.pyplot as plt
import numpy as np

def plot():
    x = np.arange(0,2*np.pi,0.1)   # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()

if __name__ == "__main__":
    plot()