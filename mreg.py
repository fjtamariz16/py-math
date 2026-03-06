import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

student = pd.read_csv('grades.csv')

print(pd.DataFrame(student))

model = sm.OLS.from_formula('port3 ~ math1 + address', data=student).fit()
print(model.params)

b0 = model.params[0]
b1 = model.params[2]
b2 = model.params[1]

interceptR = b0
interceptU = b0 + b2
slope = b1

sns.lmplot(x='math1', y='port3', hue='address', markers=['o', 'x'], ci = None, data=student)
#plt.plot(student.math1, interceptR + slope * student.math1)
#plt.plot(student.math1, interceptU + slope * student.math1)
plt.show()
