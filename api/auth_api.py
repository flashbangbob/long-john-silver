import MySQLdb as mdb
import uuid
import hashlib

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def login(username, password):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		passwordhash = hashlib.sha224(password).hexdigest()
		cur.execute("SELECT id FROM user WHERE username = %s and password_hash = %s", (username, passwordhash))
		row = cur.fetchone()
		if row:
			sessionid = create_session(row['id'])
			return True
		return False

def logout(sessionid):
	

def create_session(userid):
	with con:
		sessionid = str(uuid.uuid4())
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("INSERT INTO sessions VALUES (%s, %s, NOW())", [sessionid, userid])
		return sessionid
		
def destroy_session(sessionid):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("DELETE FROM sessions WHERE uuid = %s", sessionid)
		return True

def get_userid_from_session(sessionid):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT user_id FROM session WHERE uuid = %s", sessionid)
		rows = cur.fetchone()
		return rows['user_id']

def is_valid_session(sessionid, userid)
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT count(*) FROM session WHERE uuid = %s and user_id = %s", (sessionid, userid))
		row = cur.fetchone()
		if row:
			return True
		return None
		
		
		
		
		
		
		