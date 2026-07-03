from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output
from schema.user_input import UserInput



app = FastAPI()



@app.get('/')
def hello():
    return {'message': 'Insurance Premium Prediction API'}

@app.get('/health')
def health():
    return {'status': 'OK'}

@app.post('/predict')
def predict_premium(data: UserInput):
    input_data = {
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier
        }
    try:
        prediction = predict_output(input_data)    
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
