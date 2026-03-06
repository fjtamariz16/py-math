import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

population = [7, 7, 7, 8, 8, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 15, 16, 16, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 31, 31, 32, 32, 32, 33, 33, 34,34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 38, 38, 39, 39, 39, 39, 40, 40, 40, 40, 40, 41, 41, 41, 41, 43, 43, 46, 48, 48, 48, 49, 49, 51, 52, 52, 52, 56, 58, 58, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 64, 68, 69, 70, 71, 72, 75, 79, 80, 81, 84, 86, 89, 94, 97, 101, 108, 115, 120, 126, 134, 140]
pop_mean = np.mean(population)

plt.hist(population, color = 'lightgray', edgecolor = 'black')
plt.axvline(pop_mean, color='red', linestyle='dashed')
plt.title(f"Population mean: {pop_mean}lbs")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf()

sample_means = []

samp_size = 30
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

mean = np.mean(sample_means)
stdv = (np.var(sample_means)) ** 0.5
print(mean)
print(stdv)

sns.histplot(sample_means, stat = 'density', color = 'lightgray', edgecolor = 'black')
plt.axvline(mean, color='red', linestyle='dashed')
plt.title(f"Sampling distribution")
plt.xlabel("Weight (lbs)")
plt.ylabel("Density")
int = np.linspace(mean - stdv * 3, mean + stdv *3)
plt.plot(int, stats.norm.pdf(int, mean, stdv))
plt.show()
