import pandas as pd
import altair as alt
import geopandas as gpd
from matplotlib import pyplot as plt

alt.themes.enable('opaque')

# set the filepath and load in a shapefile
fp = "/Users/saranking/Colorado_County_Boundaries"
gdf = gpd.read_file(fp)
gdf.head()

df = pd.read_csv("/Users/saranking/profile-county.csv", header=0)
df.head()

# join the geodataframe with the cleaned up csv dataframe
merged = gdf.set_index('NUM_FIPS').join(df.set_index('CFIPS'))
merged.head()

# set a variable that will call whatever column we want to visualise on the map
variable = 'Total Population'

# set the range for the choropleth
vmin, vmax = 3522, 5609445

# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

# create map
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')

# remove the axis
ax.axis('off')

# add a title
ax.set_title("Total population in Colorado of 2017", fontdict={'fontsize': '25', 'fontweight' : '3'})

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))

# empty array for the data range
sm._A = []

# add the colorbar to the figure
cbar = fig.colorbar(sm)

fig.savefig("mapChart.png", dpi=300)
