from flask import Flask, request, jsonify, render_template
import os
import requests
import json
from app import app

# Serve the frontend HTML file
@app.route('/')
def index():
    return render_template('index.html')

# Handle the file upload and API processing
@app.route('/process', methods=['POST'])
def process_files():
    try:
        if 'image' not in request.files or 'audio' not in request.files:
            return jsonify({"error": "Both image and audio files are required."}), 400

        image = request.files['image']
        audio = request.files['audio']

        # Define the JSON payload
        payload = {}

        files = [
            ("input_face", image.stream),
            ("input_audio", audio.stream),
        ]

        api_key = os.environ.get("GOOEY_API_KEY", "")
        if not api_key:
            return jsonify({"error": "API key is not set."}), 500

        # Make the POST request with the JSON payload as a field
        response = requests.post(
            "https://api.gooey.ai/v2/Lipsync/form/?run_id=fecsii61rs6e&uid=fm165fOmucZlpa5YHupPBdcvDR02",
            headers={"Authorization": "Bearer " + api_key},
            files=files,
            data={"json": json.dumps(payload)},  # Pass the payload as a field named "json"
        )

        # Log the response for debugging
        print("API Response Status Code:", response.status_code)
        print("API Response Text:", response.text)

        # Check API response and extract output video URL
        if response.ok:
            response_data = response.json()
            print("Parsed Response Data:", response_data)  # Log parsed response data
            output = response_data.get("output", {})
            video_url = output.get("output_video")  # Access the nested key
            if video_url:
                return jsonify({"video_url": video_url})
            else:
                # Log the keys in the response data for debugging
                print("Available keys in response data:", response_data.keys())
                print("Available keys in output data:", output.keys())
                return jsonify({"error": "Video URL not found in the response."}), 500
        else:
            return jsonify({"error": "API request failed with status code " + str(response.status_code)}), 500
    except Exception as e:
        print("Exception occurred:", str(e))
        return jsonify({"error": "An error occurred on the server: " + str(e)}), 500