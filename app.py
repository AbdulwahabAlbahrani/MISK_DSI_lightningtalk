
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


app = Dash(__name__)

app.layout = html.Div([
    html.H1("This is the test for the presentaion", style={
        'textAlign': 'center',
    }),
    
    html.Div("this was prepared by Abdulwahab Albahrani"),
    dcc.Input(
        id="input",
        type="number",
        placeholder="this is a text"
    ),
    html.Div(id="place"),
    html.H1("This is an H1"),
    dcc.Slider(
        id="slider",
        marks={ i: str(i) for i in range(10) },
        value=0,
    ),
    html.Div(id="output2"),
    html.Div("Chose a year to see the life expecticy"),
    dcc.Slider(
        # df['year'].min(),
        # df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    ),
    dcc.Graph(id='lifeExp',figure={}),
    
    
])

@app.callback(
    Output('place','children'),
    Input('input','value'),
)
def jga(x):
    return x



@app.callback(
    Output('output2', 'children'),
    Input('slider','value'),
)
def callback(y):
    return y



@app.callback(
    Output(component_id='lifeExp', component_property='figure'),
    Input(component_id='year-slider', component_property='value'),
)
def update_graph(input):
    dff = df.copy()
    dff = dff[dff["year"] == input]

    # # Plotly Express
    fig = px.bar(
        dff,
        x= 'country',
        y = 'lifeExp',
        # hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        # labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        # template='plotly_dark'
        )
    fig.update_layout( xaxis={'categoryorder':'total descending'})
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)