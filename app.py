from flask import Flask, request, render_template
from markupsafe import escape
import pickle

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods = ['GET','POST'])
def prediction():
    if request.method == "POST":
        news = request.form['news']
        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("prediction.html",prediction_text = "News headline is -> {}".format(predict))

    else:
        return render_template("prediction.html")

if __name__ == '__main__':
    app.run()