import streamlit as st
import random
import numpy as np
import cv2
from keras.models import load_model

# Load your pre-trained model for image classification
# Make sure to replace 'path_to_your_image_model.h5' with the actual path to your model
image_model = load_model('path_to_your_image_model.h5')

def analyze_soil(soil_types):
    """Simulates soil analysis and provides crop recommendations."""
    crop_recommendations = {}
    for soil in soil_types:
        recommendations = []
        # Generate a larger list of crops.
        all_crops = [
            "Wheat", "Rice", "Maize", "Soybean", "Barley", "Millet", "Sorghum", 
            "Cotton", "Sugarcane", "Sunflower", "Mustard", "Groundnut", "Potato", 
            "Tomato", "Onion", "Garlic", "Chilli", "Cabbage", "Cauliflower", 
            "Brinjal", "Okra", "Spinach", "Lettuce", "Carrot", "Radish", 
            "Cucumber", "Pumpkin", "Watermelon", "Mango", "Orange", "Apple", 
            "Banana", "Grape", "Pineapple", "Papaya", "Strawberry", "Blueberry", 
            "Raspberry", "Avocado", "Peach", "Pear", "Plum", "Cherry", "Apricot", 
            "Coconut", "Cashew", "Almond", "Peanut", "Coffee", "Tea", "Rubber", 
            "Jute", "Flax", "Hemp", "Chickpea", "Lentil", "Pea", "Bean", 
            "Cowpea", "Pigeonpea", "Green gram", "Black gram", "Horse gram", 
            "Moth bean", "Cluster bean", "Guar", "Sesbania", "Sunn hemp", 
            "Crotalaria", "Tephrosia", "Glycine max", "Phaseolus vulgaris", 
            "Vigna radiata", "Vigna mungo", "Cicer arietinum", "Lens culinaris", 
            "Pisum sativum"
        ]
        for _ in range(50):  # Generate 50 random recommendations per soil type
            recommendations.append(random.choice(all_crops))
        crop_recommendations[soil] = recommendations
    return crop_recommendations

def preprocess_image(image):
    """Preprocess the uploaded image for prediction."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = cv2.resize(image, (224, 224))  # Resize to match model input
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Expand dimensions
    return image

def predict_disease_from_image(image):
    """Predict disease based on the uploaded image."""
    processed_image = preprocess_image(image)
    prediction = image_model.predict(processed_image)
    predicted_class = np.argmax(prediction, axis=1)
    return predicted_class

def predict_disease(crop):
    """Simulates plant disease prediction based on user input."""
    possible_diseases = [
        f"{crop} Leaf Spot", f"{crop} Blight", f"{crop} Rust",
        f"{crop} Wilt", f"{crop} Root Rot", f"{crop} Powdery Mildew"
    ]
    predicted_disease = random.choice(possible_diseases)
    precautions = []
    
    # Simulate disease precautions
    if "Leaf Spot" in predicted_disease:
        precautions = ["Apply fungicides.", "Improve air circulation around plants."]
    elif "Blight" in predicted_disease:
        precautions = ["Improve drainage.", "Remove infected plant parts."]
    elif "Rust" in predicted_disease:
        precautions = ["Use resistant varieties.", "Apply fungicides as needed."]
    elif "Wilt" in predicted_disease:
        precautions = ["Ensure proper watering.", "Provide adequate nutrients to the soil."]
    elif "Root Rot" in predicted_disease:
        precautions = ["Improve soil drainage.", "Avoid overwatering."]
    elif "Powdery Mildew" in predicted_disease:
        precautions = ["Apply a sulfur-based fungicide.", "Increase air circulation."]
    
    return predicted_disease, precautions

# Streamlit app
st.title("Crop Recommendation and Disease Prediction based
