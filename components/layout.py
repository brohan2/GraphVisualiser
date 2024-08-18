import dash_html_components as html
import dash_core_components as dcc
from dash import Input, Output, callback
from components.graph_visualizer import create_graph
from components.code_editor import code_editor

# Define the layout
layout = html.Div(style={'display': 'flex'}, children=[
    html.Div(style={'width': '50%', 'padding': '20px', 'display': 'flex', 'flex-direction': 'column'}, children=[
        html.H1('Options'),
        dcc.RadioItems(
            id='option-selector',
            options=[
                {'label': 'Create and Visualize Graph', 'value': 'create'},
                {'label': 'BFS Traversal', 'value': 'bfs'},
                {'label': 'DFS Traversal', 'value': 'dfs'}
            ],
            value='create'
        ),
        html.Div(id='dynamic-content')  # This will hold the dynamic content
    ]),
    html.Div(style={'width': '50%'}, children=[
        html.H1(children='DSA Graph Visualizer'),
        dcc.Graph(id='graph', style={'height': '90vh'})
    ])
])

# Callback to update the content dynamically based on the selected option
@callback(
    Output('dynamic-content', 'children'),
    Input('option-selector', 'value')
)
def update_content(selected_option):
    if selected_option == 'create':
        return code_editor()  # Invoke code_editor() if 'create' is selected
    elif selected_option == 'bfs':
        return html.Div('BFS Traversal selected. (Further input fields or information can be added here)')
    elif selected_option == 'dfs':
        return html.Div('DFS Traversal selected. (Further input fields or information can be added here)')
