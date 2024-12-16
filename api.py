import os
import requests
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Path to the extracted model
model_path = 'nsfw_model/mobilenet_v2_140_224'

# Load the model
model = tf.keras.models.load_model(model_path)

# Categories for predictions
categories = ['Neutral', 'Drawing', 'Sexy', 'Porn', 'Hentai']

# Function to download the image
def download_image(image_url, save_path="temp_image.jpg"):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        return save_path
    else:
        raise Exception(f"Failed to download image. HTTP Status: {response.status_code}")

# Function to preprocess the input image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Resize to match model's input size
    img_array = image.img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# API endpoint to evaluate image quality
@app.route('/api/v1/ad-quality', methods=['POST'])
def ad_quality():
    try:
        # Parse the request JSON
        data = request.get_json()

        # Extract parameters
        image_id = data.get("id")
        image_url = data.get("image_url")

        if not image_id or not image_url:
            return jsonify({"error": "Missing required fields: 'id' and 'image_url'"}), 400

        # Download the image
        temp_file = f"temp_image_{image_id}.jpg"
        img_path = download_image(image_url, save_path=temp_file)

        # Preprocess the image
        input_image = preprocess_image(img_path)

        # Make predictions
        predictions = model.predict(input_image)

        # Interpret the predictions
        response_data = [
            {"category": category, "score": round(float(score) * 100, 2)}
            for category, score in zip(categories, predictions[0])
        ]

        # Clean up the temporary file
        if os.path.exists(temp_file):
            os.remove(temp_file)

        # Return the response
        return jsonify({"Response": response_data})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6969)
