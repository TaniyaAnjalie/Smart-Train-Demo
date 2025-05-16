from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Allow requests from GitHub Pages domain
CORS(app, resources={r"/*": {"origins": "https://taniyaanjalie.github.io"}})

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')

    # Your logic to validate whether lat/lon is on railway line
    print(f"Received: lat={lat}, lon={lon}")

    # For demo, always accept
    return jsonify({"status": "success", "message": "Location received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
