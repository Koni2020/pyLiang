# pyLiang
# Disclaimer
This module is based on routines provided by Sanxiang Liang at http://www.ncoads.cn/.
# What is the pyLiang?
The liang-klleeman information flow (Liang) is used to detect causality between two time series. In a dynamic system, when information flow is transmitted between two entities in a specific way and often implies causality. Specifically, if the information flow rate between two time series events is close to zero, there is no causal relationship, vice versa.
# Dependencies
For the installation of pyLiang, the following packages are required:
* [numpy](https://numpy.org/)
# Installation
pyLiang can be installed using pip\
```pip install pyLiang```
# Usage
A quick example of pyLiang usage is as follow. 
```python
import numpy as np
from pyLiang import causality_est

# Data generation
ts1 = np.random.rand(360,1)
ts2 = np.random.rand(360,1)

res = causality_est(ts1, ts2)
print(res)
```
# References
1. San Liang X. Unraveling the cause-effect relation between time series[J]. Physical Review E, 2014, 90(5): 052150. doi:
2. San Liang X. Normalizing the causality between time series[J]. Physical Review E, 2015, 92(2): 022126. doi: 
