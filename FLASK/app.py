# app.py
import pandas as pd
import pickle
import statsmodels.api as sm
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)  
CORS(app)

def open_model():
    with open('random_forest_model.pkl', 'rb') as f:
        artifact = pickle.load(f)

        return artifact
    
def prepare_input_for_model(raw_input: dict) -> dict:
    # Mapping from string to integer for categorical fields
    mapping = {
        'tipo': {'Evento': 0, 'Turistico': 1, 'Ativacao': 2, 'Social': 3},
        'clima': {'ensolarado': 0, 'nublado': 1, 'frio': 2, 'chuvoso': 3},
        'tema': {'Festivo': 0, 'Turismo': 1, 'Diversidade': 2, 'Social': 3, 'Noticias': 4, 'Comunidade': 5},
        'sentimento': {'neutro': 0, 'positivo': 1, 'negativo': 2},
        'edicao_repetida': {'Sim': 0, 'Nao': 1},
        'resultado_anterior': {'bom': 0, 'ruim': 1, 'nao se aplica': 2, 'excelente': 3},
    }

    encoded = {
        'tipo': mapping['tipo'].get(raw_input.get('tipo'), -1),
        'tema': mapping['tema'].get(raw_input.get('tema'), -1),
        'clima': mapping['clima'].get(raw_input.get('clima'), -1),
        'sentimento': mapping['sentimento'].get(raw_input.get('sentimento'), -1),
        'edicao_repetida': mapping['edicao_repetida'].get(raw_input.get('edicao_repetida'), -1),
        'resultado_anterior': mapping['resultado_anterior'].get(raw_input.get('resultado_anterior'), -1),
        'investimento': raw_input.get('investimento', 0),
        'inovacao': raw_input.get('inovacao', 0),
    }

    return encoded



@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    data_encoded = prepare_input_for_model(data)
    df = pd.DataFrame([data_encoded])
    df_reordered = df[['tipo', 'tema', 'clima', 'investimento', 'sentimento', 'edicao_repetida', 'resultado_anterior', 'inovacao']]
    model = open_model()
    prediction = model.predict(df_reordered)[0]
    pred_class = int(prediction > 0.9)

    result_label = "success" if pred_class == 1 else "fail"
    return {
        "message": "Data Received",
        "Predicted probability of sucesso": f"{prediction:.4f}",
        "Prediction": result_label
    }, 200

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)
