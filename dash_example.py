from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import folium
import plotly.express as px
import pandas as pd

df_case_yearly = pd.read_csv("df_case_yearly.csv",   index_col=None)
df_category_10 = pd.read_csv("df_category_10.csv",   index_col=None)
#df_incident_day = pd.read_csv("df_incident_day.csv", index_col=None)

app = Dash(external_stylesheets=[dbc.themes.MINTY])



fig1 = px.pie(df_category_10, values='incidents_count', names='category',color_discrete_sequence=px.colors.sequential.RdBu ,width=600, height=500)
#fig1.update_layout(showlegend=False)
fig2 = px.bar(df_case_yearly, x="Year", y="Total Cases", color="Total Cases", width=650, height=500)
fig2.update_yaxes(title=None)

fig3 = px.bar(df_category_10, x="incidents_count", y="category",color="incidents_count",width=550, height=500)
fig3.update_layout(yaxis=dict(autorange="reversed"))
fig3.update_yaxes(title=None)

graphs = html.Div([
        dbc.Row(
            [
            dbc.Col(html.Iframe(id='map', srcDoc=open('index.html', 'r').read(), width='100%', height='500')),
            dbc.Col(dcc.Graph(id='graph1', figure=fig1))
            ],
            className='mt-4'),
        dbc.Row(
            [
            dbc.Col(dcc.Graph(id='graph2',figure=fig2)),
            dbc.Col(dcc.Graph(id='graph3', figure=fig3))
            ],
            className="mt--4")
            ])

heading = html.H1("San Francisco Police Incidents Report 2018-2022"
                  ,className="bg-success text-white p-3")
app.layout = dbc.Container([heading, graphs], fluid=True)
if __name__ == '__main__':
    app.run_server(debug=True, port=8040)
    

