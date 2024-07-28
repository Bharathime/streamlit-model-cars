import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title
st.title("Model Cars Data Visualization")

# Add a header image from an online URL
st.image("https://w0.peakpx.com/wallpaper/234/744/HD-wallpaper-cars-car-d-sward-king.jpg", use_column_width=True)

# Introduction
st.markdown("""
### Welcome to the Model Cars Data Visualization App!
Explore and interact with various datasets related to model cars.
""")

# Sample data with online image URLs
data = {
    "brand": ["Ferrari", "Porsche", "Lamborghini", "Mercedes-Benz", "BMW"],
    "model": ["488 GTB", "911 Carrera", "Aventador", "AMG GT", "M4"],
    "price": [300000, 100000, 400000, 150000, 80000],
    "horsepower": [670, 450, 730, 523, 473],
    "image_url": [
        "https:/https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cdni.autocarindia.com/ExtraImages/20231026071351_asdfghjkl.jpg&w=700&c=1",
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

# Add a footer image from an online URL
st.image("https://i.pinimg.com/736x/ff/51/de/ff51de001cf7ff9c77b8402b8b9f9d52.jpg", use_column_width=True)

# Background Image (Optional)
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("https://i.pinimg.com/736x/f1/0e/19/f10e1991a7834ee7c9655c7250a4d8da.jpg");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
