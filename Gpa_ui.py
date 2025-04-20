import streamlit as st
import pickle
import requests

st.set_page_config(page_title="GPA Predictor", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎓 GPA Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict your GPA based on your SAT score 📚</div>', unsafe_allow_html=True)

sat_score = st.number_input("Enter your SAT Score:", min_value=0, max_value=6000, value=1000, step=10)

if st.button("🎯 Predict My GPA"):
    url = "http://127.0.0.1:5000/predict_gpa"
    payload = {"sat_score": sat_score}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            res = response.json()["predicted_gpa"]
            st.success(f"✅ Your Predicted GPA is: **{res:.2f}**")
    
            if res >= 3.5:
                st.balloons()
                st.info("🌟 Excellent! Keep up the great work!")
            elif res >= 3.0:
                st.info("👍 Good job! A little more effort can make it even better!")
            elif res >= 2.0:
                st.warning("📚 You're doing okay, but consider focusing more on studies.")
            else:
                st.error("💡 Don't worry! Stay consistent and seek help if needed. You can do it! 🚀")

    except Exception as e:
        st.error(f"⚠️ Error connecting to server: {e}")

st.markdown("---")
