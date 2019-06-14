

class cartlogic:
    itemid = 0
    itemname = ""
    price = 0.0
    qty = 0
    total = 0.0
    netprice = 0.0
    partnerid = 0

    def __init__(self,itemid,itemname,price,qty,total,partnerid):
        self.itemid = itemid
        self.itemname = itemname
        self.price = price
        self.qty = qty
        self.total = total
        self.partnerid = partnerid
