import MySQLdb as mdb
import uuid

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def login(username, passwordhash):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id FROM user WHERE username = %s and password_hash = %s", [username, passwordhash])
		row = cur.fetchone()
		if row:
			sessionid = create_session(row['id'])
			return sessionid
		return None

def create_session(user_id):
	with con:
		sessionid = str(uuid.uuid4())
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("INSERT INTO sessions VALUES (%s, %s, NOW())", [sessionid, user_id])
		return sessionid

def get_userid_from_session(sessionid):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT user_id FROM session WHERE uuid = %s", sessionid)
		rows = cur.fetchone()
		return rows['user_id']
