import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Title of the app
st.title('My Streamlit App with Plotly')

# Sample data for Plotly
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [5, 15, 25, 35]
}
df = pd.DataFrame(data)

# Create a Plotly figure
fig = px.line(df, x='A', y=['B', 'C'], title='Line Chart Example')

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)

# Additional Streamlit elements
st.write("Here's a table of the data:")
st.write(df)

