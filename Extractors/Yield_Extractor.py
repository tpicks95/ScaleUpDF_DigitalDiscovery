# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:18:18 2024

@author: pxb20160
"""

import pandas as pd

#DATAFRAME PREP
sheet_name = "CS1 OPT TP"

df = pd.read_excel(r"I:\Science\SIPBS\cmac\Thomas Pickles\HPLC Dilutions CS1.xlsx", sheet_name = sheet_name)
df = pd.DataFrame(df)

conc_df = df["Conc (mg/mL)"]
i_conc = conc_df[3]
e_conc = conc_df.iloc[-1]
yield_conc = (i_conc - e_conc) / i_conc
print(yield_conc)
