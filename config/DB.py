import mysql.connector
from mysql.connector import Error


class DB():
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',
            database='cafeteria_keikruk',
            user='root',
            password='')

    def connect(self):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()

        except Error as e:
            print("Error while connecting to MySQL", e)
            return False
        finally:
            #sql_select_Query = "SELECT * FROM productos WHERE ID = '1'"
            #cursor = self.connection.cursor()
            #cursor.execute(sql_select_Query)
            #record = (cursor.fetchall())
            #print("Total number of rows in productos is: ", record[0][1])
            return True
            
        
    def close(self):
        if (self.connection.is_connected()):
                self.connection.cursor().close()
                self.connection.close()
