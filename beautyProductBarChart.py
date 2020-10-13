from matplotlib import pyplot as plt #data visualization
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)

# Read in data from CSV File
df = pd.read_csv("/Users/saranking/bar_chart.csv")
print(df)

plt.figure(figsize=(13, 4)) #Create new figure and size 13 inches wide and height is 4 inches
plt.bar(df['Beauty Product'], df['Revenue in Dollars'] / 1000) #Create bar graph
plt.title("Beauty Products with Highest Gross Sales") #Label Title
plt.xlabel("Beauty Product") #Label x-axis
plt.ylabel("Revenue in Dollars [k$]") #Label y-axis

fig1 = plt.gcf() #Get current figure so savefig works properly
plt.show()
fig1.savefig('visualization_bar_chart.png') #Save bar chart as png
