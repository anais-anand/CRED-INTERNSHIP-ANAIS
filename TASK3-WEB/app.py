from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__, template_folder="template")

model = pickle.load(open('titan.pkl', 'rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    p = request.form["rd"]
    q = request.form["as"]
    a = request.form["ag"]
    b = request.form["ss"]
    c = request.form["ph"]
    d = request.form["fe"]

    s = request.form["s"]
    if s == "y":
        s = 1
    else:
        s = 0.5

    t = [[float(p), float(q), float(a), float(b), float(c), float(d), float(s)]]
    output = model.predict(t)
    print(output)

    return render_template("index.html", y="The prediction is  " + str(np.round(output[0])))

if __name__ == '__main__':
    app.run(debug=True)
