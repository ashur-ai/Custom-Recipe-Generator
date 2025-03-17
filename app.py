from boltiotai import openai
import streamlit as st
import os

# Set OpenAI API Key securely
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to generate the recipe
def generate_recipe(components):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {
                "role": "user",
                "content": f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"
            }
        ]
    )
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("Custom Recipe Generator 🍽️")
st.write("Enter the ingredients you have, and I will generate a recipe for you!")

# User input
components = st.text_input("Enter ingredients (comma separated)", "")

# Button to generate recipe
if st.button("Generate Recipe"):
    if components:
        with st.spinner("Cooking up something delicious... 🍳"):
            output = generate_recipe(components)
            st.success("Here is your recipe!")
            st.text_area("Generated Recipe", output, height=300)
    else:
        st.warning("Please enter at least one ingredient.")
