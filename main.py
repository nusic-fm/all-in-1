import os
import tempfile
from flask import Flask, request, jsonify
import allin1

app = Flask(__name__)

@app.route("/", methods=["GET"])
def entry():
    return "saulgoodman...", 200

@app.route("/all-in-one", methods=["POST"])
def allInOne():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    print(file.filename)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        # Save the uploaded audio file to a temporary location
        temp_path = tempfile.mktemp(suffix='.wav')
        file.save(temp_path)
        print("Track is received and saved on the local", temp_path)

        try:
            result = allin1.analyze(temp_path)

            return jsonify({'segments': result.segments, 'bpm': result.bpm, 'beats': result.beats, 'downbeats': result.downbeats, 'beat_positions': result.beat_positions})
        except Exception as e:
            return jsonify({'error': f'{str(e)}'})
        
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))