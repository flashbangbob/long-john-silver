import MySQLdb
import MySQLdb.cursors

def get_new_connection():
	return MySQLdb.connect(host = 'localhost', user = 'flashbangbob', passwd = '5022', db = 'main', cursorclass = MySQLdb.cursors.DictCursor)
		
		
		
		
		
