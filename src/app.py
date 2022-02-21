import torch
from flask import request
from flask import Flask, render_template
from detoxify import Detoxify

app = Flask(__name__)

# model = torch.load("models/model.pt")
# model = torch.hub.load('unitaryai/detoxify','toxic_bert')
model = Detoxify('original')


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def results():

    if request.method == 'POST':
        text = request.form['inputedText']
        predictions =  model.predict(text)
        return 'Hola {}'.format(predictions) # render_template('index.html', predictions=pred)






if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
