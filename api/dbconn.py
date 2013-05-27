import MySQLdb
import MySQLdb.cursors

def get_new_connection():
	conn =  MySQLdb.connect(host = 'localhost', user = 'flashbangbob', passwd = '5022', db = 'main', cursorclass = MySQLdb.cursors.DictCursor)
	conn.autocommit(True)
	return conn	
		
		
		
