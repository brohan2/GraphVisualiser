import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback

# Define the layout
layout = html.Div([
        html.Header([
        html.Title("Your Custom Title")  # Change this to your desired title
    ]),
    html.Div([
        html.H1("Graph Visualizer", style={
            'textAlign': 'center',
            'color': '#ffffff',
            'backgroundColor': '#007BFF',
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
            'margin': '0',
            'width': '100%',
            'boxSizing': 'border-box'
        }),
    ], style={'width': '100%', 'marginBottom': '20px', 'boxSizing': 'border-box'}),

    # Main content area
    html.Div([
        # Left side for options and dynamic content
        html.Div([
            # Option Button
            dbc.Button("Create and Visualize Graph", id='create_matrix_btn', color="primary", className="me-2", n_clicks=0, style={
                'padding': '10px 20px',
                'borderRadius': '8px',
                'transition': 'backgroundColor 0.3s',
                'marginBottom': '20px',
                'width': '100%',
                'boxSizing': 'border-box'
            }),

            # Dynamic content area for DataTable and traversal options
            html.Div(id='dynamic-content', style={
                'width': '100%',
                'boxSizing': 'border-box'
            }),

            # Starting Node Input
            html.Div([
                html.Label("Starting Node:", style={'marginRight': '10px'}),
                dcc.Input(id='starting-node', type='number', min=0, style={'width': '100%', 'marginBottom': '10px'})
            ], style={'width': '100%', 'boxSizing': 'border-box'}),

            # Traversal Dropdown, Start Button, and Clear Button
            html.Div([
                dcc.RadioItems(
                    id='traversal-method',
                    options=[
                        {'label': 'BFS', 'value': 'BFS'},
                        {'label': 'DFS', 'value': 'DFS'}
                    ],
                    value='None',
                    labelStyle={'display': 'inline-block'}
                ),
                dbc.Button("Start Traversal", id='start-traversal-btn', color="secondary", className="me-2", n_clicks=0, style={
                    'padding': '10px 20px',
                    'borderRadius': '8px',
                    'transition': 'backgroundColor 0.3s',
                    'marginRight': '10px',
                    'boxSizing': 'border-box'
                }),
                dbc.Button("Clear", id='clear-btn', color="danger", className="me-2", n_clicks=0, style={
                    'padding': '10px 20px',
                    'borderRadius': '8px',
                    'transition': 'backgroundColor 0.3s',
                    'boxSizing': 'border-box',
                    'display':'None'
                })
            ], style={'padding': '10px', 'textAlign': 'center', 'width': '100%', 'boxSizing': 'border-box'}),

            # Informational Text (default visible)
            html.P("You need to refresh the website for a new Traversal. We know it's not ideal.", style={
                'textAlign': 'center',
                'marginTop': '10px',
                'fontStyle': 'italic',
                'color': '#666'
            }),
            # Interval component for animation
            dcc.Interval(
                id='interval-component',
                interval=1*1000,  # Interval in milliseconds
                n_intervals=0,
                max_intervals=-1,
                disabled=True
            )
        ], style={
            'flex': '1 1 50%',
            'padding': '20px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '10px',
            'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
            'boxSizing': 'border-box',
            'width': '100%'
        }),
        

        # Right side for graph visualization
        html.Div([
            html.H2('DSA Graph Visualizer', style={'textAlign': 'center', 'color': '#007BFF'}),
            dcc.Graph(id='graph', style={'height': '80vh', 'width': '100%'})
        ], style={
            'flex': '1 1 50%',
            'padding': '20px',
            'backgroundColor': '#ffffff',
            'borderRadius': '10px',
            'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
            'boxSizing': 'border-box',
            'width': '100%'
        })
    ], style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'width': '100%',
        'boxSizing': 'border-box'
    })
], style={'width': '100%', 'boxSizing': 'border-box'})
