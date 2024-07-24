import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# st.write("Hello World")
# # # Title of the app
st.title("Streamlit Basics and Fun with Python 🪄")

# # # # Text and Markdown
st.write("Welcome to the Streamlit Basics tutorial!")
st.markdown("### This tutorial will cover:")
st.markdown("- Basic Python operations")
st.markdown("- Introduction to pandas")
st.markdown("- Basics of Streamlit")
st.markdown("- Simple Data Visualization")

# # # # Section for Basic Python Operations
st.header("🧮📚 Basic Python Operations")

# # # # Adding two numbers
st.subheader("1. Adding Two Numbers")

number1 = st.number_input("Enter the first number", value=0)
number2 = st.number_input("Enter the second number", value=0)
sum_result = number1 + number2

st.write(f"The sum of {number1} and {number2} is **{sum_result}**")

# # # # String concatenation
st.subheader("2. String Concatenation")
string1 = st.text_input("Enter the first Name")
string2 = st.text_input("Enter the second Name")
concat_result = string1 + " " + string2
st.write(f"The Full name is: {concat_result}")

# # # # Introduction to pandas
st.header("🐼 Introduction to pandas")

# # # # Creating a DataFrame
st.subheader("1. Creating a DataFrame")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

st.write("Here's a sample DataFrame:")
st.write(df)

# # # # Descriptive statistics
st.subheader("2. Descriptive Statistics")
st.write("Descriptive statistics of the DataFrame:")
st.write(df.describe())

# # # # Loading a CSV file
st.subheader("3. Loading a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Here's the content of the uploaded CSV file:")
    st.write(df_uploaded)

# # # # Basic Streamlit Components
st.header("🔧 Basic Streamlit Components")

# # # # Buttons
st.subheader("1. Buttons")
if st.button("Classify!"):
    st.write("Hello Students!")

# # # # Selectbox
st.subheader("2. Selectbox")
option = st.selectbox("Choose a number", [1, 2, 3, 4, 5])
st.write(f"You selected: **{option}**")

# # # # Checkbox
st.subheader("3. Checkbox")
if st.checkbox("Show a secret message"):
    st.write("🎉 This is a secret message!")

# # # # Slider
st.subheader("4. Slider")
slider_value = st.slider("Select a value", 0, 100, 20)
st.write(f"Slider value is: **{slider_value}**")

# # # # Text Input
# # # st.subheader("5. Text Input")
# # # name = st.text_input("What's your name?")
# # # st.write(f"Hello, **{name}**!")

# # # # Data Visualization
st.header("📊 Simple Data Visualization")

# # # # Creating a random dataset
st.subheader("1. Scatter Plot")
x = np.random.rand(100)
y = np.random.rand(100)
df_scatter = pd.DataFrame({'x': x, 'y': y})
st.write(df_scatter)

fig_scatter = px.scatter(df_scatter, x='x', y='y', title="Random Scatter Plot")

st.plotly_chart(fig_scatter)

# # Line chart
st.subheader("2. Line Chart")
df_line = pd.DataFrame({
    'x': range(1, 101),
    'y': np.random.randn(100).cumsum()
})

fig_line = px.line(df_line, x='x', y='y', title="Random Line Chart")

st.plotly_chart(fig_line)

# # Bar chart
st.subheader("3. Bar Chart")
df_bar = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'Amount': [10, 15, 7, 20]
})

fig_bar = px.bar(df_bar, x='Fruit', y='Amount', title="Fruit Bar Chart")
st.plotly_chart(fig_bar)

# # # Conclusion
st.write("### Congratulations! You have learned the basics of Streamlit, Python, and pandas.")
st.write("🎉 Now you're ready to build your own data apps!")
