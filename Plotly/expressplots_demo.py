import pandas as pd
import numpy as np
import plotly.express as px

# Step 1: Create data
df = pd.DataFrame(np.random.randn(100, 2), columns=["A", "B"])
df["Index"] = df.index

# Step 2: Melt the data to long format
df_melted = df.melt(id_vars="Index", value_vars=["A", "B"], var_name="Series", value_name="Value")

# Step 3: Plot
fig = px.line(
    df_melted,
    x="Index",
    y="Value",
    color="Series",
    title="Line Plot of Random Data",
    labels={"Value": "Y Axis Value", "Index": "X Axis Index"}
)

fig.show()

