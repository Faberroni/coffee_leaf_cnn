from flask import jsonify
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    
    return('<h>Hello world</h>')

