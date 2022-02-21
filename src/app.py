#import torch
from flask import Flask, render_template
# from detoxify import Detoxify

app = Flask(__name__)


#model = torch.load("models/model.pt")


@app.route('/')
def homepage():
    #pred = model.predict('You suck! You fuckin cunt')
    return render_template('index.html')

# @app.route('/results')
# def results():
#     pred = model.predict('You suck! You fuckin cunt')
#     return render_template('index.html', predictions=pred)






if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
