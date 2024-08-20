from flask import Flask
import dash
from components.layout import layout
from components.callbacks import register_callbacks
from dash import dcc, html

# Initialize Flask app
app = Flask(__name__)

# Initialize Dash app within Flask
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/')
dash_app.title = 'GraphMika'  # This will set the title of the Dash app

# Define the layout with title in the meta component
dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Allows dynamic routing
    html.Header([
        html.Title('GraphMika')  # Set the title here
    ]),
    layout  # Your main layout
])

# Register Dash callbacks
register_callbacks(dash_app)

@app.route('/')
def index():
    return 'Welcome to the DSA Graph Visualizer! <a href="/dash/">Go to Graph</a>'

if __name__ == '__main__':
    app.run(debug=True)
