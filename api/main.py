from flask import Flask, jsonify
import user_api
import corp_api
import shop_type_api
import product_api
import MySQLdb as mdb
import json

app = Flask(__name__)
app.config.update(DEBUG=True)

'''
RTE - ROOT
'''        

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

'''
RTE - AUTH
'''       

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

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

@app.route('/shoptype/')
def get_shop_types():
	rows = shop_type_api.get_shop_types()
	return jsonify(shop_types = rows)


'''
RTE - PRODUCT
'''

@app.route('/product/')
def get_shop_types():
	rows = product_api.get_products()
	return jsonify(products = rows)


'''
PROGRAMRUN
'''
app.secret_key = 'Wb \x85\x13\x94\x13\xb7z\xd5\xe3#(a\xe1\xf0\x07\xb2\xb1\xbbq\xf8\x888'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)












