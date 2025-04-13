import pandas as pd
import numpy as np
q1 = pd.Series(np.arange(1,20))
q2 = pd.Series(np.random.randint(10,20,size=10))
q3 = pd.Series([i*10 for i in range(10,20)])
print(q1)
print(q2)
print(q3)

