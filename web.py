from flask import Flask
from flask import render_template

import client

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/machines')
def machines():
    c = client.Client()
    machines = c.get_machines()
    return render_template('machines.html', machines=machines)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
