# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:52:31 2024

@author: pxb20160
"""
#IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import os

#SET THE EXPERIMENT NAME
eLN = "PICKL-46"

#PREPARING DATAFRAME
base_path = "H:\Documents\POSTDOC\LAB\CASE STUDY 1"
file_name = eLN+".xlsx"
file_path = os.path.join(base_path, file_name) 
df = pd.read_excel(file_path)
df = pd.DataFrame(df)
df = df[(df["phase_idx"]==8)]

#LINEAR REGRESSION FOR Blaze-LW-counts-5-120
x = df[["Time in minutes"]].to_numpy().ravel()
y = df[["Blaze-LW-counts-5-120"]].to_numpy().ravel()
res = stats.linregress((x, y))
print("Nucleation rate parameters for LW Counts 5-120 um:")
print(f"Nucleation rate (in #/s): {res.slope/60:.6f}")
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
plt.ylabel("Blaze-LW-counts-5-120", fontsize=12)
plt.xlabel("Time in minutes", fontsize=12)
plt.legend()
plt.show()
res5120 = res.slope/60

#LINEAR REGRESSION FOR Blaze-LW-counts-140-280
x = df[["Time in minutes"]].to_numpy().ravel()
y = df[["Blaze-LW-counts-140-280"]].to_numpy().ravel()
res = stats.linregress((x, y))
print("Nucleation rate parameters for LW Counts 140-280 um:")
print(f"Nucleation rate (in #/s): {res.slope/60:.6f}")
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
plt.ylabel("Blaze-LW-counts-140-280", fontsize=12)
plt.xlabel("Time in minutes", fontsize=12)
plt.legend()
plt.show()
res140280 = res.slope/60

#LINEAR REGRESSION FOR Blaze-LW-counts-300-880
x = df[["Time in minutes"]].to_numpy().ravel()
y = df[["Blaze-LW-counts-300-880"]].to_numpy().ravel()
res = stats.linregress((x, y))
print("Nucleation rate parameters for LW Counts 300-880 um:")
print(f"Nucleation rate (in #/s): {res.slope/60:.6f}")
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
plt.ylabel("Blaze-LW-counts-300-880", fontsize=12)
plt.xlabel("Time in minutes", fontsize=12)
plt.legend()
plt.show()
res300880 = res.slope/60

#MEAN NUCLEATION RATE CALCULATION
nuc = np.array([res5120,res140280,res300880])
nuc = nuc[nuc > 0]
nucAVG = np.average(nuc)
print("Nucleation rate (in #/s): ", nucAVG)
