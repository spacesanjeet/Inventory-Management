#PYTHON MODULE: INVENTORY
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def clrscreen():
    print('\n' * 5)


def searchData():
    try:
        os.system('cls')
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = input("Enter Product Code to be searched from the Inventory : ")
        query = ("SELECT * FROM Inventory where ProductCode = %s")
        rec_srch = (ProductCode,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for (ProductCode, ProductName, PurchaseDate, SalesDate, PurchasePrice, SalesPrice) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("1.Product Code : ", ProductCode)
            print("2.Product Name : ", ProductName)
            print("3.Purchase Date : ", PurchaseDate)
            print("4.Sales Date : ", SalesDate)
            print("5.Purchase Price : ", PurchaseDate)
            print("6.Sales Price : ", SalesPrice)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
        Cursor.close()
        cnx.close()
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
