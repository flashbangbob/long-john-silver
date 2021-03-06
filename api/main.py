from flask import Flask, jsonify, session, redirect, url_for, escape, request
import user_api
import corp_api
import shop_type_api
import product_api
import auth_api
import shares_api
import trade_api
import MySQLdb as mdb
import json

app = Flask(__name__)
app.config.update(DEBUG=True)

@app.before_request
def before_request():
    if request.remote_addr == '127.0.0.1':
        return
        
    if ('sessionid' not in session or 'userid' not in session) and request.endpoint != 'login' and request.endpoint != 'logout' and request.endpoint != 'index':
        return redirect(url_for('login'))
    elif request.endpoint != 'login' and request.endpoint != 'logout' and request.endpoint != 'index' :
        validsession = auth_api.is_valid_session(session['sessionid'], session['userid'])
        if validsession == False:
          return redirect(url_for('logout'))

'''
RTE - ROOT
'''
@app.route('/')
def index():
    if 'sessionid' in session and 'sessionid' != None:
        return 'Logged in as userID: %s' % escape(session['userid'])
    return 'You are not logged in'

'''
RTE - AUTH
'''       
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        sessionid = auth_api.login(request.form['username'], request.form['password'])
        if sessionid:
            session['sessionid'] = sessionid
            session['userid'] = auth_api.get_userid_from_session(sessionid)
            session['corpid'] = corp_api.get_corp_by_id(session['userid'])['id']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    auth_api.destroy_session(session['sessionid'])
    session.pop('sessionid', None)
    return redirect(url_for('index'))

'''
RTE - CORP
'''        

@app.route('/corp/<int:id>')
def get_corp_for_user_id(id):
    corp = corp_api.get_corp_by_id(id)
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
    row = user_api.get_user_by_id(id)
    return jsonify(users = row)

@app.route('/user/<string:username>')
def get_users_by_name(username):    
    row = user_api.get_user_by_name(username)
    return jsonify(users = row)

'''
RTE - SHOPTYPE
'''

@app.route('/shoptype/')
def get_shop_types():
    rows = shop_type_api.get_shop_types()
    return jsonify(shop_types = rows)

'''
RTE - SHARES
'''

@app.route('/shares/')
def get_shares():
    rows = shares_api.get_all_shares_for_corp_id(session['corpid'])
    return jsonify(shares = rows)

'''
RTE - TRADE
'''

@app.route('/trade/')
def trade_stock():
    action = request.args.get('action', '')
    targetCorpId = int(request.args.get('corpid', ''))
    quantity = int(request.args.get('quantity', ''))
    if action == "sell":
        trade_api.sell_stock(session['corpid'], targetCorpId, quantity)
    else:
        trade_api.buy_stock(session['corpid'], targetCorpId, quantity)
    return get_shares()


'''
RTE - PRODUCT
'''

@app.route('/product/')
def get_products():
    rows = product_api.get_products()
    return jsonify(products = rows)


'''
PROGRAMRUN
'''
app.secret_key = 'Wb \x85\x13\x94\x13\xb7z\xd5\xe3#(a\xe1\xf0\x07\xb2\xb1\xbbq\xf8\x888'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)












