import numpy as np

t = np.array([[1, 5 , 5 ,70 , 30], [1, 2 , 3 , 4 ,5]])

print(t)

print(type(t))
print(t.shape)
print(t.ndim)
print(t.size)
print(t.dtype)
print(t[: , 0])
print(f"le minimum est {t.min()} , le maximum est {t.max()} , la moyenne est {t.mean()}")