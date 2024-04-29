import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the application with festive emojis
st.title("🎉 Streamlit Research Study Dashboard 🎈")

# Sidebar for user inputs with a colorful header
st.sidebar.header('🌟 Settings')

# Create a sample data frame
data = pd.DataFrame({
    "x": np.arange(1, 101),
    "y": np.random.normal(0, 1, 100)
})

# Add a slider to select a subset of the data with a playful prompt
subset_size = st.sidebar.slider("🎨 Select the number of data points", 10, 100, 50)

# Add a dropdown for selecting plot type with a cheerful prompt
plot_type = st.sidebar.selectbox("📊 Select plot type", ["Line Plot", "Scatter Plot", "Bar Plot", "Histogram"])

# Display the selected plot
fig, ax = plt.subplots()
if plot_type == "Line Plot":
    ax.plot(data["x"][:subset_size], data["y"][:subset_size], "-o")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
elif plot_type == "Scatter Plot":
    ax.scatter(data["x"][:subset_size], data["y"][:subset_size])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
elif plot_type == "Bar Plot":
    ax.bar(data["x"][:subset_size], data["y"][:subset_size])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
elif plot_type == "Histogram":
    sns.histplot(data["y"][:subset_size], kde=True)
    ax.set_xlabel("Y")
    ax.set_ylabel("Frequency")

# Option to save the plot as an image file with a celebratory message
if st.sidebar.button('📸 Save Plot'):
    plot_filename = "plot.png"
    plt.savefig(plot_filename)
    st.sidebar.success(f"🎉 Plot saved as {plot_filename}")

st.pyplot(fig)

# Add a text input for comments or notes with a playful prompt
notes = st.text_area("📝 Add your comments or notes here")

# Add a surprise button for extra fun
if st.button("🎈 Click here for a surprise"):
    st.balloons()
    st.success("🎉 Yay! You found the surprise! 🎈")
