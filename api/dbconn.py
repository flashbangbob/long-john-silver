import MySQLdb as mdb

def get_new_connection():
	return mdb.connect(host = 'localhost', user = 'flashbangbob', passwd = '5022', db = 'main', cursorclass = mdb.cursors.DictCursor)
		
		
		
		
		
