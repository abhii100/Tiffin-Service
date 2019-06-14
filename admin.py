from connection import *

con = connection.connection("")

class admin:

    def loginadmin(self, email, password):
        global con
        cursor = con.cursor()
        s = "Select * from admintable where email='" + email + "' and password='" + password + "'"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def changepassword(self, email, oldpassword, newpassword):
        global con
        cursor = con.cursor()
        s = "select * from admintable where email='" + email + "' and password='" + oldpassword + "'"
        cursor.execute(s)
        res = cursor.fetchone()
        if res != None:
            s1 = "update admintable set password='" + newpassword + "' where email='" + email + "'"
            c = cursor.execute(s1)
            con.commit()
            return c
        else:
            return 3