import matplotlib.pyplot as plt
import numpy as np

def plot():
    x = np.arange(0,2*np.pi,0.1)   # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,label="Sin")
    plt.plot(x,z,label="Cos")
    
    t=np.tan(x)
    max_index=t.argmax()
    min_idex=t.argmin()
    x[max_index]=np.nan
    x[min_idex]=np.nan
    plt.plot(x,t,label="Tan")
    
    plt.legend()
    plt.axhline(y=0.0, color='black')
    plt.ylim(-1.5,1.5)
    plt.show()

if __name__ == "__main__":
    plot()
