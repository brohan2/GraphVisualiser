import numpy as np
from dash.dependencies import Input, Output
from components.graph_visualizer import create_graph

def register_callbacks(app):
    @app.callback(
        Output('graph', 'figure'),
        [Input('matrix-size', 'value'),
         Input('matrix-tables', 'data')]
    )
    def update_graph(matrix_size, matrix_data):
        if not matrix_size or not matrix_data:
            # Default graph if no input
            return create_graph(np.array([[0, 1], [1, 0]]))
        
        try:
            size = int(matrix_size)
            if len(matrix_data) != size:
                raise ValueError("Matrix size does not match data rows.")
            
            adj_matrix = np.array([
                [int(matrix_data[i][f'col-{j}']) for j in range(size)]
                for i in range(size)
            ])
            return create_graph(adj_matrix)
        except Exception as e:
            print(f"Error parsing matrix: {e}")
            return create_graph(np.array([[0, 1], [1, 0]]))
