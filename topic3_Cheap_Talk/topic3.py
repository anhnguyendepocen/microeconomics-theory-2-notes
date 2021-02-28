
import matplotlib.pyplot as plt
import numpy as np
b = np.arange(0, 1, 0.01) 
N = 0.5+np.sqrt(0.25+1/(2*b))
plt.plot(b, N) 
plt.xlabel('b') 
plt.ylabel('N*')
plt.grid()
#plt.savefig('bNplot.png')  
plt.show()

print(0.5+np.sqrt(0.25+1/(2*1)))