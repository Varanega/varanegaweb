from flask import Flask, redirect, render_template, url_for
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('.env')

app.debug = config['DEFAULT']['DEBUG']
app.secret_key = config['DEFAULT']['SECRET_KEY']

@app.route("/")
def index():
    return render_template(items/index.html)

if __name__ == "__main__":
    app.run()