from flask import Flask, jsonify
from user_api import user_api

app = Flask(__name__)
app.config.update(DEBUG=True)

app.register_blueprint(user_api)

@app.route('/')
def hello_world():
        data = {"id": 5, "title": "Myworld"}
        return jsonify(**data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)
