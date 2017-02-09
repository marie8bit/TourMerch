import sqlite3, DBManager, ui
from items import Item
from performances import Performance
from merchSales import Sale
#process choice from user
def handle_choice(choice):
    if choice == '1':
        itemList = DBManager.showAll(Item)
        for ob in itemList:
            print(ob)
    if choice == '2':
        ui.addNewItem()
    if choice == '3':
        ui.addNewPerformance()
    if choice == '4':
        #validates user input/tells them they cannot add a sale object without
        #data in the tables that provide foreign keys
        if not DBManager.showAll(Item):
            print ('No items in Database, try adding a new item')
        elif not DBManager.showAll(Performance):
            print ('No performances in Database, try adding a new performance')
        else:
            ui.addNewSale()
    if choice == '5':
        ui.getTSpI()
    if choice == '6':
        ui.getTSpP()
    if choice == 'q':
        quit()
