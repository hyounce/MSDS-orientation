import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('MSDS.xlsx')
values = data['CPU Number of Cores (int)'].values


plt.hist(values, bins=12, color='thistle', edgecolor='black')
plt.xlim(0,20)
plt.xlabel('Number of CPU Cores')
plt.ylabel('Number of Students')
plt.title('CPU Cores for MSDS Students')
plt.show()

