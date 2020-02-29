import pandas as pd
import altair as alt

df = pd.read_csv('/Users/saranking/areaChart.csv')

alt.data_transformers.enable('default', max_rows=None) #Ensures no MaxRowsError 

chart = alt.Chart(df).mark_area().encode(
    x=alt.X("Year"),
    y=alt.Y("Name Count", stack="normalize"), #Normalize to take percentage of each group
    color="Names",
    tooltip=["Names"],
    opacity=alt.value(0.8)
).properties(
    background='white',
    title='Most Popular US Names Within Last 30 Years')

chart
chart.save('areaChart.png', scale_factor=2.0)
