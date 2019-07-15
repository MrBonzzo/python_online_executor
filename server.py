#!/usr/bin/env python3


from configparser import ConfigParser
from executor import run
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms import CodeForm
import json


app = Flask(__name__)
configuration = ConfigParser()
configuration.read('configuration.ini')
app.config['SECRET_KEY'] = configuration['server']['secret_key']
timeout = float(configuration['server']['timeout'])
csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/')
def main_page():
    form = CodeForm()
    return render_template('index.html', form=form)


@app.route('/launch', methods=['POST'])
def launch():
    code = request.form['code']
    input_ = request.form['stdin']
    execution_result = run(code, input_, timeout)
    return json.dumps(execution_result)


if __name__ == '__main__':
    app.run(debug=True)
