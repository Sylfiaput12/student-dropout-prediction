import joblib

# load model
model = joblib.load("model/rf_model.joblib")

# load encoder target
encoder_target = joblib.load("model/encoder_target.joblib")


def prediction(data):
    """
    Function untuk prediksi status mahasiswa
    """

    # prediksi (hasilnya angka)
    result = model.predict(data)

    # balik ke label asli
    final_result = encoder_target.inverse_transform(result)

    return final_result[0]
