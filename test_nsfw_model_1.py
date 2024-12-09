import os
import requests
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np


# Path to the extracted model
model_path = 'nsfw_model/mobilenet_v2_140_224'

# Load the model
model = tf.keras.models.load_model(model_path)

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

# Define the image URL
# image_url = "https://sandbox.lemmatechnologies.com/media/1080/1732519530455896633-pngtree-lotus-flower-jpg-pink-lotus-flower-image_13023952.jpg"
# image_url="https://sandbox.lemmatechnologies.com/media/1080/1732875480934804142-pexels-life-of-pix-7919.jpg"

# Array of image URLs
image_urls = [
    "https://sandbox.lemmatechnologies.com/media/1080/1733224888644237689-pngimg.com%20-%20skull_PNG70.png",
    "https://sandbox.lemmatechnologies.com/media/1080/1733383990920810264-Screenshot%20from%202024-11-18%2011-50-42.png",
    "https://sandbox.lemmatechnologies.com/media/1080/1733390872843905792-Screenshot%20from%202024-11-29%2017-25-55.png",
    "https://sandbox.lemmatechnologies.com/media/1080/20240731070010-thumbnail-20240730125117-20230718114610-Motorola_RD_1080x1920_30June_2.jpg",
    "https://sandbox.lemmatechnologies.com/media/1080/20240731091842-Screenshot%20from%202024-07-25%2012-40-50.png"
]

# Categories for predictions
categories = ['Neutral', 'Drawing', 'Sexy', 'Porn', 'Hentai']

try:
    for i, image_url in enumerate(image_urls):
        print(f"Processing image {i + 1}/{len(image_urls)}: {image_url}")

        # Step 1: Download the image
        img_path = download_image(image_url, save_path=f"temp_image_{i}.jpg")
                        
        # Step 2: Preprocess the image
        input_image = preprocess_image(img_path)
                                                
        # Step 3: Make predictions
        predictions = model.predict(input_image)
                                                                        
        # Step 4: Interpret the predictions
        print("Predictions:")
        for category, score in zip(categories, predictions[0]):
            print(f"  {category}: {score:.2f}")
        print("-" * 50)
                        
finally:
    # Clean up all the temporary files
    for i in range(len(image_urls)):
        temp_file = f"temp_image_{i}.jpg"
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"Deleted temporary file: {temp_file}")




