import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

student = pd.read_csv('grades.csv')

model = sm.OLS.from_formula('port3 ~ math1 + address + math1:address', data = student).fit()
print(model.params)
