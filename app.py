import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Title of the app
st.title('Connected Graphs with Plotly in Streamlit')

# Sample data for Plotly
data = {
    'x1': [1, 2, 3, 4],
    'y1': [10, 20, 30, 40],
    'x2': [1, 2, 3, 4],
    'y2': [40, 30, 20, 10]
}
df1 = pd.DataFrame({'x': data['x1'], 'y': data['y1']})
df2 = pd.DataFrame({'x': data['x2'], 'y': data['y2']})

# Create the first Plotly figure
fig1 = go.Figure(data=go.Scatter(x=df1['x'], y=df1['y'], mode='lines+markers', name='Graph 1'))

# Create the second Plotly figure
fig2 = go.Figure(data=go.Scatter(x=df2['x'], y=df2['y'], mode='lines+markers', name='Graph 2'))

# Add a connector line between specific points in the two graphs
fig1.add_shape(
    type='line',
    x0=df1['x'][1], y0=df1['y'][1],
    x1=df2['x'][1], y1=df2['y'][1],
    line=dict(color='RoyalBlue', width=2)
)

fig1.add_shape(
    type='line',
    x0=df1['x'][2], y0=df1['y'][2],
    x1=df2['x'][2], y1=df2['y'][2],
    line=dict(color='RoyalBlue', width=2)
)

# Display the Plotly figures in Streamlit
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

# Additional Streamlit elements
st.write("Here's a table of the data:")
st.write(df1)
st.write(df2)


