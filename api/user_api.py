import corp_api
import MySQLdb as mdb

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_users():
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id, username, email FROM user")
		rows = cur.fetchall()
		return rows

def get_users_by_id(id):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE id = %s", id)
                row = cur.fetchone()
                row['corp'] = corp_api.get_corp_for_user_id(row['id'])
      		return row

def get_users_by_name(username):
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT id, username, email FROM user WHERE username = %s", username)
                row = cur.fetchone()
                row['corp'] = corp_api.get_corp_for_user_id(row['id'])
                return row;
