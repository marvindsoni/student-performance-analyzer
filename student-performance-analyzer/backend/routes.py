from flask import Blueprint, request, jsonify
# Import logic from Person 4 and Person 3
from Analysis.analysis import get_prediction
from Database.db import save_report

# We use a Blueprint to keep app.py clean
api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/test', methods=['GET'])
def test_connection():
    """Quick route to check if the backend is alive"""
    return jsonify({"message": "Backend is online and reaching the routes!"}), 200

@api_bp.route('/predict', methods=['POST'])
def predict_student_performance():
    # 1. Grab the JSON sent by Person 1 (Frontend)
    user_data = request.get_json()

    # Basic safety check: Did they send anything?
    if not user_data:
        return jsonify({"error": "No data received from frontend"}), 400

    try:
        # 2. Send data to Person 4's logic (Analysis)
        # It expects: cgpa, coding_score, attendance, projects
        final_results = get_prediction(user_data)

        # 3. Send data to Person 3's logic (Database) to save it
        # We save the name and the result we just got
        save_report(
            user_data.get('name', 'Anonymous'),
            user_data.get('cgpa', 0),
            user_data.get('coding_score', 0),
            final_results.get('placement_probability', 'N/A')
        )

        # 4. Send the final answer back to the Website
        return jsonify(final_results), 200

    except Exception as e:
        # If something breaks in Person 4's or Person 3's code, we catch it here
        print(f"Error during processing: {e}")
        return jsonify({"error": "Internal server error. Check logic files."}), 500