import networkx as nx
import plotly.graph_objects as go
import numpy as np

def create_graph(adj_matrix, traversal=None, queue_stack_state=None):
    G = nx.from_numpy_array(adj_matrix)
    
    # Compute node positions once and reuse them
    pos = nx.spring_layout(G, seed=42)  # Seed ensures consistency

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_color = []
    node_size = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        if traversal and node in traversal:
            node_color.append('black')
            node_size.append(60)
        else:
            node_color.append('black')
            node_size.append(50)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='none',
        marker=dict(
            showscale=False,
            color=node_color,
            size=node_size,
            line=dict(width=3, color='black'),
        ),
        text=[str(node) for node in G.nodes()],
        textfont=dict(size=14, color='white'),
        textposition="middle center"
    )
    
    if queue_stack_state:
        queue_x = [pos[node][0] for node in queue_stack_state['queue']]
        queue_y = [pos[node][1] for node in queue_stack_state['queue']]
        queue_trace = go.Scatter(
            x=queue_x, y=queue_y,
            mode='markers+text',
        marker=dict(
            showscale=False,
            color='gray',
            size=node_size,
            line=dict(width=3, color='blue'),
        ),    
            textposition='top center',
            textfont=dict(size=14, color='black'),

            # showlegend=False
        )
        fig = go.Figure(data=[edge_trace, node_trace, queue_trace],
                        layout=go.Layout(
                            title='Traversal',
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=0, l=0, r=0, t=0),
                            xaxis=dict(showgrid=False, zeroline=False),
                            yaxis=dict(showgrid=False, zeroline=False))
                        )
    else:
        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='Visualising',
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=0, l=0, r=0, t=0),
                            xaxis=dict(showgrid=False, zeroline=False),
                            yaxis=dict(showgrid=False, zeroline=False))
                        )
    
    return fig
