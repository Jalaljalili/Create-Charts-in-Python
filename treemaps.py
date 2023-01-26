import squarify
import matplotlib.pyplot as plt

# Sample data
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}


# Create the treemap

squarify.plot(sizes=data.values(), label=data.keys(),
              color=["red","green","blue","yellow"],alpha=.4)
plt.axis('off')
#show the plot
plt.show()  