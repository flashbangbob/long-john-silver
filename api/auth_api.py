import uuid
import hashlib
import dbconn

def login(username, password):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		passwordhash = hashlib.sha224(password).hexdigest()
		cur.execute("SELECT id FROM user WHERE username = %s and password_hash = %s", (username, passwordhash))
		row = cur.fetchone()
		if row:
			sessionid = create_session(row['id'])
			return True
		return False

def create_session(userid):
	con = dbconn.get_new_connection()
	with con:
		sessionid = str(uuid.uuid4())
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("INSERT INTO sessions VALUES (%s, %s, NOW())", [sessionid, userid])
		cur.close()
		return sessionid
		
def destroy_session(sessionid):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("DELETE FROM sessions WHERE uuid = %s", sessionid)
		return True

def get_userid_from_session(sessionid):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT user_id FROM sessions WHERE uuid = %s", sessionid)
		rows = cur.fetchone()
		return rows['user_id']

def is_valid_session(sessionid, userid):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT count(*) FROM sessions WHERE uuid = %s and user_id = %s", (sessionid, userid))
		row = cur.fetchone()
		if row:
			return True
		return None
		
		
		
		
		
		
		
