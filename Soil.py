import streamlit as st
import random

def analyze_soil(soil_types):
    """Simulates soil analysis and provides crop recommendations."""
    crop_recommendations = {}
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
    
    for soil in soil_types:
        recommendations = random.sample(all_crops, min(15, len(all_crops)))  # Pick 15 random crops
        crop_recommendations[soil] = recommendations
    
    return crop_recommendations

def predict_disease(crop):
    """Simulates plant disease prediction based on user input."""
    possible_diseases = [
        f"{crop} Leaf Spot", f"{crop} Blight", f"{crop} Rust",
        f"{crop} Wilt", f"{crop} Root Rot", f"{crop} Powdery Mildew"
    ]
    predicted_disease = random.choice(possible_diseases)
    precautions = {
        "Leaf Spot": ["Apply fungicides.", "Improve air circulation around plants."],
        "Blight": ["Improve drainage.", "Remove infected plant parts."],
        "Rust": ["Use resistant varieties.", "Apply fungicides as needed."],
        "Wilt": ["Ensure proper watering.", "Provide adequate nutrients to the soil."],
        "Root Rot": ["Improve soil drainage.", "Avoid overwatering."],
        "Powdery Mildew": ["Apply a sulfur-based fungicide.", "Increase air circulation."]
    }
    
    for key in precautions:
        if key in predicted_disease:
            return predicted_disease, precautions[key]
    
    return predicted_disease, ["No specific precautions found."]

# Streamlit App
st.title("🌱 Crop Recommendation and Disease Prediction")

# Input for soil types
st.subheader("🌾 Soil Type Analysis")
soil_input = st.text_area("Enter soil types (separated by commas):")
soil_types = [soil.strip() for soil in soil_input.split(",") if soil.strip()]

if st.button("🔍 Get Crop Recommendations"):
    if soil_types:
        crop_recommendations = analyze_soil(soil_types)
        for soil, crops in crop_recommendations.items():
            st.subheader(f"✅ Recommended crops for {soil}:")
            st.write(", ".join(crops))
    else:
        st.warning("⚠️ Please enter at least one soil type.")

# Crop Disease Prediction
st.subheader("🦠 Disease Prediction")
all_crops = [
    "Wheat", "Rice", "Maize", "Soybean", "Barley", "Millet", "Sorghum", 
    "Cotton", "Sugarcane", "Sunflower", "Mustard", "Groundnut", "Potato", 
    "Tomato", "Onion", "Garlic", "Chilli", "Cabbage", "Cauliflower", 
    "Brinjal", "Okra", "Spinach", "Lettuce", "Carrot", "Radish", 
    "Cucumber", "Pumpkin", "Watermelon", "Mango", "Orange", "Apple", 
    "Banana", "Grape", "Pineapple", "Papaya", "Strawberry"
]  # A smaller list for dropdown

crop_to_check = st.selectbox("🌿 Select the crop you want to check for disease:", [""] + all_crops)
if st.button("🔬 Check Disease"):
    if crop_to_check:
        predicted_disease, precautions = predict_disease(crop_to_check)
        st.subheader("🦠 Predicted Disease:")
        st.write(predicted_disease)
        st.subheader("🛑 Precautions:")
        st.write(", ".join(precautions))
    else:
        st.warning("⚠️ Please select a crop.")

st.write("🌾 This application provides **crop recommendations** based on soil type and predicts **possible diseases** for crops.")
