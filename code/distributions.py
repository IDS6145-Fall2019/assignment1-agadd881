import numpy as np
import matplotlib.pyplot as plt
import sobol_seq
import scipy.stats

fig, ax = plt.subplots(nrows=3, ncols=5)

axes = plt.subplot(3,5,1)

#Uniform Distribution
N = 50
uni = np.random.uniform(0,1,N)
axes.set_title('N=50')
axes.set_ylabel('Uniform')
plt.hist(uni, bins=N)

axes = plt.subplot(3,5,2)
N = 100
uni = np.random.uniform(0,1,N)
axes.set_title('N=100')
plt.hist(uni, bins=N)

axes = plt.subplot(3,5,3)
N = 250
uni = np.random.uniform(0,1,N)
axes.set_title('N=250')
plt.hist(uni, bins=N)

axes = plt.subplot(3,5,4)
N = 500
uni = np.random.uniform(0,1,N)
axes.set_title('N=500')
plt.hist(uni, bins=N)

axes = plt.subplot(3,5,5)
N = 1000
uni = np.random.uniform(0,1,N)
axes.set_title('N=1000')
plt.hist(uni, bins=N)

#Normal Distribution
axes = plt.subplot(3,5,6)
N = 50
norm = np.random.normal(0,0.1,N)
axes.set_ylabel('Normal')
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,7)
N = 100
norm = np.random.normal(0,0.1,N)
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,8)
N = 250
norm = np.random.normal(0,0.1,N)
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,9)
N = 500
norm = np.random.normal(0,0.1,N)
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,10)
N = 1000
norm = np.random.normal(0,0.1,N)
plt.hist(norm, bins=N)

#Exponential Distribution
axes = plt.subplot(3,5,11)
N = 50
expo = np.random.exponential(1,N)
axes.set_ylabel('Exponential')
plt.hist(expo, bins=N)

axes = plt.subplot(3,5,12)
N = 100
expo = np.random.exponential(1,N)
plt.hist(expo, bins=N)

axes = plt.subplot(3,5,13)
N = 250
expo = np.random.exponential(1,N)
plt.hist(expo, bins=N)

axes = plt.subplot(3,5,14)
N = 500
expo = np.random.exponential(1,N)
plt.hist(expo, bins=N)

axes = plt.subplot(3,5,15)
N = 1000
expo = np.random.exponential(1,N)
plt.hist(expo, bins=N)

plt.show()