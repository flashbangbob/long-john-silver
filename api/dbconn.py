import MySQLdb as mdb

def get_new_connection():
	return mdb.connect('localhost', 'flashbangbob', '5022', 'main')
		
		
		
		
		
