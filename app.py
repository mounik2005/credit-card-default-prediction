import streamlit as st
import numpy as np
import pickle

# Title
st.title("💳 Credit Default Prediction App")

st.write("Enter customer details:")

# ---------------- BASIC INFO ----------------
LIMIT_BAL = st.number_input("Credit Limit", value=50000)
SEX = st.selectbox("Sex (1=Male, 2=Female)", [1, 2])
EDUCATION = st.selectbox("Education (1=Graduate, 2=University, 3=High School, 4=Others)", [1,2,3,4])
MARRIAGE = st.selectbox("Marriage (1=Married, 2=Single, 3=Others)", [1,2,3])
AGE = st.number_input("Age", value=25)

# ---------------- REPAYMENT STATUS ----------------
st.subheader("Repayment History (last 6 months)")
PAY_0 = st.number_input("PAY_0 (Last Month)", value=0)
PAY_2 = st.number_input("PAY_2", value=0)
PAY_3 = st.number_input("PAY_3", value=0)
PAY_4 = st.number_input("PAY_4", value=0)
PAY_5 = st.number_input("PAY_5", value=0)
PAY_6 = st.number_input("PAY_6", value=0)

# ---------------- BILL AMOUNTS ----------------
st.subheader("Bill Amounts")
BILL_AMT1 = st.number_input("BILL_AMT1", value=20000)
BILL_AMT2 = st.number_input("BILL_AMT2", value=20000)
BILL_AMT3 = st.number_input("BILL_AMT3", value=20000)
BILL_AMT4 = st.number_input("BILL_AMT4", value=20000)
BILL_AMT5 = st.number_input("BILL_AMT5", value=20000)
BILL_AMT6 = st.number_input("BILL_AMT6", value=20000)

# ---------------- PAYMENT AMOUNTS ----------------
st.subheader("Payment Amounts")
PAY_AMT1 = st.number_input("PAY_AMT1", value=5000)
PAY_AMT2 = st.number_input("PAY_AMT2", value=5000)
PAY_AMT3 = st.number_input("PAY_AMT3", value=5000)
PAY_AMT4 = st.number_input("PAY_AMT4", value=5000)
PAY_AMT5 = st.number_input("PAY_AMT5", value=5000)
PAY_AMT6 = st.number_input("PAY_AMT6", value=5000)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model (2).pkl", "rb"))

# ---------------- PREDICTION ----------------
if st.button("Predict"):

    input_data = np.array([[ 
        LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE,
        PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
        BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
        PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk: Customer likely to default")
    else:
        st.success("✅ Low Risk: Customer not likely to default")