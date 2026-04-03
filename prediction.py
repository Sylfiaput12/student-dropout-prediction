import joblib

# load model & encoder (sekali saja saat app dijalankan)
model = joblib.load("model/rf_model.joblib")
encoder_target = joblib.load("model/encoder_target.joblib")


def prediction(data):
    """
    Function untuk prediksi status mahasiswa

    Args:
        data (DataFrame): data yang sudah dipreprocessing

    Returns:
        tuple: (label hasil prediksi, probability)
    """

    # prediksi (hasil angka)
    result = model.predict(data)

    # probability
    proba = model.predict_proba(data)

    # ubah ke label asli
    final_result = encoder_target.inverse_transform(result)

    return final_result[0], proba[0]
