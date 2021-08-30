import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
df = px.data.iris()
fig = px.scatter_matrix(df,
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
    color="species")
fig.show()