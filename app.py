import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.title("Model Cars Collection")
st.write("Explore various model cars in our collection.")

# Sample data
data = {
    'Model': ['Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'],
    'Price': [250, 300, 450, 500, 350],
    'Rating': [4.5, 4.7, 4.6, 4.8, 4.7]
}

df = pd.DataFrame(data)

# Display data
st.write("## Car Models Data")
st.dataframe(df)

# Interactive widgets
st.write("## Filter Models")
max_price = st.slider("Max Price", 0, 500, 300)
filtered_df = df[df['Price'] <= max_price]

st.write(f"Models with price below {max_price}:")
st.dataframe(filtered_df)

# Data visualization
st.write("## Price Distribution")
fig, ax = plt.subplots()
ax.hist(df['Price'], bins=5)
st.pyplot(fig)


