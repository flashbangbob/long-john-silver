import dbconn
import time

#UPDATE STOCKS
con = dbconn.get_new_connection()
for x in range(0,6)
    with con:
        cur = con.cursor()
        cur.execute("UPDATE corporation SET share_price = share_price * (1 + ((RAND() - .5) / 1000))")
    time.sleep(10)