import numpy as np
from flask import Flask, request, jsonify, render_template
from googletrans import Translator
translater = Translator(service_urls=['translate.googleapis.com'])


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/testcasepredict',methods=['POST'])
def testcasepredict():
    int_features = [x for x in request.form.values()][0]
    print(int_features)
    out = translater.translate(int_features[0],dest=int_features[1])
    print(out.text)

    return render_template('index.html', prediction_testcase='Translated text :  {}'.format(out.text))


if __name__ == "__main__":
    app.run(debug=True)