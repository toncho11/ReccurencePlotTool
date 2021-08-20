import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys


from pyts.image import RecurrencePlot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


sin_func = np.random.uniform(-1,0,1000)
y = np.sin(sin_func)

X = np.reshape(y,(1, y.size)) #1 because we have only one input

# Recurrence plot transformation
rp = RecurrencePlot(threshold='point', percentage=20)
X_rp = rp.fit_transform(X)

#plt.subplot(211)
#plt.plot(y)
#plt.subplot(212)
plt.imshow(X_rp[0],  cmap='binary', origin='lower')