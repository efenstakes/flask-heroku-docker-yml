import os
from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/')
def index():
    return { 'page': [ 'index', 'home' ] }

@app.route('/about')
def about():
    return { 'page': 'about' }



PORT = os.environ.get('PORT', 5000)

if __name__ == "__main__":
    app.run( host='0.0.0.0', port=PORT )