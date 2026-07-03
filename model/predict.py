import pickle
import pandas as pd
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)
def predict_output(data_input: dict) -> str:
    data = pd.DataFrame([data_input])
    prediction = model.predict(data)[0]
    return prediction