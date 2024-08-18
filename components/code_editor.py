from dash import dash_table, html, dcc
from dash.dependencies import Input, Output, State
import dash

def code_editor():
    return html.Div(style={'width': '50%', 'padding': '20px'}, children=[
        html.H1('Adjacency Matrix Input'),
        html.Div(id='matrix-container', children=[
            dcc.Input(
                id='matrix-size',
                type='number',
                min=1,
                placeholder='Enter size of matrix',
                style={'width': '100%'}
            )
        ]),
        html.Div(id='matrix-table-container')
    ])

@dash.callback(
    Output('matrix-table-container', 'children'),
    [Input('matrix-size', 'value')]
)
def update_matrix_input(size):
    if size and size > 0:
        try:
            size = int(size)
            columns = [{'name': 'Row/Col', 'id': 'row-col'}] + [{'name': f'Column {i}', 'id': f'col-{i}'} for i in range(size)]

            data = [{'row-col': f'Row {i}'} | {f'col-{j}': '0' for j in range(size)} for i in range(size)]
            return dash_table.DataTable(
                id='matrix-tables',
                columns=columns,
                data=data,
                editable=True,
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'center'}
            )
        except ValueError:
            return html.Div('Invalid input. Please enter a positive integer.')
    return html.Div()
