from flask import Flask, render_template, request
import joblib
import numpy as np


app = Flask(__name__, template_folder='webapp/templates')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():

    loaded_model = joblib.load('artifacts/model_training/model.joblib')
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))

        to_predict = np.array(to_predict_list).reshape(1, len(to_predict_list))
        result = loaded_model.predict(to_predict)

    if (int(result) == 1):
        prediction = "Sorry! it seems getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("index.html", prediction_text=prediction))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
