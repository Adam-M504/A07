import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Create the database
data = {
    'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022],
    'Winner': ['Uruguay', 'Italy', 'Italy', 'Uruguay', 'Germany', 'Brazil', 'Brazil', 'England', 'Brazil', 'Germany', 'Argentina', 'Italy', 'Argentina', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany', 'France', 'Argentina'],
    'Runner-up': ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Hungary', 'Sweden', 'Czechoslovakia', 'Germany', 'Italy', 'Netherlands', 'Netherlands', 'Germany', 'Germany', 'Argentina', 'Italy', 'Brazil', 'Germany', 'France', 'Netherlands', 'Argentina', 'Croatia', 'France']
}
results = pd.DataFrame(data)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='View All Winners', value='tab-1'),
        dcc.Tab(label='Specific Country', value='tab-2'),
        dcc.Tab(label='Specific Year', value='tab-3'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('All Countries that have won the World Cup'),
            html.Pre(f"{results['Winner'].unique()}")
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.Input(id='country-input', type='text', placeholder='Enter a Country', debounce=True),
            html.Div(id='country-output')
        ])
    elif tab == 'tab-3':
        return html.Div([
            dcc.Input(id='year-input', type='number', placeholder='Enter a Year', debounce=True),
            html.Div(id='year-output')
        ])

@app.callback(
    Output('country-output', 'children'),
    Input('country-input', 'value'))
def update_country_output(value):
    if value:
        value = value.capitalize()
        win_results = results[results['Winner'] == value]
        if not win_results.empty:
            return f"{value} has won the World Cup {len(win_results)} time(s)."
        else:
            return f"{value} has not won the World Cup."

@app.callback(
    Output('year-output', 'children'),
    Input('year-input', 'value'))
def update_year_output(value):
    if value:
        year_results = results[results['Year'] == value]
        if not year_results.empty:
            return f"The winner in {value} was {year_results.iloc[0]['Winner']} and the runner-up was {year_results.iloc[0]['Runner-up']}."
        else:
            return "There was no World Cup in that year."

if __name__ == '__main__':
    app.run(debug=True)
