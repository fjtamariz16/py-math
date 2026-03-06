import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

student = pd.read_csv('grades.csv')

model1 = sm.OLS.from_formula('port3 ~ math1 + port1', data = student).fit()
model2 = sm.OLS.from_formula('port3 ~ math1 + port1 + address', data = student).fit()

#R-Squared
print(model1.rsquared)
print(model2.rsquared)

#R-Squared Adjusted
print(model1.rsquared_adj)
print(model2.rsquared_adj)

#F-Test
anova_results = anova_lm(model1, model2)
print(anova_results)

#Log-Likelihood
print(model1.llf)
print(model2.llf)

print(model1.aic)
print(model2.aic)

print(model1.bic)
print(model2.bic)
