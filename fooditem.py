from connection import *

con = connection.connection("")


class fooditem:
    def addfooditem(self, itemname, price, description, categoryid, partnerid, availabledays):
        global con
        cursor = con.cursor()
        m = ""
        for k in availabledays:
            m += k + ","
        m = m[:-1]
        print(m)
        s = "Select * from itemtable where itemname='" + itemname + "' and categoryid='" + categoryid + "'"
        cursor.execute(s)
        result1 = cursor.fetchone()
        if result1 != None:
            return 3
        else:
            s = "insert into itemtable values (null,'" + itemname + "','" + price + "','" + description + "','" + categoryid + "','Active','" + str(
                partnerid) + "','" + m + "')"
            # print(s)
            res = con.cursor()
            c = res.execute(s)
            con.commit()
            return c

    def getcategory_item(self, partnerid='', categoryid=''):
        global con
        cursor = con.cursor()
        if partnerid != '' and categoryid == '':
            s = "SELECT categoryid,categorytable.cname FROM `itemtable`,categorytable where itemtable.categoryid=categorytable.id and partnerid='" + partnerid + "' group by categoryid"
        elif partnerid != '' and categoryid != '':
            s = "select * from itemtable where categoryid='" + str(categoryid) + "' and partnerid='" + str(partnerid) + "'"

        print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def viewfooditem(self, id='', partnerid='', categoryid=''):
        global con
        cursor = con.cursor()
        if id == '' and partnerid == '':
            s = "Select itemtable.id,itemtable.itemname,itemtable.price,itemtable.description,categorytable.id,categorytable.cname,itemtable.availabledays from itemtable,categorytable where itemtable.categoryid=categorytable.id"
        elif id == '' and partnerid != '':
            s = "Select itemtable.id,itemtable.itemname,itemtable.price,itemtable.description,categorytable.id,categorytable.cname,itemtable.availabledays from itemtable,categorytable where itemtable.categoryid=categorytable.id and partnerid='" + str(
                partnerid) + "'"
        elif id != '' and partnerid == '':
            s = "Select itemtable.id,itemtable.itemname,itemtable.price,itemtable.description,categorytable.id,categorytable.cname,itemtable.availabledays from itemtable,categorytable where itemtable.categoryid=categorytable.id and itemtable.id='" + id + "'"
        elif id == '' and partnerid != '' and categoryid != '':
            s = "Select itemtable.id,itemtable.itemname,itemtable.price,itemtable.description,categorytable.id,categorytable.cname,itemtable.availabledays from itemtable,categorytable where itemtable.categoryid=categorytable.id and itemtable.categoryid='" + categoryid + "' and partnerid='" + str(
                partnerid) + "'"
        else:
            s = "Select itemtable.id,itemtable.itemname,itemtable.price,itemtable.description,categorytable.id,categorytable.cname,itemtable.availabledays from itemtable,categorytable where itemtable.categoryid=categorytable.id and itemtable.id='" + id + "' and partnerid='" + str(
                partnerid) + "'"
        # print(s)
        cursor.execute(s)
        result1 = cursor.fetchall()
        return result1

    def deletefooditem(self, id):
        global con
        s = "delete from itemtable where id='" + str(id) + "'"
        cursor = con.cursor()
        res = cursor.execute(s)
        con.commit()
        return res
