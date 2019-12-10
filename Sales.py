#PYTHON MODULE: SALES
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os


def clrscreen():
    print('\n' * 5)


def insertData():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = input("Enter Product Code : ")
        ProductName = input("Enter Product Name : ")
        print("Enter Date of Sales (Date/Month and Year) seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        SalesDate = date(YY,MM,DD)
        SalesPrice = int(input("Enter Sales Price : "))
        Qry = ("INSERT INTO Sales VALUES(%s, %s, %s, %s)")
        data = (ProductCode, ProductName, SalesDate, SalesPrice)
        Cursor.execute(Qry, data)
        #Qry1 = ("INSERT INTO Inventory(SalesDate,SalesPrice) SELECT SalesDate, SalesPrice FROM Sales WHERE ProductCode")
        #data1 = (ProductCode)
        #Cursor.execute(Qry1,data1)
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
        ProductCode = input("Enter Product Code to be deleted from the Sales : ")
        Qry =("""DELETE FROM Sales WHERE ProductCode = %s""")
        del_rec = (ProductCode,)
        Cursor.execute(Qry, del_rec)
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
        ProductCode = input("Enter Product Code to be searched from the Sales : ")
        query = ("SELECT * FROM Sales where ProductCode = %s")
        rec_srch = (ProductCode,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(ProductCode, ProductName, SalesDate, SalesPrice) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Product Code : ", ProductCode)
            print("Product Name : ", ProductName)
            print("Date of Sale : ", SalesDate)
            print("Sale Price : ", SalesPrice)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key to continue: ")
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
        ProductCode = input("Enter Product Code to be updated from the Sales : ")
        query = ("SELECT * FROM Sales WHERE ProductCode = %s")
        rec_srch = (ProductCode,)
        print("Enter new data")
        ProductName = input("Enter Product Name : ")
        print("Enter Date of Sales (Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        SalesDate = date(YY,MM,DD)
        SalesPrice = input("Enter Sales Price : ")
        Qry = ("UPDATE Sales SET ProductName=%s, SalesDate=%s, SalesPrice=%s WHERE ProductCode=%s")
        data = (ProductName, SalesDate, SalesPrice, ProductCode)
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
