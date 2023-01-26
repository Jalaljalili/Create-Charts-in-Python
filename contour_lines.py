import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create another contour plot

plt.contour(X, Y, Z, levels= 10, cmap='RdYlBu')
plt.colorbar()

#show the plot
plt.show()  