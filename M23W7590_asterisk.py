# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:01:34 2024

@author: M23W7590楊楓
"""
import matplotlib.pyplot as plt
import numpy as np
dX  = [0] * 11 + [1] * 11 + [2] * 6 +[3]*12 +[4] * 8 +[5]*4+[6]*12+[7]*9+[8]*5+[9]*13+[10]*9
a = np.arange(-1,11) + 0.5
plt.hist(dX,a,rwidth=0.8)
plt.xticks(range(0, 11))
plt.show()

