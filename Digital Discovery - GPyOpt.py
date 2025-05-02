#MODULES
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import time
import GPyOpt
from GPyOpt.methods import BayesianOptimization
from numpy.random import seed

#DATAFRAME
df = pd.read_excel(r'<File Location>')
df = df.dropna()
FORMAT = ["Yield", "Growth rate (mean-1-880)", "R2 Growth rate (mean-1-880)", "Nucleation rate (LW-counts-5-120)", "R2 Nucleation rate (LW-counts-5-120)"]
df2 = df[FORMAT]
normalized_df2=(df2-df2.min())/(df2.max()-df2.min())
normalized_df2.insert(5, "Objective Function", normalized_df2["Yield"]+normalized_df2["Growth rate (mean-1-880)"]+normalized_df2["R2 Growth rate (mean-1-880)"]-normalized_df2["Nucleation rate (LW-counts-5-120)"]+normalized_df2["R2 Nucleation rate (LW-counts-5-120)"])
#Creating initial value variables from df
obj = normalized_df2[["Objective Function"]].to_numpy()
var = df[["Cooling Rate (°C/min)","Seed Mass (%)", "SS"]].to_numpy()

#Design Space Plot
xdata = df["Cooling Rate (°C/min)"]
ydata = df["Seed Mass (%)"]
zdata = df["SS"]
ax = plt.axes(111, projection='3d')
ax.scatter3D(xdata, ydata, zdata)
ax.set_xlabel('Cooling rate (°C)')
ax.set_ylabel('Seed mass (%)')
ax.set_zlabel('SS')
plt.show()

#BAYESIAN
start_time = time.time()
seed(123)
def f(x):
    return x

bounds = [{'name': 'Cooling Rate (°C/min)', 'type': 'continuous', 'domain': (0.1, 0.5)},
          {'name': 'Seed Mass (%)', 'type': 'continuous', 'domain': (1, 5)},
          {'name': 'SS', 'type': 'continuous', 'domain': (1.2, 1.5)}]

bo_step = GPyOpt.methods.BayesianOptimization(f = f,
                                              domain=bounds,
                                              model_type='GP',
                                              acquisition_type ='EI',
                                              acquisition_jitter = 0.1,
                                              maximize = True,
                                              X=var,
                                              Y=obj)

x_next = bo_step.suggest_next_locations()
print("--- %s seconds ---" % (time.time() - start_time))


print("The next experiment to be run is:")
print("Cooling rate = " + str(x_next[:,0]))
print("Seed mass = " + str(x_next[:,1]))
print("Seed SS = " + str(x_next[:,2]))

#PLOTTERS
O = np.ravel(normalized_df2["Objective Function"])
desO = np.sort(O)[::-1]
xn = list(range(1,len(O)+1))
plt.xlabel("Number of experiments")
plt.ylabel("Objective function value")
plt.plot(xn,O)
plt.show()