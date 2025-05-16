# backend/app.py
from flask import Flask, request, jsonify
import pandas as pd
from shapely.geometry import LineString, Point
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load railway lines from CSV
railway_data = pd.read_csv('railways.csv')
railway_lines = []

for _, row in railway_data.iterrows():
    try:
        coords = eval(row['geometry'].replace('LINESTRING', '').strip())
        if isinstance(coords, list) and len(coords) > 1:
            railway_lines.append(LineString(coords))
    except:
        continue

# Distance threshold in degrees (~50 meters)
THRESHOLD = 0.0005

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    lat = data['lat']
    lon = data['lon']
    point = Point(lon, lat)

    on_track = any(line.distance(point) < THRESHOLD for line in railway_lines)

    if on_track:
        return jsonify({'status': 'accepted', 'message': 'Location is on the railway line.'})
    else:
        return jsonify({'status': 'rejected', 'message': 'Location is off the railway line.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
