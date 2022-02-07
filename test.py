#%%
import pandas as pd
#%%
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# %%
df
# %%
x = df.columns
# %%
x
# %%
df.to_dict('records')
# %%
selected_year = 2002
df[df.year == selected_year]
# %%
L = df[df ['year'] == selected_year]
L.to_dict('records'), [{"name": i, "id": i} for i in df.columns]

# %%
L['country','year']