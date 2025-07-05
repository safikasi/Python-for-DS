import plotly.express as px
import pandas as pd

# Example dataset: country ISO codes and values (population in millions)
data = {
    "country": ["Pakistan", "India", "United States", "Russia", "Brazil", "China", "Canada", "Germany"],
    "iso_alpha": ["PAK", "IND", "USA", "RUS", "BRA", "CHN", "CAN", "DEU"],
    "population": [241, 1440, 331, 146, 214, 1439, 38, 83]  # Approx in millions
}

df = pd.DataFrame(data)

# Create choropleth map
fig = px.choropleth(
    df,
    locations="iso_alpha",        # 3-letter country ISO code
    color="population",           # Data to color-code
    hover_name="country",         # Hover info
    color_continuous_scale="Viridis",  # Color scheme (can try 'Plasma', 'Cividis', etc.)
    projection="natural earth",   # Map projection type
    title="World Population by Country"
)

# Show the map
fig.show()
