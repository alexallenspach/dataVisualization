import altair as alt
import pandas as pd
from altair import Color, Scale

df = pd.read_csv('/Users/saranking/weight-height.csv')

alt.data_transformers.enable('default', max_rows=None)

chart = alt.Chart(df).mark_point().encode(
    Color('Gender:N',
          scale=Scale(domain=['Male', 'Female'],
                      range=['#1f77b4', '#e377c2'])),
    x=alt.X('Height_in:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('Weight_lbs:Q', scale=alt.Scale(zero=False)),
    tooltip=['Height_in', 'Weight_lbs', 'Gender'],
    opacity=alt.value(0.45)
).properties(background='white')

chart
chart.save('scatterPlot.png', scale_factor=2.0)
