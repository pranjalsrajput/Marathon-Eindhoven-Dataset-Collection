import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

videoData = pd.read_excel('./video_metadata.xlsx')
# print(videoData)
print(videoData['Duration'].describe())
ax=videoData.plot.hist(y='Duration', bins=1000)
table(ax, np.round(videoData['Duration'].describe(), 2), loc='upper center', colWidths=[0.2, 0.2, 0.2])
# videoData.plot.scatter(x='Sun', y='Duration')
plt.savefig("DurationStats.png")
plt.show()
