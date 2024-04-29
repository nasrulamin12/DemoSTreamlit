import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the application
st.title("🚀 Welcome to the Streamlit Research Explorer 🌟")

# Create a sample data frame
data = pd.DataFrame({"x": np.arange(1, 101), "y": np.random.normal(0, 1, 100)})

# Add a slider to select a subset of the data
subset_size = st.slider("📊 Select the number of data points to explore", 10, 100, 50)

# Choose the type of graph to display
graph_type = st.selectbox(
    "📈 Select the type of graph", ["Line Plot", "Scatter Plot", "Bar Chart"]
)

# Display the selected graph based on the chosen type
fig, ax = plt.subplots()
if graph_type == "Line Plot":
    ax.plot(data["x"][:subset_size], data["y"][:subset_size], "-o", color="skyblue")
elif graph_type == "Scatter Plot":
    ax.scatter(data["x"][:subset_size], data["y"][:subset_size], color="orange")
elif graph_type == "Bar Chart":
    ax.bar(data["x"][:subset_size], data["y"][:subset_size], color="green")
ax.set_title(f"📊 {graph_type}")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
st.pyplot(fig)

# Add a fun fact based on the data
average_y = np.mean(data["y"][:subset_size])
st.info(f"🧠 Fun Fact: The average value of Y in this subset is {average_y:.2f}")

# Add a text input for comments or notes
notes = st.text_area("📝 Add your comments, thoughts, or discoveries here")

# Display a word cloud of the notes
if notes:
    st.subheader("🌈 Your Thoughts in a Word Cloud")
    # Generate a word cloud
    from wordcloud import WordCloud

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        notes
    )
    st.image(wordcloud.to_array())

# Add a surprise button for extra fun
if st.button("🎉 Click here for a surprise"):
    st.balloons()
    st.success("🎈 Yay! You found the surprise!")
