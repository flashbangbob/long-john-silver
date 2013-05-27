from flask import Flask, jsonify
import user_api
import corp_api
import shop_type_api
import MySQLdb as mdb
import json

app = Flask(__name__)
app.config.update(DEBUG=True)

'''
RTE - ROOT
'''        

@app.route('/')
def hello_world():
        data = {"id": 5, "title": "Myworld"}
        return jsonify(**data)

'''
RTE - CORP
'''        

@app.route('/corp/<int:id>')
def get_corp_for_user_id(id):
	corp = corp_api.get_corp_for_user_id(id)
	return jsonify(corp=corp)

'''
RTE - USERS
'''

@app.route('/user/')
def get_users():
	rows = user_api.get_users()
	return jsonify(users = rows)

@app.route('/user/<int:id>')
def get_users_by_id(id):
	row = user_api.get_users_by_id(id)
    	return jsonify(users = row)

@app.route('/user/<string:username>')
def get_users_by_name(username):
	row = user_api.get_users_by_name(username)
    	return jsonify(users = row)

'''
RTE - SHOPTYPE
'''

@app.route('/user/')
def get_shop_types():
	rows = shop_type_api.get_shop_types()
	return jsonify(shop_types = rows)


'''
PROGRAMRUN
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)












