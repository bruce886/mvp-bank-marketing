from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, send_from_directory
from flask_cors import CORS
import pandas as pd
import joblib
import os

from logger import logger
from schemas import ClienteSchema, PredicaoViewSchema, ErrorSchema

info = Info(
    title="API - Previsão de Adesão a Depósito Bancário",
    version="1.0.0"
)

app = OpenAPI(
    __name__,
    info=info,
    static_folder="../front",
    static_url_path="/front"
)

CORS(app)

home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação da API"
)

predicao_tag = Tag(
    name="Predição",
    description="Predição de adesão a depósito bancário"
)


@app.get("/", tags=[home_tag])
def home():
    """Serve o frontend principal."""
    return send_from_directory("../front", "index.html")


@app.get("/docs", tags=[home_tag])
def docs():
    """Redireciona para a documentação OpenAPI."""
    return redirect("/openapi")


@app.post(
    "/predict",
    tags=[predicao_tag],
    responses={
        "200": PredicaoViewSchema,
        "400": ErrorSchema,
    },
)
def predict(body: ClienteSchema):
    """
    Realiza a predição de adesão a depósito bancário
    com base nos dados enviados pelo usuário.
    """
    try:
        input_data = {
            "age": body.age,
            "job": body.job,
            "marital": body.marital,
            "education": body.education,
            "default": body.default,
            "balance": body.balance,
            "housing": body.housing,
            "loan": body.loan,
            "contact": body.contact,
            "day": body.day,
            "month": body.month,
            "duration": body.duration,
            "campaign": body.campaign,
            "pdays": body.pdays,
            "previous": body.previous,
            "poutcome": body.poutcome,
        }

        df = pd.DataFrame([input_data])
        df = pd.get_dummies(df)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        colunas_path = os.path.join(base_dir, "MachineLearning", "models", "colunas_modelo.pkl")
        modelo_path = os.path.join(base_dir, "MachineLearning", "models", "bank_marketing_svm.pkl")

        colunas_modelo = joblib.load(colunas_path)
        df = df.reindex(columns=colunas_modelo, fill_value=0)

        modelo = joblib.load(modelo_path)

        predicao = int(modelo.predict(df)[0])

        probabilidade = None
        if hasattr(modelo, "predict_proba"):
            try:
                probabilidade = float(modelo.predict_proba(df)[0][1])
            except Exception:
                probabilidade = None

        resultado = {
            "prediction": predicao,
            "classe": "Sim" if predicao == 1 else "Não",
            "probability": probabilidade
        }

        logger.info(f"Predição realizada com sucesso: {resultado}")
        return resultado, 200

    except FileNotFoundError as e:
        logger.error(f"Arquivo não encontrado: {str(e)}")
        return {"message": f"Arquivo não encontrado: {str(e)}"}, 400

    except Exception as e:
        logger.error(f"Erro ao realizar predição: {str(e)}")
        return {"message": f"Não foi possível realizar a predição: {str(e)}"}, 400


if __name__ == "__main__":
    app.run(debug=True)