# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:47:22 2024

@author: pxb20160
"""

#IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#PREPARING DATAFRAME
df = pd.read_excel(r"H:\Documents\POSTDOC\LAB\CASE STUDY 2\AO-5.xlsx")
df = pd.DataFrame(df)

df = df[(df["Blaze-HDR-TU"]>0.001) & (df["phase_idx"]==2) & (df["Time in minutes"]>200)]

#LINEAR REGRESSION FOR Blaze-SW-mean-1-880
x = df[["Time in minutes"]].to_numpy().ravel()
y = df[["Blaze-SW-mean-1-880"]].to_numpy().ravel()
res = stats.linregress((x, y))
print("Growth rate parameters for mean SW-mean-1-880:")
print(f"Growth rate in um/min: {res.slope:.6f}")
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
plt.ylabel("Blaze-SW-mean-1-880", fontsize=12)
plt.xlabel("Time in minutes", fontsize=12)
plt.legend()
plt.show()

#LINEAR REGRESSION FOR Blaze-CW-90percentile-1-900
x = df[["Time in minutes"]].to_numpy().ravel()
y = df[["Blaze-CW-90percentile-1-900"]].to_numpy().ravel()
res = stats.linregress((x, y))
print("Growth rate parameters for PSD D90:")
print(f"Growth rate in um/min: {res.slope:.6f}")
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
plt.ylabel("Blaze-CW-90percentile-1-900", fontsize=12)
plt.xlabel("Time in minutes", fontsize=12)
plt.legend()
plt.show()
