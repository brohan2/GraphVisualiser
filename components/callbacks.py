import numpy as np
from dash.dependencies import Input, Output
from components.graph_visualizer import create_graph

def register_callbacks(app):
    @app.callback(
        Output('graph', 'figure'),
        [Input('matrix-input', 'value')]
    )
    def update_graph(matrix_input):
        if not matrix_input:
            return create_graph(np.array([[0, 1], [1, 0]]))  # Default example graph
        try:
            adj_matrix = np.array([
                [int(num) for num in row.split()]
                for row in matrix_input.splitlines()
            ])
            return create_graph(adj_matrix)
        except Exception as e:
            print(f"Error parsing matrix: {e}")
            return create_graph(np.array([[0, 1], [1, 0]]))
