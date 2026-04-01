import streamlit as st
import pandas as pd

from data_preprocessing import data_preprocessing
from prediction import prediction

# Streamlit App
st.set_page_config(page_title="Student Dropout Prediction", layout="centered")

st.title("🎓 Student Dropout Prediction")
st.write("Predict apakah mahasiswa akan Dropout, Enrolled, atau Graduate")

# input form

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

course_dict = {
    "Management": 9147,
    "Management (Evening)": 9991,
    "Nursing": 9500,
    "Journalism and Communication": 9773,
    "Tourism": 9254,
    "Advertising and Marketing Management": 9670,
    "Informatics Engineering": 9119,
    "Veterinary Nursing": 9085,
    "Agronomy": 9003,
    "Basic Education": 9853,
}

course_label = st.selectbox("Course", list(course_dict.keys()))
course = course_dict[course_label]

# Age
age = st.number_input("Age", min_value=15, max_value=70, value=20)

#  Debtor
debtor = st.selectbox("Debtor", ["Yes", "No"])
debtor = 1 if debtor == "Yes" else 0

# Marital Status
marital_dict = {"Single": 1, "Married": 2, "Divorced": 3, "Widowed": 4}

marital_label = st.selectbox("Marital Status", list(marital_dict.keys()))
marital = marital_dict[marital_label]

# Scholarship (MAP KE ANGKA)
scholarship = st.selectbox("Scholarship", ["Yes", "No"])
scholarship = 1 if scholarship == "Yes" else 0

# Tuition (MAP KE ANGKA)
tuition = st.selectbox("Tuition Status", ["Up to date", "Not paid"])
tuition = 1 if tuition == "Up to date" else 0

#  Admission Grade
admission_grade = st.number_input(
    "Admission Grade", min_value=0.0, max_value=200.0, value=120.0
)

# Inflation
inflation = st.number_input("Inflation Rate", min_value=-5.0, max_value=10.0, value=2.0)

# Create DataFrame untuk input model
input_data = pd.DataFrame(
    {
        "Gender": [gender],
        "Course": [course],
        "Age": [age],
        "Debtor": [debtor],
        "Marital_status": [marital],
        "Scholarship": [scholarship],
        "Tuition": [tuition],
        "Admission_grade": [admission_grade],
        "Inflation_rate": [inflation],
    }
)

# PREDIKSI
if st.button("Predict"):

    processed_data = data_preprocessing(input_data)

    # Prediksi class
    result = prediction(processed_data)

    # Ambil probability
    import joblib

    model = joblib.load("model/rf_model.joblib")
    proba = model.predict_proba(processed_data)[0]

    st.subheader("Prediction Result:")

    if result == "Dropout":
        st.error("⚠️ Dropout Risk")
    elif result == "Enrolled":
        st.warning("📚 Still Enrolled")
    else:
        st.success("🎓 Graduate")

    # Tampilkan probability
    st.subheader("Prediction Probability:")

    st.write(f"Dropout: {proba[0]*100:.2f}%")
    st.write(f"Enrolled: {proba[1]*100:.2f}%")
    st.write(f"Graduate: {proba[2]*100:.2f}%")
