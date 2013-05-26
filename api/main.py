from flask import Flask, jsonify
import MySQLdb as mdb
import sys
import json

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main'); 
app = Flask(__name__)
app.config.update(DEBUG=True)
@app.route('/')
def hello_world():
        data = {"id": 5, "title": "Myworld"}
        return jsonify(**data)

@app.route('/user/')
def get_users():
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id, username, email FROM user")
		rows = cur.fetchall()
		return jsonify(users = rows)

@app.route('/user/<int:id>')
def get_users_by_id(id):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE id = %s", id)
                rows = cur.fetchall()
                return jsonify(users = rows)

@app.route('/user/<string:username>')
def get_users_by_name(username):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE username = %s", username)
                rows = cur.fetchall()
                return jsonify(users = rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)
