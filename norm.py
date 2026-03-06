import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

x = 158
mean = 167.64
stdv = 8
prob = stats.norm.cdf(x, mean, stdv)
print(prob)

int = np.linspace(mean - stdv * 3, mean + stdv *3)
y = stats.norm.pdf(int, mean, stdv)

plt.plot(int, y)
plt.show()
