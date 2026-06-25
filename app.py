from flask import Flask, render_template, request
import subprocess
import sys
import pandas as pd
from Customer_Churn.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)
@app.route('/',methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route('/train', methods = ['GET'])
def training():
    result = subprocess.run(["python", "main.py"])
    return "Training Successuful!"

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        data = {
            "credit_score": int(request.form["credit_score"]),
            "country": request.form["country"],
            "gender": request.form["gender"],
            "age": int(request.form["age"]),
            "tenure": int(request.form["tenure"]),
            "balance": float(request.form["balance"]),
            "products_number": int(request.form["products_number"]),
            "credit_card": int(request.form["credit_card"]),
            "active_member": int(request.form["active_member"]),
            "estimated_salary": float(request.form["estimated_salary"])
        }

        df = pd.DataFrame([data])

        obj = PredictionPipeline()
        prediction = obj.predict(df)

        if prediction[0] == 1:
            result = "Warning: High Risk of Attrition"
        else:
            result = "Secure: Customer is Likely to Stay"

        return render_template("index.html", prediction_text=result)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
