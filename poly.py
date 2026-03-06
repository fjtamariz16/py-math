import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

bluegills = pd.read_csv('bluegills.csv')

simple = sm.OLS.from_formula('length ~ age', data = bluegills).fit()
polynomial = sm.OLS.from_formula('length ~ age + np.power(age,2)', data = bluegills).fit()

print(simple.params)
print(polynomial.params)

sns.lmplot(x='age', y='length', ci=None, data=bluegills)

x = np.linspace(1,6,100)
y = polynomial.params[0] + polynomial.params[1] * x + polynomial.params[2] * np.power(x,2)
plt.plot(x, y, linestyle = 'dashed', linewidth = 2, color = 'black')

plt.show()
