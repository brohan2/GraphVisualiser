import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback
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
            # Option Button
            dbc.Button("Create and Visualize Graph", id='create_matrix_btn', color="primary", className="me-2", n_clicks=0, style={
                'padding': '10px 20px',
                'border-radius': '8px',
                'transition': 'background-color 0.3s'
            }),

            # Dynamic content area for DataTable and traversal options
            html.Div(id='dynamic-content', style={'flex': 1}),
            
            # Traversal Dropdown and Start Button
            html.Div([
                dcc.RadioItems(
                    id='traversal-method',
                    options=[
                        {'label': 'BFS', 'value': 'BFS'},
                        {'label': 'DFS', 'value': 'DFS'}
                    ],
                    value='None',  # Default value
                    labelStyle={'display': 'inline-block'}
                ),
                dbc.Button("Start Traversal", id='start-traversal-btn', color="secondary", className="me-2", n_clicks=0, style={
                    'padding': '10px 20px',
                    'border-radius': '8px',
                    'transition': 'background-color 0.3s'
                })
            ], style={'padding': '10px'}),
            
            # Interval component for animation
            dcc.Interval(
                id='interval-component',
                interval=1*1000,  # Interval in milliseconds
                n_intervals=0,
                max_intervals=-1,
                disabled=True
            )
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
        ]),
    ])
])
