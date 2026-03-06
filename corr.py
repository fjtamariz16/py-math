import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

grades = pd.read_csv('grades.csv')

corr_grid = grades.corr(numeric_only = True)

sns.heatmap(corr_grid, xticklabels = corr_grid.columns, yticklabels = corr_grid.columns, vmin = -1, center = 0, vmax = 1, cmap = 'PuOr', annot = True)
plt.show()
