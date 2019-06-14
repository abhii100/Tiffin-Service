

class mycart:
    itemid = 0
    itemname = ""
    price = 0.0
    qty = 0
    total = 0.0
    netprice = 0.0

    def __init__(self,itemid,itemname,price,qty,total):
        self.itemid = itemid
        self.itemname = itemname
        self.price = price
        self.qty = qty
        self.total = total
        # s = str(self.itemid) + " - " + self.itemname + " - " + str(self.price) + " - " + str(self.qty) + " - " + str(self.total)
        # print(s)
