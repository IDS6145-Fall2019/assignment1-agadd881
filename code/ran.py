import numpy as np
import matplotlib.pyplot as plt
import sobol_seq
import scipy.stats

fig, ax = plt.subplots(nrows=3, ncols=5)

axes = plt.subplot(3,5,1)
N = 5
uni = np.random.uniform(0,1,N)
axes.set_title('N=5')
axes.set_ylabel('Uniform')
plt.plot(uni)

axes = plt.subplot(3,5,2)
N = 10
uni = np.random.uniform(0,1,N)
axes.set_title('N=10')
plt.plot(uni)

axes = plt.subplot(3,5,3)
N = 25
uni = np.random.uniform(0,1,N)
axes.set_title('N=25')
plt.plot(uni)

axes = plt.subplot(3,5,4)
N = 50
uni = np.random.uniform(0,1,N)
axes.set_title('N=50')
plt.plot(uni)

axes = plt.subplot(3,5,5)
N = 100
uni = np.random.uniform(0,1,N)
axes.set_title('N=100')
plt.plot(uni)

#standard normal distribution
mean = 1
std = 0.5

axes = plt.subplot(3,5,6)
N = 5
x = np.linspace(0, 2, N)
y = scipy.stats.norm.pdf(x,mean,std)
plt.plot(x,y)
axes.set_ylabel('Normal')

axes = plt.subplot(3,5,7)
N = 10
x = np.linspace(0, 2, N)
y = scipy.stats.norm.pdf(x,mean,std)
plt.plot(x,y)

axes = plt.subplot(3,5,8)
N = 25
x = np.linspace(0, 2, N)
y = scipy.stats.norm.pdf(x,mean,std)
plt.plot(x,y)

axes = plt.subplot(3,5,9)
N = 50
x = np.linspace(0, 2, N)
y = scipy.stats.norm.pdf(x,mean,std)
plt.plot(x,y)

axes = plt.subplot(3,5,10)
N = 100
x = np.linspace(0, 2, N)
y = scipy.stats.norm.pdf(x,mean,std)
plt.plot(x,y)

#Exonential Distribution
axes = plt.subplot(3,5,11)
N = 20
x = np.linspace(0, 1, N)
y = np.random.exponential(1,N)
axes.set_ylabel('Exponential')
plt.plot(x,y)

plt.show()