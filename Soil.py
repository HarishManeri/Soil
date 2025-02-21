import streamlit as st
import random

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
st.title("Crop Recommendation and Disease Prediction based upon soil")

# Input for soil types
num_soil_types = st.number_input("Enter the number of soil types you want to analyze (at least 1):", min_value=1)
soil_types = []

for i in range(num_soil_types):
    soil_type = st.text_input(f"Enter soil type {i + 1}:")
    if soil_type:
        soil_types.append(soil_type)

if st.button("Get Crop Recommendations"):
    if soil_types:
        crop_recommendations = analyze_soil(soil_types)
        for soil, crops in crop_recommendations.items():
            st.subheader(f"Recommended crops for {soil}:")
            st.write(", ".join(crops))

# Input for crop disease prediction
crop_to_check = st.text_input("Enter the crop you want to check for disease:")
if st.button("Check Disease"):
    if crop_to_check:
        predicted_disease, precautions = predict_disease(crop_to_check)
        st.subheader("Predicted Disease:")
        st.write(predicted_disease)
        st.subheader("Precautions:")
        st.write(", ".join(precautions))

# Run the Streamlit app
if __name__ == "__main__":
    st.write("This application provides crop recommendations based on soil types and predicts diseases for specific crops.")
