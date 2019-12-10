#PYTHN MODULE: MENULIB
import Purchases
import Sales
import Inventory

def MenuPurchases():
    while True:
        Purchases.clrscreen()
        print("\t\t\t Purchase Record Management\n")
        print("=================================================================")
        print("1. Add Purchase Record")
        print("2. Search Purchase Record")
        print("3. Delete Purchase Record")
        print("4. Update Purchase Record")
        print("5. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 5 -------> : "))
        if choice == 1:
            Purchases.insertData()
        elif choice == 2:
            Purchases.searchData()
        elif choice == 3:
            Purchases.deleteData()
        elif choice == 4:
            Purchases.updateData()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuSales():
    while True:
        Purchases.clrscreen()
        print("\t\t\t Sales Record Management\n")
        print("=================================================================")
        print("1. Add Sales Record")
        print("2. Search Sales Record")
        print("3. Delete Sales Record")
        print("4. Update Sales Record")
        print("5. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            Sales.insertData()
        elif choice == 2:
            Sales.searchData()
        elif choice == 3:
            Sales.deleteData()
        elif choice == 4:
            Sales.updateData()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuInventory():
    while True:
        Purchases.clrscreen()
        print("\t\t\t Inventory Record Management\n")
        print("=================================================================")
        print("1. Search from Inventory")
        print("2. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 3 ------> : "))
        if choice == 1:
            Inventory.searchData()
        elif choice == 2:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")
