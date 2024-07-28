import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title
st.title("Model Cars Data Visualization")

# Add a header image
st.image("/Users/bharathit/Desktop", use_column_width=True)

# Introduction
st.markdown("""
### Welcome to the Model Cars Data Visualization App!
Explore and interact with various datasets related to model cars.
""")

# Sample data similar to what might be scraped from the provided website
data = {
    "brand": ["Ferrari", "Porsche", "Lamborghini", "Mercedes-Benz", "BMW"],
    "model": ["488 GTB", "911 Carrera", "Aventador", "AMG GT", "M4"],
    "price": [300000, 100000, 400000, 150000, 80000],
    "horsepower": [670, 450, 730, 523, 473],
    "image_url": [
        "/Users/bharathit/Desktop",
        "/Users/bharathit/Desktop",
        "/Users/bharathit/Desktop",
        "/Users/bharathit/Desktop",
        "/Users/bharathit/Desktop"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (if needed for future use)
df.to_csv("model_cars_data.csv", index=False)

# Display the data
st.write(df)

# Add an interactive Plotly chart
fig = px.scatter(df, x='price', y='horsepower', color='brand', title="Price vs Horsepower")
st.plotly_chart(fig)

# Optional image display
for index, row in df.iterrows():
    if st.checkbox(f"Show image of {row['brand']} {row['model']}"):
        st.image(row['image_url'], caption=f"{row['brand']} {row['model']}", use_column_width=True)

# Add a footer image
st.image("/Users/bharathit/Desktop", use_column_width=True)

# Background Image (Optional)
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("/Users/bharathit/Desktop");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
