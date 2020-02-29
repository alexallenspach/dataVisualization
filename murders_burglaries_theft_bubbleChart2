import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/saranking/bubbleChartDataSet.csv")

plt.figure(figsize=(20,13))

# pulling in the data from csv file
x = df['murder']
y = df['burglary']
z = df['state']
colorScatter = df['larceny_theft']
cm = plt.cm.get_cmap('jet') #Changing the default colorbar colors
area = np.sqrt(df['population'])

#Labeling the state's names for each bubble
for i,type in enumerate(z):
    xp = x[i]
    yp = y[i]
    plt.text(xp, yp, z[i], fontsize=9, horizontalalignment='center')

# making the bubble chart
bubble = plt.scatter(x, y, c=colorScatter, s=area, linewidths=2, edgecolor='face', cmap=cm)
bubble.set_alpha(0.75)

clb = plt.colorbar(bubble)
clb.set_label('Larceny Theft', labelpad=-50, y=1.02, rotation=0)
plt.axis([0,11,200,1280])
plt.title("United States Murders, Burglaries, and Theft in 2005")
plt.xlabel('Murders (per 100,000 population)')
plt.ylabel('Burglaries (per 100,000 population)')

fig1 = plt.gcf() #Get current figure so savefig works properly
plt.show()
fig1.savefig('visualization_histogram.png') #Save histogram chart as png
