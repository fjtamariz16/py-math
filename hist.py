import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

rand_var = stats.poisson.rvs(10, size = 500)
print(rand_var.mean())

plt.hist(rand_var, bins = np.arange(len(set(rand_var))), color = 'lightgray', edgecolor = 'black')
plt.xticks(list(range(rand_var.max())))
plt.show()
