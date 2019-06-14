from connection import *

con = connection.connection("")


class offer:
    def addoffer(self, offername, rate, fromdate, todate, description):
        global con
        cursor = con.cursor()
        s = "Select * from offertable where offername='" + offername + "' and fromdate='" + fromdate + "' and todate='" + todate + "'"
        cursor.execute(s)
        result1 = cursor.fetchone()
        if result1 != None:
            return 3
        else:
            s = "insert into offertable values (null,'" + offername + "','" + rate + "','" + fromdate + "','" + todate + "','" + description + "','Active')"
            print(s)
            res = con.cursor()
            c = res.execute(s)
            con.commit()
            return c

    def viewoffer(self, fromdate, todate):
        global con
        cursor = con.cursor()
        s = ""
        if fromdate == "" and todate == "":
            s = "Select * from offertable where status='Active' order by id DESC"
        else:
            s = "Select * from offertable where status='Active' and fromdate>='" + str(fromdate) + "' and todate<='" + str(
                todate) + "' order by id DESC"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def viewofferbyid(self,id):
        global con
        cursor = con.cursor()
        s = ""
        s = "Select * from offertable where id='"+id+"'"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def editofferaction(self,offername,rate,fromdate,todate,description,id):
        global con
        cursor = con.cursor()
        s = "Select * from offertable where offername='" + offername + "' and fromdate='" + fromdate + "' and todate='" + todate + "' and id<>'"+id+"'"
        # print(s)
        cursor.execute(s)
        result1 = cursor.fetchone()
        # print(result1)
        if result1 != None:
            return 3
        else:
            s1 = "update offertable set offername='" + offername + "',rate='"+rate+"',fromdate='"+fromdate+"',todate='"+todate+"',description='" + description + "' where id='" + str(
                id) + "'"
            # print(s1)
            c = cursor.execute(s1)
            con.commit()
            return c

    def deleteoffer(self,id):
        global con
        s = "update offertable set status='Inactive' where id='" + str(id) + "'"
        cursor = con.cursor()
        res = cursor.execute(s)
        con.commit()
        return res
