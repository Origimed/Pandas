import numpy as np
import pandas as pd



a = np.array([[1,2,3], [4,5,6]])

#print(a)

b = np.ones(shape=(2,2))
#print(b)


wines = np.genfromtxt(fname="/home/ptro/Code/un/TLP/Curso/code/winequality-red.csv", delimiter=";", skip_header=1)

##print(wines)

quality = wines[:,-1]
print(quality)




max_quality = quality.max()


print(max_quality)