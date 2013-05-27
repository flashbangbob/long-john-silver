from flask import Blueprint, jsonify
import MySQLdb as mdb
import sys
import json

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main'); 
corp_api = Blueprint('corp_api', __name__)

@corp_api.route('/corp/<int:id>')
def get_corp_for_user_id(id):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id, name, ticker, money, share_price FROM corporation WHERE id = %s", id)
		rows = cur.fetchall()
		return jsonify(corp = rows)
