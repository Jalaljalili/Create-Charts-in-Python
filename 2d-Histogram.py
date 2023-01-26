import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
data = np.random.randn(1000,6)

# Create a 2D histogram

plt.hist2d(data[:,0], data[:,1], bins=25)

# Adding color bar
plt.colorbar()
#show the plot
plt.show()  