from flask import Flask
import dash
from components.layout import layout
from components.callbacks import register_callbacks

# app.py

from dash import dcc, html



# Initialize Flask app
app = Flask(__name__)

# Initialize Dash app within Flask
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')
dash_app.layout = layout

# Register Dash callbacks
register_callbacks(dash_app)

# Define a simple Flask route
@app.route('/')
def index():
    return 'Welcome to the DSA Graph Visualizer! <a href="/dash/">Go to Graph</a>'

if __name__ == '__main__':
    app.run(debug=True)
