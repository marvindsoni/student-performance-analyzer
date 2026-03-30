from flask import Flask
from flask_cors import CORS
import sys
import os

# --- PATH CONFIGURATION ---
# We need this so the backend can "see" the analysis and database folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now we import our custom modules
from routes import api_bp
from Database.db import init_db

def create_app():
    app = Flask(__name__)
    
    # Enable CORS so Person 1's Frontend can talk to us
    CORS(app)

    # Register the routes from routes.py
    app.register_blueprint(api_bp, url_prefix='/api')

    # Initialize the database file (placement.db) on startup
    with app.app_context():
        init_db()
        print("Database initialized successfully.")

    return app

if __name__ == '__main__':
    # Running the app
    # Debug=True is great for development; it restarts the server when you save
    my_app = create_app()
    print("Starting Student Analyzer Server on http://127.0.0.1:5000")
    my_app.run(debug=True, port=5000)