import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash import Input, Output, callback, ctx
from components.graph_visualizer import create_graph
from components.code_editor import code_editor

# Define the layout
layout = html.Div([
    # Top-Centered Title
    html.Div([
        html.H1("Graph Visualizer", style={
            'textAlign': 'center',
            'color': '#ffffff',
            'background-color': '#007BFF',
            'padding': '20px',
            'border-radius': '10px',
            'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'
        }),
    ], style={'margin-bottom': '20px'}),

    # Main content area
    html.Div(style={'display': 'flex'}, children=[
        # Left side for options and dynamic content
        html.Div(style={
            'width': '50%', 
            'padding': '20px', 
            'display': 'flex', 
            'flex-direction': 'column',
            'background-color': '#f8f9fa', 
            'border-radius': '10px',
            'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'
        }, children=[
            # Option Buttons
            dbc.ButtonGroup([
                dbc.Button("Create and Visualize Graph", id='create_matrix_btn', color="primary", className="me-2", n_clicks=0),
                
                dbc.Button("BFS Traversal", id='bfs_btn', color="secondary", className="me-2", n_clicks=0),
                dbc.Button("DFS Traversal", id='dfs_btn', color="secondary", n_clicks=0),
            ], style={'margin-bottom': '20px'}),
            
            # Dynamic content area
            html.Div(id='dynamic-content', style={'flex': 1})
        ]),
        
        # Right side for graph visualization
        html.Div(style={
            'width': '50%', 
            'padding': '20px',
            'background-color': '#ffffff',
            'border-radius': '10px',
            'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'
        }, children=[
            html.H2('DSA Graph Visualizer', style={'textAlign': 'center', 'color': '#007BFF'}),
            dcc.Graph(id='graph', style={'height': '80vh'})
        ])
    ])
])

# Callback to update the content dynamically based on the selected option
@callback(
    Output('dynamic-content', 'children'),
    [Input('create_matrix_btn', 'n_clicks'),
     Input('bfs_btn', 'n_clicks'),
     Input('dfs_btn', 'n_clicks')]
)
def update_content(create_matrix_clicks, bfs_clicks, dfs_clicks):
    # Determine which button was clicked
    triggered_id = ctx.triggered_id

    # Handle the case where no button has been clicked yet (initial load)
    if triggered_id is None or triggered_id == 'create_matrix_btn':
        return code_editor()  # Default content on load

    if triggered_id == 'bfs_btn':
        return html.Div('BFS Traversal selected. (Further input fields or information can be added here)')
    
    if triggered_id == 'dfs_btn':
        return html.Div('DFS Traversal selected. (Further input fields or information can be added here)')
    
    return html.Div()  # Fallback in case no button was clicked
