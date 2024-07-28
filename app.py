import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title
st.title("Model Cars Data Visualization")


# Introduction
st.markdown("""
### Welcome to the Model Cars Data Visualization App!
Explore and interact with various datasets related to model cars.
""")

# Sample data with online image URLs
data = {
    "brand": ["Ferrari", "Porsche", "Lamborghini", "Mercedes-Benz", "BMW"],
    "model": ["488 GTB", "911 Carrera", "Aventador", "AMG GT", "M4"],
    "price": [5000, 7500, 4000, 4700, 4800],
    "image_url": [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRmJ-LUhs89TlmhCcvsO2kiVIvRWXiczf5dg&s",
        "https://files.porsche.com/filestore/image/multimedia/none/992-gt3-rs-modelimage-sideshot/model/cfbb8ed3-1a15-11ed-80f5-005056bbdc38/porsche-model.png",
        "https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_detail/few_off/sian-fkp-37/2022/06_20/over/sian_body_01.jpg",
        "https://www.motortrend.com/uploads/sites/10/2023/07/2023-mercedes-benz-s-class-580-maybach-sedan-angular-front.png",
        "https://www.bmw.in/content/dam/bmw/common/topics/offers-and-services/bmw-special-sales-2020/protection-vehicle/bmw-css-7-series-protection-ms-new-standard.jpg"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the data
st.write(df)

# Add an interactive Plotly chart
fig = px.scatter(df, x='price', y='horsepower', color='brand', title="Price vs Horsepower")
st.plotly_chart(fig)

# Optional image display
for index, row in df.iterrows():
    if st.checkbox(f"Show image of {row['brand']} {row['model']}"):
        st.image(row['image_url'], caption=f"{row['brand']} {row['model']}", use_column_width=True)


# Background Image (Optional)
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("https://i.pinimg.com/736x/2e/96/65/2e96651aa1d65a128847b36e06b27c01.jpg");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
