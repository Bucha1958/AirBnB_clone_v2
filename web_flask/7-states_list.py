#!/usr/bin/python3
from flask import Flask, jsonify, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/api/data', methods=['GET'])
def get_data():
    data = storage.all()
    return jsonify(data)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State').values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
