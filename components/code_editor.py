from dash import dash_table, html, dcc, callback, Input, Output  # Import necessary Dash components

def code_editor():
    return html.Div(style={'width': '100%', 'padding': '20px'}, children=[
        html.H2('Adjacency Matrix Input'),
        dcc.Input(
            id='matrix-size',
            type='number',
            min=1,
            placeholder='Enter size of matrix',
            style={'width': '100%', 'margin-bottom': '10px'}
        ),
        html.Div(id='matrix-table-container')
    ])

@callback(
    Output('matrix-table-container', 'children'),
    Input('matrix-size', 'value')
)
def update_matrix_input(size):
    if size and size > 0:
        columns = [{'name': f'Column {i}', 'id': f'col-{i}'} for i in range(size)]
        data = [{'col-{}'.format(i): 0 for i in range(size)} for _ in range(size)]

        return dash_table.DataTable(
            id='matrix-tables',
            columns=columns,
            data=data,
            editable=True,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'center'}
        )
    return html.Div()
