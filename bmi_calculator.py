import streamlit as st

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Apply custom CSS for background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("⚖️ BMI Calculator")
st.write("Welcome! Calculate your Body Mass Index (BMI) and get health advice.")

# Sliders for user input
height = st.slider("Select your height (meters):", 0.5, 2.5, 1.70, 0.01)
weight = st.slider("Select your weight (kilograms):", 10, 200, 70, 1)

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.subheader(f"Your BMI is: {bmi:.2f}")

    # Health Status and Tips
    if bmi < 18.5:
        st.warning("🔵 You are **Underweight**.\n\n🍽️ Try to eat more healthy calories and consult a nutritionist.")
    elif 18.5 <= bmi < 24.9:
        st.success("🟢 You have a **Normal weight**.\n\n💪 Keep up the good lifestyle!")
    elif 25 <= bmi < 29.9:
        st.info("🟠 You are **Overweight**.\n\n🥗 Try balanced diets and regular exercise.")
    else:
        st.error("🔴 You are **Obese**.\n\n🏃‍♂️ It's important to exercise and seek professional advice.")

    # Friendly reminder
    st.caption("✨ Remember: BMI is a general guide. Always consult a doctor for professional health advice.")
