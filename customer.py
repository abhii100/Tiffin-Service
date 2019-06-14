from connection import *
import os
from datetime import *

con = connection.connection("")


class customer:

    def addorder(self,customerid,customeremail,name,mobileno,city,address,amount,partnerid,paymentmode):
        global con
        cursor = con.cursor()
        dt = datetime.now().date()
        s = "insert into ordertable values (null,'"+str(customerid)+"','"+customeremail+"','"+name+"','"+str(mobileno)+"','"+city+"','"+address+"','"+str(amount)+"','"+str(dt)+"','"+str(partnerid)+"','"+paymentmode+"','Pending')"
        res = cursor.execute(s)
        con.commit()
        orderid = cursor.lastrowid
        return orderid

    def addorderdetail(self,orderid,itemid,itemname,price,qty,amount):
        global con
        cursor = con.cursor()
        dt = datetime.now().date()
        s = "insert into orderdetail values (null,'" + str(orderid) + "','" + str(itemid) + "','" + itemname + "','" + str(price) + "','" + str(qty)+ "','" + str(amount) + "')"
        res = cursor.execute(s)
        con.commit()
        return res


    def signupcustomer(self, name, mobileno, address, photo, photoname, city, email, password):
        global con
        cursor = con.cursor()
        s = "Select * from customertable where email='" + email + "'"
        cursor.execute(s)
        result1 = cursor.fetchone()
        if result1 != None:
            return 3
        else:
            s = "insert into customertable values (null,'" + name + "','" + mobileno + "','" + address + "','" + photoname + "','" + city + "','" + email + "','" + password + "','Pending')"
            # print(s)
            res = con.cursor()
            c = res.execute(s)
            con.commit()
            print()
            filepath = '../../static/upload/'
            if not os.path.exists(filepath):
                os.mkdir(filepath)

            with open(filepath + photoname, 'wb+') as destination:
                for chunk in photo.chunks():
                    destination.write(chunk)
            return c

    def logincustomer(self, email, password):
        global con
        cursor = con.cursor()
        s = "Select * from customertable where email='" + email + "' and password='" + password + "' and status='Approved'"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def viewpendingcustomer(self, name):
        global con
        cursor = con.cursor()
        s = ""
        if name == "":
            s = "Select * from customertable order by id DESC"
        else:
            s = "Select * from customertable where name LIKE '%" + name + "%' order by id DESC"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def showsales(self,customerid):
        global con
        cursor = con.cursor()
        s = "select paymentmode,sum(amount) from ordertable where customerid='"+str(customerid)+"' group by paymentmode"
        cursor.execute(s)
        result1 = cursor.fetchall()
        r = []
        for p in result1:
            d = {}
            d['name'] = p[0]
            d['y'] = p[1]
            r.append(d)
        return r

    def myorders(self,customerid):
        global con
        cursor = con.cursor()
        if customerid=='':
            s = ""
        else:
            s = "select ordertable.customeremail,ordertable.name,ordertable.mobileno,ordertable.city,ordertable.shippingaddress,ordertable.amount,ordertable.dateoforder,ordertable.paymentmode,partnertable.companyname from partnertable,ordertable where partnertable.id=ordertable.restid and ordertable.customerid='"+str(customerid)+"'"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        r = []
        for p in result1:
            d = {}
            d['email'] = p[0]
            d['name'] = p[1]
            d['mobileno'] = p[2]
            d['city'] = p[3]
            d['address'] = p[4]
            d['amount'] = p[5]
            d['dateoforder'] = p[6]
            d['paymentmode'] = p[7]
            d['companyname'] = p[8]
            r.append(d)
        return r

    def approverejectcustomer(self, id, status):
        global con
        s = "update customertable set status='" + status + "' where id='" + id + "'"
        print(s)
        res = con.cursor()
        c = res.execute(s)
        con.commit()
        return c

    def changepassword(self, email, oldpassword, newpassword):
        global con
        cursor = con.cursor()
        s = "select * from customertable where email='" + email + "' and password='" + oldpassword + "'"
        cursor.execute(s)
        res = cursor.fetchone()
        if res != None:
            s1 = "update customertable set password='" + newpassword + "' where email='" + email + "'"
            c = cursor.execute(s1)
            con.commit()
            return c
        else:
            return 3
