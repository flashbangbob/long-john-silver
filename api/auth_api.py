import uuid
import hashlib
import dbconn

def login(username, password):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		passwordhash = hashlib.sha224(password).hexdigest()
		cur.execute("SELECT id FROM user WHERE username = %s and password_hash = %s", (username, passwordhash))
		row = cur.fetchone()
		if row:
			sessionid = create_session(row['id'])
			return sessionid
		return None

def create_session(userid):
	con = dbconn.get_new_connection()
	with con:
		sessionid = str(uuid.uuid4())
		cur = con.cursor()
		cur.execute("INSERT INTO sessions VALUES (%s, %s, NOW())", (sessionid, userid))
		cur.close()
		con.commit()
		return sessionid
		
def destroy_session(sessionid):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		cur.execute("DELETE FROM sessions WHERE session_id = %s", sessionid)
		return True

def get_userid_from_session(sessionid):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		cur.execute("SELECT user_id FROM sessions WHERE session_id = %s", (sessionid,))
		rows = cur.fetchone()
		if rows:
			return rows['user_id']
		return None

def is_valid_session(sessionid, userid):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		cur.execute("SELECT count(*) as cnt FROM sessions WHERE session_id = %s and user_id = %s", (sessionid, userid))
		row = cur.fetchone()
		if row['cnt'] > 0:
			return True
		return False
		
		
		
		
		
		
		
