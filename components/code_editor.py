import dash_html_components as html
import dash_core_components as dcc

def code_editor():
    return html.Div(style={'width': '50%', 'padding': '20px'}, children=[
        html.H1('Adjacency Matrix Input'),
        dcc.Textarea(
            id='matrix-input',
            style={'width': '100%', 'height': '30vh'},
            placeholder='Enter adjacency matrix, e.g.,\n0 1 1 0\n1 0 0 1\n1 0 0 1\n0 1 1 0'
        ),
    ])
