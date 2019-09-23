import numpy as np
import matplotlib.pyplot as plt
import sobol_seq
import scipy.stats

fig, ax = plt.subplots(nrows=3, ncols=5)

#Uniform Distribution

axes = plt.subplot(3,5,1)
N = 50
norm = sobol_seq.i4_sobol_generate(1, N)
axes.set_title('N=50')
axes.set_ylabel('Uniform')
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,2)
N = 100
norm = sobol_seq.i4_sobol_generate(1, N)
axes.set_title('N=100')
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,3)
N = 250
norm = sobol_seq.i4_sobol_generate(1, N)
axes.set_title('N=250')
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,4)
N = 500
norm = sobol_seq.i4_sobol_generate(1, N)
axes.set_title('N=500')
plt.hist(norm, bins=N)

axes = plt.subplot(3,5,5)
N = 1000
norm = sobol_seq.i4_sobol_generate(1, N)
axes.set_title('N=1000')
plt.hist(norm, bins=N)

plt.show()