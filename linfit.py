import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

test_data = {'ex1': [15, 23, 25, 30, 34, 34, 40], 'ex2':[20, 26, 27, 32, 35, 37, 35]}

results = pd.DataFrame(test_data)

model = sm.OLS.from_formula('ex2 ~ ex1', data = results).fit()
print(model.params)
print(model.rsquared)

# Prediction 1: Exam 1 with 19 points
print(model.params[1] * 19 + model.params[0])

# Prediction 2: Exam 1 with 37 points
newdata = {'ex1': 37}
print(model.predict(newdata))

x = test_data['ex1']
y = test_data['ex2']

xval = np.arange(np.min(x), np.max(x), 1)
reg = model.params[1] * xval + model.params[0]

plt.scatter(x, y)
plt.plot(xval, reg)
plt.xlabel('Exam 1')
plt.ylabel('Exam 2')
plt.xlim(0)
plt.ylim(0)
plt.show()
plt.clf()

fitted_values = model.predict(test_data)
print(fitted_values.head())

residuals = y - fitted_values
print(residuals.head())

plt.hist(residuals)
plt.show()
plt.clf()

plt.scatter(fitted_values, residuals)
plt.axhline(0, color = 'black', linestyle = 'dashed')
plt.show()
plt.clf()
