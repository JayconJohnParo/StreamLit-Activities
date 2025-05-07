import streamlit as st

# App title and intro
st.title("🌟 Welcome to Streamlit!")
st.header("🎉 Kickstart Your First Streamlit App")
st.write("👇 Use the inputs below and see how the app responds instantly!")

# Input fields
name = st.text_input("📝 Enter your name:")
number = st.number_input("🎂 Enter your age:", step=1)

# Conditional output
if name:
    st.success(f"Hello, {name}!")
    st.info(f"You are {number} years old")
else:
    st.warning("⚠️ Please enter your name above.")
