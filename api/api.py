from flask import Blueprint, jsonify
import MySQLdb as mdb
import sys
import json

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main'); 
Api= Blueprint('Api', __name__)


@Api.route('/user/')
def get_users():
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id, username, email FROM user")
		rows = cur.fetchall()
		return jsonify(users = rows)

@Api.route('/user/<int:id>')
def get_users_by_id(id):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE id = %s", id)
                rows = cur.fetchall()
                return jsonify(users = rows)

@Api.route('/user/<string:username>')
def get_users_by_name(username):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE username = %s", username)
                rows = cur.fetchall()
                return jsonify(users = rows)
