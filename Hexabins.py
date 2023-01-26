import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)


# Create the hexabin plot

plt.hexbin(x, y, gridsize=50, cmap='Reds')
plt.colorbar()
#show the plot
plt.show()  