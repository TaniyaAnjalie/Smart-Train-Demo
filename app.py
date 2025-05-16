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

    print(f"Received location: {lat}, {lon}")

    # Example: reject if outside bounds (simulate off-rail logic)
    if not (5.0 < lat < 10.0 and 79.0 < lon < 82.0):  # approx Sri Lanka bounds
        return jsonify({'message': 'Location rejected – outside rail area'}), 400

    return jsonify({'message': 'Location updated successfully'}), 200

if __name__ == '__main__':
    app.run(port=5000)

