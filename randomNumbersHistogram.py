from matplotlib import pyplot as plt #data visualization
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)

# Read in data from CSV File
df = pd.read_csv("/Users/saranking/Random_numbers.csv")

# Variable that holds x-tick mark names
x_labels = ["0 to 10", "10 to 20", "20 to 30", "30 to 40", "40 to 50", "50 to 60", "60 to 70", "70 to 80", "80 to 90", "90 to 100"]

plt.figure(figsize=(12, 4))
plt.title("Frequency of 1000 Random Numbers From 0 to 100")
plt.xlabel("Bins")
plt.ylabel("Count")

plt.hist(df['Random Number'],rwidth=0.85) #Create histogram with spacing between bars at 85%

ax = plt.subplot()
ax.set_xticks(range(5, 100, 10))
ax.set_xticklabels(x_labels)

fig1 = plt.gcf() #Get current figure so savefig works properly
plt.show()
fig1.savefig('visualization_histogram.png') #Save histogram chart as png
