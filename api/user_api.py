import corp_api
import dbconn

def get_users():
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		cur.execute("SELECT id, username, email FROM user")
		rows = cur.fetchall()
		return rows

def get_users_by_id(id):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()	
		cur.execute("SELECT id, username, email FROM user WHERE id = %s", id)
		row = cur.fetchone()
        row['corp'] = corp_api.get_corp_for_user_id(row['id'])
      	return row

def get_users_by_name(username):
    with con:
        cur = con.cursor()
        cur.execute("SELECT id, username, email FROM user WHERE username = %s", username)
        row = cur.fetchone()
        row['corp'] = corp_api.get_corp_for_user_id(row['id'])
        return row;
