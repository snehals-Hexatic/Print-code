import numpy as np

a = np.array([101, 12, 300, 4, 500])
b = np.array([100, 20, 30, 400, 50])

result = np.where(a > b, a, b)
print(result)
