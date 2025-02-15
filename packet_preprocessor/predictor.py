import joblib
from tensorflow.keras.models import load_model

# Load the models
# model = load_model('ARP_MODEL.h5')
# scaler = joblib.load('ARP_MitM_scaler.pkl')
# pca = joblib.load('ARP_MitM_pca.pkl')
model = load_model("fuzzing.h5")
scaler = joblib.load("fuzzing_scaler.pkl")
pca = joblib.load("fuzzing_pca.pkl")


def predict(x):
    x_scaled = scaler.transform(x)
    x_pca = pca.transform(x_scaled)

    # Perform inference
    prediction = model.predict(x_pca)

    # Print or return the prediction
    print(prediction)
