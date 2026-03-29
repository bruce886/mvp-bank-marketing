import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def test_model_accuracy():
    model = joblib.load("./MachineLearning/models/bank_marketing_svm.pkl")
    colunas = joblib.load("./MachineLearning/models/colunas_modelo.pkl")

    url = "https://archive.ics.uci.edu/static/public/222/data.csv"
    df = pd.read_csv(url)

    df.columns = df.columns.str.strip()
    df = df.fillna("unknown")
    df["y"] = df["y"].map({"yes": 1, "no": 0})

    X = df.drop("y", axis=1)
    y = df["y"]

    X = pd.get_dummies(X, drop_first=True)
    X = X.reindex(columns=colunas, fill_value=0)

    y_pred = model.predict(X)
    acc = accuracy_score(y, y_pred)

    assert acc > 0.7