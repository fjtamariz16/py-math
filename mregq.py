import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

student = pd.read_csv('grades.csv')

model = sm.OLS.from_formula('port3 ~ math1 + port1', data = student).fit()
print(model.params)

sns.lmplot(x = 'math1', y = 'port3', hue = 'port1', palette = 'Greys', fit_reg = False, data = student)

score4 = plt.plot(student.math1, model.params[0] + model.params[1] * student.math1 + model.params[2] * 4, color = 'lightgrey', linewidth = 2)
score6 = plt.plot(student.math1, model.params[0] + model.params[1] * student.math1 + model.params[2] * 6, color = 'darkgrey', linewidth = 2)
score8 = plt.plot(student.math1, model.params[0] + model.params[1] * student.math1 + model.params[2] * 8, color = 'grey', linewidth = 2)

legend = plt.legend(['score = 4', 'score = 6', 'score = 8'])

handles = legend.legendHandles
colors = ['lightgrey', 'darkgrey', 'grey']
for i, handle in enumerate(handles):
    handle.set_facecolor(colors[i])

plt.show()
