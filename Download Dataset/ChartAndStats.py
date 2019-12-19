import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

videoData = pd.read_excel('/home/pranjal/Documents/PythonProjects/LeNetProject/data/video_metadata.xlsx')
# print(videoData)
print(videoData['Duration'].describe())
print("Total Duration: ",np.sum(videoData["Duration"]))
print("Total frames: ",30*np.sum(videoData["Duration"]))
ax=videoData.plot.hist(y='Duration', bins=500)
# for p in ax.patches:
#     ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
ax.set_xticks(range(0,5000,250))
ax.set_yticks(range(0,800,15))
table(ax, np.round(videoData['Duration'].describe(), 2), loc='upper center', colWidths=[0.2, 0.2, 0.2])
# videoData.plot.scatter(x='Sun', y='Duration')
plt.savefig("DurationStats.png")
plt.show()
