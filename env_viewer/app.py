from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    env_vars = dict(os.environ)
    return render_template('index.html', env_vars=env_vars)

if __name__ == '__main__':
    app.run(debug=True)
