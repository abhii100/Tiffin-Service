from connection import *
from datetime import *
import os

con = connection.connection("")


class partner:
    def signuppartner(self, companyname, ownername, mobileno, address, email, password, location):
        global con
        cursor = con.cursor()
        s = "Select * from partnertable where email='" + email + "'"
        cursor.execute(s)
        result1 = cursor.fetchone()
        if result1 != None:
            return 3
        else:
            location = location.replace('+', "%20")
            s = "insert into partnertable values (null,'" + companyname + "','" + ownername + "','" + mobileno + "','" + address + "','" + email + "','" + password + "','Pending','" + location + "')"
            print(s)
            res = con.cursor()
            c = res.execute(s)
            con.commit()
            return c

    def restorders(self, partnerid, status):
        global con
        cursor = con.cursor()
        if status == 'Other' and partnerid != '':
            s = "select ordertable.customeremail,ordertable.name,ordertable.mobileno,ordertable.city,ordertable.shippingaddress,ordertable.amount,ordertable.dateoforder,ordertable.paymentmode,partnertable.companyname,ordertable.id from partnertable,ordertable where partnertable.id=ordertable.restid and ordertable.restid='" + str(
                partnerid) + "' and (ordertable.status='Accepted' or ordertable.status='Rejected') order by ordertable.id DESC"
        else:
            if partnerid == '':
                s = ""
            else:
                s = "select ordertable.customeremail,ordertable.name,ordertable.mobileno,ordertable.city,ordertable.shippingaddress,ordertable.amount,ordertable.dateoforder,ordertable.paymentmode,partnertable.companyname,ordertable.id from partnertable,ordertable where partnertable.id=ordertable.restid and ordertable.restid='" + str(
                    partnerid) + "' and ordertable.status='" + status + "' order by ordertable.id DESC"
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
            d['orderid'] = p[9]
            r.append(d)
        return r

    def restorderdetail(self, orderid):
        global con
        cursor = con.cursor()
        if orderid == '':
            s = ""
        else:
            s = "select orderdetail.*,ordertable.status from orderdetail,ordertable where orderdetail.orderid=ordertable.id and orderdetail.orderid='" + str(
                orderid) + "'"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        r = []
        for p in result1:
            d = {}
            d['id'] = p[0]
            d['orderid'] = p[1]
            d['itemid'] = p[2]
            d['itemname'] = p[3]
            d['price'] = p[4]
            d['qty'] = p[5]
            d['amount'] = p[6]
            d['orderstatus'] = p[7]
            r.append(d)
        return r

    def accept_reject_order(self, orderid, status):
        global con
        cursor = con.cursor()
        if orderid == '':
            s = ""
        else:
            s = "update ordertable set status='" + status + "' where id='" + str(orderid) + "'"
        print(s)
        res = cursor.execute(s)
        con.commit()
        d = {}
        d['message'] = "Order " + status
        return d

    def todaysales(self, partnerid):
        con = connection.connection('')
        cursor = con.cursor()
        dt = datetime.now().date()
        s = "select paymentmode,sum(amount) from ordertable where dateoforder='" + str(
            dt) + "' and status='Accepted' and restid='" + partnerid + "' group by paymentmode"
        cursor.execute(s)
        res = cursor.fetchall()
        con.close()
        r = []
        for p in res:
            d = {}
            d['name'] = p[0]
            d['y'] = p[1]
            r.append(d)
        return r

    def monthlysales(self, partnerid):
        con = connection.connection('')
        cursor = con.cursor()
        dt = datetime.now().date()
        s = "select dateoforder,sum(amount) from ordertable where MONTH(dateoforder)=MONTH(CURRENT_DATE()) and status='Accepted' and restid='" + partnerid + "' group by dateoforder"
        cursor.execute(s)
        res = cursor.fetchall()
        con.close()
        r = []
        for p in res:
            d = {}
            d['label'] = p[0]
            d['y'] = p[1]
            r.append(d)
        return r

    def allpartnerforcustomer(self, name, id):
        con = connection.connection('')
        cursor = con.cursor()
        s = ""
        if name == "" and id == "":
            s = "Select * from partnertable where status='Approved' order by id DESC "
        elif name == "" and id != "":
            s = "Select * from partnertable where status='Approved' and id='" + id + "'"
        else:
            s = "Select * from partnertable where status='Approved' and (companyname LIKE '%" + name + "%' or ownername LIKE '%" + name + "%') order by id DESC "
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def viewpendingpartner(self, name):
        global con
        cursor = con.cursor()
        s = ""
        if name == "":
            s = "Select * from partnertable order by id DESC "
        else:
            s = "Select * from partnertable where (companyname LIKE '%" + name + "%' or ownername LIKE '%" + name + "%') order by id DESC "
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def approverejectpartner(self, id, status):
        global con
        s = "update partnertable set status='" + status + "' where id='" + id + "'"
        print(s)
        res = con.cursor()
        c = res.execute(s)
        con.commit()
        return c

    def loginpartner(self, email, password):
        global con
        cursor = con.cursor()
        s = "Select * from partnertable where email='" + email + "' and password='" + password + "' and status='Approved'"
        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def changepassword(self, email, oldpassword, newpassword):
        global con
        cursor = con.cursor()
        s = "select * from partnertable where email='" + email + "' and password='" + oldpassword + "'"
        cursor.execute(s)
        res = cursor.fetchone()
        if res != None:
            s1 = "update partnertable set password='" + newpassword + "' where email='" + email + "'"
            c = cursor.execute(s1)
            con.commit()
            return c
        else:
            return 3


    def addgallery(self,partnerid,photo,photoname):
        con = connection.connection("")
        s = "insert into partnerphoto values(null,'"+str(partnerid)+"','"+photoname+"')"
        print(s)
        cr = con.cursor()
        res = cr.execute(s)
        con.commit()
        con.close()
        filepath = '../../static/upload/'
        if not os.path.exists(filepath):
            os.mkdir(filepath)

        with open(filepath + photoname, 'wb+') as destination:
            for chunk in photo.chunks():
                destination.write(chunk)
        return res

