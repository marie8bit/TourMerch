import sqlite3, DBManager, ui
from items import Item
from performances import Performance
from merchSales import Sale
#process choice from user
def handle_choice(choice):
    if choice == '1':
        DBManager.showAll(Item)
    if choice == '2':
        ui.addNewItem()
    if choice == '3':
        ui.addNewPerformance()
    if choice == '4':
        ui.addNewSale()
    if choice == '5':
        getTSpI()
    if choice == '6':
        getTSpP()
    if choice == 'q':
        quit()
