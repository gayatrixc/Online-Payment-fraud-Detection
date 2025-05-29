# app.py
import streamlit as st
from predict import model_prediction

st.set_page_config(page_title="Fraud Detection App", layout="centered")
st.title("💳 Online Payment Fraud Detection")
st.markdown("Enter the transaction details below to check for fraud.")

# Input form
with st.form("fraud_form"):
    step = st.number_input("Step (Transaction Time)", min_value=0)
    typeup = st.number_input("Type (Transaction Type Encoded)", min_value=0)
    amount = st.number_input("Transaction Amount", min_value=0.0)
    nameOrig = st.number_input("NameOrig (Customer ID Encoded)", min_value=0)
    oldbalanceOrg = st.number_input("Old Balance (Customer)", min_value=0.0)
    newbalanceOrig = st.number_input("New Balance (Customer)", min_value=0.0)
    nameDest = st.number_input("NameDest (Merchant ID Encoded)", min_value=0)
    oldbalanceDest = st.number_input("Old Balance (Merchant)", min_value=0.0)
    newbalanceDest = st.number_input("New Balance (Merchant)", min_value=0.0)
    isFlaggedFraud = st.number_input("Is Flagged Fraud (0 or 1)", min_value=0, max_value=1)
    
    submit = st.form_submit_button("🔍 Predict")

if submit:
    features = [[step, typeup, amount, nameOrig, oldbalanceOrg, newbalanceOrig,
                 nameDest, oldbalanceDest, newbalanceDest, isFlaggedFraud]]
    
    result = model_prediction(features)
    
    if "1" in result:
        st.error("⚠️ Alert: Fraudulent Transaction Detected!")
    else:
        st.success("✅ Safe Transaction: No Fraud Detected.")
