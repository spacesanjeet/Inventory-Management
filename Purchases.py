#PYTHON MODULE: PURCHASES
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))


def insertData():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = input("Enter Product Code : ")
        ProductName = input("Enter Product Name : ")
        print("Enter Date of Purchase (Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        PurchaseDate = date(YY,MM,DD)
        PurchasePrice = int(input("Enter Product Price : "))
        ProductStock = int(input("Enter Quantity purchased : "))
        Qry = ("INSERT INTO Purchases VALUES (%s, %s, %s, %s, %s)")
        data = (ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock)
        Cursor.execute(Qry,data)
        Qry1 = ("INSERT INTO Inventory(ProductCode,ProductName,PurchaseDate,PurchasePrice) VALUES(%s, %s, %s, %s)")
        data1 = (ProductCode, ProductName, PurchaseDate, PurchasePrice)
        Cursor.execute(Qry1,data1)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def deleteData():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = input("Enter Product Code to be deleted from the Purchases : ")
        Qry = ("""DELETE FROM Purchases WHERE ProductCode = %s""")
        del_rec = (ProductCode,)
        Cursor .execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def searchData():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = input("Enter Product Code to be searched from the Purchases : ")
        query = ("SELECT * FROM Purchases WHERE ProductCode = %s ")
        rec_srch = (ProductCode,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Product Code : ", ProductCode)
            print("Product Name : ", ProductName)
            print("Purchased on : ", PurchaseDate)
            print("Price of Product : ", PurchasePrice)
            print("Product in Stock : ", ProductStock)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def updateData():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = input("Enter Product Code to be updated from the Purchases : ")
        query = ("SELECT * FROM Purchases WHERE ProductCode = %s ")
        rec_srch = (ProductCode,)
        print("Enter new data")
        ProductName = input("Enter Product Name : ")
        print("Enter Date of Purchase (Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        PurchaseDate = date(YY,MM,DD)
        PurchasePrice = int(input("Enter Product Price : "))
        ProductStock = int(input("Enter Quantity purchased : "))
        Qry = ("UPDATE Purchases SET ProductName=%s, PurchaseDate=%s, PurchasePrice=%s, ProductStock=%s  WHERE ProductCode=%s")
        data = (ProductName, PurchaseDate, PurchasePrice, ProductStock, ProductCode)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()
