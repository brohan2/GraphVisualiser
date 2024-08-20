import numpy as np
from dash import Input, Output, State, callback
from components.graph_visualizer import create_graph
from components.graph_traversals import bfs_traversal, dfs_traversal
from components.code_editor import code_editor
from dash import html

# Initialize the state to store the user-provided adjacency matrix
user_created_graph = {'adj_matrix': np.array([[0, 1], [1, 0]])}
traversal_state = {'nodes_highlight': [], 'queue_stack_state': None}  # Store traversal state

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
         Input('starting-node', 'value'),
         Input('interval-component', 'n_intervals')],
        [State('traversal-method', 'value')]
    )
    def update_graph(matrix_size, matrix_data, traversal_method, starting_node, n_intervals, traversal_state_value):
        global user_created_graph, traversal_state
        
        if not matrix_size or not matrix_data:
            # Default graph if no input
            return create_graph(user_created_graph['adj_matrix'], traversal=None, queue_stack_state=None)
        
        try:
            size = int(matrix_size)
            if len(matrix_data) != size:
                raise ValueError("Matrix size does not match data rows.")
            
            adj_matrix = np.array([
                [int(matrix_data[i][f'col-{j}']) for j in range(size)]
                for i in range(size)
            ])
            
            # Store the user-created graph state before traversal
            user_created_graph['adj_matrix'] = adj_matrix
            
            if not traversal_method:
                return create_graph(adj_matrix, traversal=None, queue_stack_state=None)
            
            # Set the starting node, default to 0 if not provided
            starting_node = int(starting_node) if starting_node else 0

            traversal = []
            if traversal_method == 'BFS':
                traversal = bfs_traversal(adj_matrix, starting_node)
            elif traversal_method == 'DFS':
                traversal = dfs_traversal(adj_matrix, starting_node)
            
            # Determine the step index based on n_intervals
            step_index = min(n_intervals, len(traversal) - 1) if traversal else 0
            
            # Highlight nodes up to the current step
            nodes_highlight = traversal[:step_index + 1]
            queue_stack_state = {
                'queue': traversal[:step_index + 1]  # Display the state of the traversal queue or stack
            }

            traversal_state = {'nodes_highlight': nodes_highlight, 'queue_stack_state': queue_stack_state}

            return create_graph(adj_matrix, traversal=nodes_highlight, queue_stack_state=queue_stack_state)
        except Exception as e:
            print(f"Error parsing matrix: {e}")
            return create_graph(user_created_graph['adj_matrix'], traversal=None, queue_stack_state=None)
    
    @app.callback(
        Output('interval-component', 'disabled'),
        [Input('start-traversal-btn', 'n_clicks')],
        [State('interval-component', 'disabled'),
         State('matrix-size', 'value'),
         State('matrix-tables', 'data'),
         State('traversal-method', 'value'),
         State('starting-node', 'value'),
         State('graph', 'figure')]
    )
    def toggle_interval(start_btn_clicks, interval_disabled, matrix_size, matrix_data, traversal_method, starting_node, graph_figure):
        if start_btn_clicks and start_btn_clicks > 0:
            # Enable interval component if start button is clicked and traversal is not complete
            return False
        
        # Ensure interval is disabled if traversal is complete
        if traversal_method and traversal_state['nodes_highlight']:
            return True
        
        return interval_disabled
