from flask import Flask
from api import Api

app = Flask(__name__)
app.config.update(DEBUG=True)

app.register_blueprint(Api, url_prefix='/user')

@app.route('/')
def hello_world():
        data = {"id": 5, "title": "Myworld"}
        return jsonify(**data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)
