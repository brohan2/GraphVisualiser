import numpy as np
from dash.dependencies import Input, Output, State
from components.graph_visualizer import create_graph
from components.graph_traversals import bfs_traversal, dfs_traversal
from components.code_editor import code_editor
import dash_html_components as html  # Ensure html is imported

def register_callbacks(app):
    @app.callback(
        Output('dynamic-content', 'children'),
        [Input('create_matrix_btn', 'n_clicks')]
    )
    def update_content(create_matrix_clicks):
        if create_matrix_clicks and create_matrix_clicks > 0:
            return code_editor()  # Show the code editor when the button is clicked
        return html.Div()  # Default content (or nothing) when no button is clicked

    @app.callback(
        Output('graph', 'figure'),
        [Input('matrix-size', 'value'),
         Input('matrix-tables', 'data'),
         Input('traversal-method', 'value'),
         Input('interval-component', 'n_intervals')],
        [State('traversal-method', 'value')]
    )
    def update_graph(matrix_size, matrix_data, traversal_method, n_intervals, traversal_state):
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
            
            traversal = []
            if traversal_method == 'BFS':
                traversal = bfs_traversal(adj_matrix)
            elif traversal_method == 'DFS':
                traversal = dfs_traversal(adj_matrix)
            
            # Determine the step index based on n_intervals
            step_index = min(n_intervals, len(traversal) - 1) if traversal else 0
            
            # Highlight nodes up to the current step
            nodes_highlight = traversal[:step_index + 1]
            queue_stack_state = {
                'queue': traversal[:step_index + 1]  # Display the state of the traversal queue or stack
            }

            return create_graph(adj_matrix, traversal=nodes_highlight, queue_stack_state=queue_stack_state)
        except Exception as e:
            print(f"Error parsing matrix: {e}")
            return create_graph(np.array([[0, 1], [1, 0]]))
    
    @app.callback(
        Output('interval-component', 'disabled'),
        [Input('start-traversal-btn', 'n_clicks')],
        [State('interval-component', 'disabled'),
         State('matrix-size', 'value'),
         State('matrix-tables', 'data'),
         State('traversal-method', 'value'),
         State('graph', 'figure')]  # Added state for graph figure
    )
    def toggle_interval(start_btn_clicks, interval_disabled, matrix_size, matrix_data, traversal_method, graph_figure):
        # Determine if traversal is complete
        traversal_complete = True  # Default to True (complete)
        if graph_figure:
            # Check if the traversal is complete by evaluating the figure data
            step_index = len(graph_figure['data'][2]['text']) - 1  # Last index of queue_stack_state text
            if step_index < len(bfs_traversal(np.array([
                [int(matrix_data[i][f'col-{j}']) for j in range(int(matrix_size))]
                for i in range(int(matrix_size))
            ]))):
                traversal_complete = False
        
        if start_btn_clicks and start_btn_clicks > 0 and not traversal_complete:
            # If start button is clicked and traversal is not complete, enable the interval component
            return False
        return True
