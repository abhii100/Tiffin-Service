import pymysql

class connection:
    def connection(self):
        # con = pymysql.connect("demopython.db.7623447.c79.hostedresource.net","demopython","Demo@123456","demopython")  # Connection String in Python
        con = pymysql.connect("tiffinsystemdb.db.7623447.242.hostedresource.net", "tiffinsystemdb", "Tifin@123", "tiffinsystemdb")  # Connection String in Python
        return con