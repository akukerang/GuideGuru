from flask import Flask, render_template
import config
api_key = config.API_KEY
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html',api_key = api_key)



app.run()