import plotly as py
from plotly import tools
import plotly.graph_objs as go
import pandas as pd

#set up offline mode
py.offline.init_notebook_mode(connected=True)
df = pd.read_csv('/Users/saranking/Downloads/simple_candlestick.csv')

trace = go.Candlestick(x=df['x'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])
layout = go.Layout(
    title=go.layout.Title(
        text='AAPL Stock',
        xref='paper',
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='Date',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='Stock Price',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
)

data = [trace]
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='appleStocks.html')
