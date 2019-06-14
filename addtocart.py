import json
from cartlogic import *
from connection import *

con = connection.connection("")
lstcart = []

class addtocart:

    def additemtocart(self, id, qty):
        global con,lstcart

        cursor = con.cursor()
        s = "Select * from itemtable where id='" + id + "'"
        cursor.execute(s)
        row_header = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        for result in rv:
            a = dict(zip(row_header,result))
            total = float(qty) * result[2]
            x = cartlogic(result[0], result[1], result[2], qty, total,result[6])
            # lstcart.append(x.__dict__)
            # print(lstcart)
        print("*********************")
        print(x.__dict__)
        print("*********************")
        return x.__dict__

