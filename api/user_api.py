from flask import Blueprint, jsonify
from corp_api import corp_api
import MySQLdb as mdb
import sys
import json

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')
user_api = Blueprint('user_api', __name__)

@user_api.route('/user/')
def get_users():
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id, username, email FROM user")
		rows = cur.fetchall()
		return jsonify(users = rows)

@user_api.route('/user/<int:id>')
def get_users_by_id(id):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE id = %s", id)
                row = cur.fetchone()
                row['corp'] = corp_api.get_corp_for_user_id(row['id'])
                return jsonify(users = row)

@user_api.route('/user/<string:username>')
def get_users_by_name(username):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE username = %s", username)
                row = cur.fetchone()
                row['corp'] = corp_api.get_corp_for_user_id(row['id'])
                return jsonify(users = row)