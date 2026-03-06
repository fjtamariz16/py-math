import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

population = [40, 40, 42, 35, 40, 39, 37, 41, 37, 39, 39, 38, 42, 40, 36, 40, 41, 41, 41, 37, 38, 38, 38, 42, 39, 43, 39, 30, 37, 33, 33, 34, 33, 36, 36, 32, 33, 33, 34, 38, 37, 32, 32, 35, 34, 35, 31, 35, 38, 35, 22, 22, 24, 23, 27, 28, 24, 25, 25, 24, 26, 23, 23, 25, 27, 24, 30, 18, 18, 30, 40, 49, 38, 35, 42, 40]
pop_mean = round(np.mean(population), 3)

plt.hist(population, color = 'lightgray', edgecolor = 'black')
plt.axvline(pop_mean, color='red', linestyle='dashed')
plt.title(f"Population mean: {pop_mean}g")
plt.xlabel("Weight (g)")
plt.show()
plt.clf()

samp_size = 50
sample = np.random.choice(np.array(population), samp_size, replace = False)
samp_mean = round(np.mean(sample), 3)

plt.hist(sample, color = 'lightgray', edgecolor = 'black')
plt.axvline(samp_mean, color='red', linestyle='dashed')
plt.title(f"Sample mean: {samp_mean}g")
plt.xlabel("Weight (g)")
plt.show()
