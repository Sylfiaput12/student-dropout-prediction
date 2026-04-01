import joblib
import pandas as pd


# load encoder
encoder_course = joblib.load("model/encoder_Course.joblib")
encoder_marital = joblib.load("model/encoder_Marital_status.joblib")


# load scaler

scaler_age = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_admission = joblib.load("model/scaler_Admission_grade.joblib")
scaler_inflation = joblib.load("model/scaler_Inflation_rate.joblib")


def data_preprocessing(data):

    df = pd.DataFrame()

    # mapping

    df["Gender"] = data["Gender"]  # 1 = Male, 0 = Female
    df["Debtor"] = data["Debtor"]  # 1 = Yes, 0 = No
    df["Scholarship_holder"] = data["Scholarship"]  # 1 = Yes, 0 = No
    df["Tuition_fees_up_to_date"] = data["Tuition"]  # 1 = Up to date, 0 = Not paid

    # Encoding
    df["Course"] = data["Course"]
    df["Marital_status"] = data["Marital_status"]

    # Scaling
    df["Age_at_enrollment"] = scaler_age.transform(data[["Age"]])
    df["Admission_grade"] = scaler_admission.transform(data[["Admission_grade"]])
    df["Inflation_rate"] = scaler_inflation.transform(data[["Inflation_rate"]])

    df = df[
        [
            "Gender",
            "Course",
            "Age_at_enrollment",
            "Debtor",
            "Marital_status",
            "Scholarship_holder",
            "Tuition_fees_up_to_date",
            "Admission_grade",
            "Inflation_rate",
        ]
    ]

    return df
