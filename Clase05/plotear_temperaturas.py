def plotear_temperaturas():
    import numpy as np
    temperaturas=np.load('Data/temperaturas.npy')
    import matplotlib.pyplot as plt
    plt.hist(temperaturas,bins=50)
    plt.show()

plotear_temperaturas()