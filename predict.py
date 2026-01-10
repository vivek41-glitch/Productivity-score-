import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("productivity_model.joblib")

# 🎨 Custom CSS for background and styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .big-font {
        font-size:40px !important;
        font-weight: bold;
        text-align: center;
        color: #FFD700;
    }
    .sub-font {
        font-size:18px !important;
        text-align: center;
        color: #DDDDDD;
    }
    label, .stNumberInput label {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }
    .prediction-card {
        padding: 20px;
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.1);
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    }
    footer {
        visibility: hidden;
    }
    .footer-text {
        text-align: center;
        font-size: 14px;
        color: #BBBBBB;
        margin-top: 30px;
    }
    .made-by {
        position: fixed;
        bottom: 10px;
        right: 20px;
        font-size: 13px;
        color: #FFD700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🚀 App Title
st.markdown('<p class="big-font">🚀 Productivity Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">Enter your daily habits and get an AI-driven productivity score</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2910/2910768.png", width=120)  # 🎯 goal icon
st.sidebar.title("📘 About this App")
st.sidebar.write("""
This app predicts your **Productivity Score** based on:
- 💼 Work Hours  
- 🏋️ Exercise Time  
- 😴 Sleep Hours  
- 📱 Screen Time  

Model trained using **Machine Learning (scikit-learn)**.  
""")
st.sidebar.markdown("[🌐 View on GitHub](https://github.com/yourusername/productivity-predictor)")

# Input Section
st.subheader("📝 Input Your Daily Routine")

col1, col2 = st.columns(2)

with col1:
    work_hours = st.number_input("💼 Daily Work Hours", 0, 16, 8)
    exercise_hours = st.number_input("🏋️ Daily Exercise (minutes)", 0, 180, 30)

with col2:
    sleep_hours = st.number_input("😴 Daily Sleep Hours", 0, 12, 7)
    screen_time = st.number_input("📱 Screen Time (hours)", 0, 16, 5)

# Predict Button
if st.button("✨ Predict Productivity", use_container_width=True):
    features = np.array([[work_hours, exercise_hours, sleep_hours, screen_time]])
    prediction = model.predict(features)

    st.markdown(
        f"""
        <div class="prediction-card">
            <h2>✅ Your Predicted Productivity Score:</h2>
            <h1 style="color:#FFD700;">{prediction[0]:.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown('<div class="footer-text">⚡ Built with Streamlit & Scikit-learn</div>', unsafe_allow_html=True)
st.markdown('<div class="made-by">👨‍💻 Made by Vivek</div>', unsafe_allow_html=True)
