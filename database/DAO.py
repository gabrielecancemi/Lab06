from database.DB_connect import DBConnect
from model.daily_sales import Daily_sales
from model.retailer import Retailer


class DAO():

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "select DISTINCT YEAR(Date) from go_daily_sales"

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["YEAR(Date)"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "select DISTINCT Product_brand from go_products"

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["Product_brand"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "select * from go_retailers"

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getVendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("select * from go_daily_sales as gds, go_products as gp" +
                 " where YEAR(Date) = COALESCE(%s, YEAR(Date))" +
                 " and Product_brand = COALESCE(%s, Product_brand)" +
                 " and Retailer_code = COALESCE(%s, Retailer_code)" +
                 " and gds.Product_number = gp.Product_number")

        cursor.execute(query, (anno, brand, retailer))

        res = []
        for row in cursor:
            res.append(Daily_sales(row["Retailer_code"], row["Product_number"], row["Date"], row["Quantity"]*row["Unit_sale_price"]))

        cursor.close()
        cnx.close()
        return res