import numpy as np

numbers = np.array([1 ,3 , 4 , 5, np.nan , 6 , np.nan ])

position_nan = np.argwhere(np.isnan(numbers))


num_nan = np.isnan(numbers).sum()

print(np.isfinite(numbers))


print(num_nan)