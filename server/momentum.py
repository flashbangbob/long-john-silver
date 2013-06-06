import dbconn

#UPDATE STOCKS
con = dbconn.get_new_connection()
with con:
    cur = con.cursor()
    cur.execute("UPDATE corporation SET momentum = momentum - sign(momentum)")