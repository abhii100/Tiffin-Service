from connection import *

con = connection.connection("")

class category:
    def addcategory(self, cname, description):
        global con
        cursor = con.cursor()
        s = "Select * from categorytable where cname='" + cname + "'"
        cursor.execute(s)
        result1 = cursor.fetchone()
        if result1 != None:
            return 3
        else:
            s = "insert into categorytable values (null,'" + cname + "','" + description + "')"
            print(s)
            res = con.cursor()
            c = res.execute(s)
            con.commit()
            return c

    def viewcategory(self):
        global con
        cursor = con.cursor()
        s = "Select * from categorytable"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def deletecategory(self,id):
        global con
        s = "delete from categorytable where id='" + str(id) + "'"
        cursor = con.cursor()
        res = cursor.execute(s)
        con.commit()
        return res

    def viewcategorybyid(self,id):
        global con
        cursor = con.cursor()
        s = "Select * from categorytable where id='" + id + "'"
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def editcategoryaction(self,cname,description,id):
        global con
        cursor = con.cursor()
        s = "Select * from categorytable where cname='" + cname + "' and description='" + description + "' and id!='" + str(
            id) + "'"
        # print(s)
        cursor.execute(s)
        result1 = cursor.fetchone()
        # print(result1)
        if result1 != None:
            return 3
        else:
            s1 = "update categorytable set cname='" + cname + "',description='" + description + "' where id='" + str(id) + "'"
            # print(s1)
            c = cursor.execute(s1)
            con.commit()
            return c
