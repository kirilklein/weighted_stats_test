#%%
import funcs
import importlib
importlib.reload(funcs)
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
#%%
x = np.linspace(0.1,1,20)
X = ss.beta.rvs(a=2,b=2,size=100)

print(funcs.indicator_func(x, X).shape)
print(funcs.emp_dist_func(x,X).shape)
fig, ax = plt.subplots()
ax.scatter(x, funcs.emp_dist_func(x,X), label='Empirical distribution')
ax.scatter(x, ss.beta.cdf(x,a=2,b=2), label='Theoretical distribution')
ax.legend()