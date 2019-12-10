#Project on Inventory Management System
#Author : Sanjeet
#--------------------------------------------------------------------------------
#MODULE : INVENTORY MANAGEMENT
import Database
import Purchases
import Menulib

Database.DatabaseCreate()
Database.TablesCreate()


while True:
    Purchases.clrscreen()
    print("\t\t\t Inventory Management\n")
    print("=====================================================================")
    print("1. Purchase Management")
    print("2. Sales Management")
    print("3. Inventory Management")
    print("4. Exit")
    choice = int(input("Enter Choice between 1 to 4 -------> : "))
    if choice == 1:
        Menulib.MenuPurchases()
    elif choice == 2:
        Menulib.MenuSales()
    elif choice == 3:
        Menulib.MenuInventory()
    elif choice == 4:
        break
    else:
        print("Wrong Choice.....Enter Your Choice again")
        x = input("Press any key to continue: ")
