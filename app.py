import streamlit as st
import pandas as pd
import joblib

st.title("Student Dropout Early Warning System")

# Load the trained model
model = joblib.load("model.joblib")

file = st.file_uploader("Upload student data CSV", type="csv")

if file:
    df = pd.read_csv(file)
    probs = model.predict_proba(df)[:, 1]

    df['risk_score'] = probs
    df['risk_label'] = df['risk_score'].apply(lambda x: 'High' if x >= 0.7 else 'Medium' if x >= 0.4 else 'Low')
    df['predicted_dropout'] = (df['risk_score'] >= 0.3).astype(int)

    st.subheader("🚨 High Risk Students")
    st.dataframe(df[df['risk_label'] == 'High'])
