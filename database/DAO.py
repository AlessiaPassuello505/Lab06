from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_Anni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        # Usiamo DISTINCT e YEAR() per avere anni univoci
        query = "SELECT DISTINCT YEAR(Date) as anno FROM go_daily_sales ORDER BY anno DESC"
        cursor.execute(query)
        res = [row["anno"] for row in cursor]
        print(res)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_Brand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        # Usiamo DISTINCT e YEAR() per avere anni univoci
        query = """select distinct product_brand as brand 
                from go_products gp """
        cursor.execute(query)
        res = [row["brand"] for row in cursor]
        print(res)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_Retail():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                from go_retailers gr """

        cursor.execute(query)
        res = []
        for row in cursor:
            # USA I NOMI ESATTI DEL DATABASE (es. Retailer_code)
            res.append(Retailer(
                codice=row["Retailer_code"],
                nome=row["Retailer_name"],
                type=row["Type"],
                paese=row["Country"]
            ))
        print(res)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def top_Vendite(anno,brand,retail):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select gds.*
                    from go_daily_sales gds, go_products gp
                    WHERE YEAR(gds.Date) = %s AND gp.Product_brand = %s AND gds.Retailer_code = %s
                    order by gds.Quantity * Unit_sale_price desc"""

        cursor.execute(query,(anno,brand,retail))
        res = []
        for row in cursor:
            # USA I NOMI ESATTI DEL DATABASE (es. Retailer_code)
            res.append((row["Retailer_code"],
                row["Product_number"],
                row["Order_method_code"],
                row["Date"],
                row["Quantity"],
                row["Unit_price"],
                row["Unit_sale_price"]
                       ))
        print(res)
        cursor.close()
        cnx.close()
        return res







