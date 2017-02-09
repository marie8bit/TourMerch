import DBManager, choiceProcessor
from merchSales import Sale
from items import Item
import items
from performances import Performance
def main():
    #initializes database or reads data from the database file
    DBManager.setup()
    quit = 'q'
    choice = None
    #allow users to loop through choices until they quit
    while choice != quit:
        choice = display_menu_get_choice()
        choiceProcessor.handle_choice(choice)

#displays options to user
def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show items for sale
        2. Add a new item
        3. Add a new performance
        4. Add a new sale
        5. Get total sales per item
        6. Get total sales per performance
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice
#validates user input data
def getPositiveInt(string):
    #loops until it gets valid user data
    while True:
        #handles common user input errors
        try:
            id = int(string)
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
                string = input()

        except ValueError:
            print('Please enter an integer number')
            string = input()
#validates float data type for item value attribute
def getPositiveFloat(string):
    while True:
        try:
            id = float(string)
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
                string = input()

        except ValueError:
            print('Please enter a numerical value')
            string = input()
#gets item data from user
def addNewItem():
    desc = input('Enter the new item\'s description: ')
    val = getPositiveFloat(input('Enter the price: '))
    #sends data to dbManager to add object to database
    DBManager.addNewObject('Item', desc, val)
#gets performance data from user
def addNewPerformance():
    iyear = getPositiveInt(input('Enter the year of the performance: '))
    imonth = getPositiveInt(input('Enter the month of the performance: '))
    iday = getPositiveInt(input('Enter the day of the month of the performance: '))
    locCity = input('Enter the city of the performance: ')
    locState = input('Enter the State of the city of the performance: ')
    #sends data to dbManager to add object to database
    DBManager.addNewObject('Performance', iyear, imonth, iday, locCity, locState)
#gets sales data form user
def addNewSale():
    #displays items to aid user in identifying id numbers for foreign keys
    itemList = DBManager.showAll(Item)
    for ob in itemList:
        print(ob)
    iID = getPositiveInt(input('Enter the ID number of the item sold: '))
    #gets the item object to access its description attribute and valid foreign key
    desc = DBManager.getObjectByID('Item', iID)
    item = desc.description
    #uses description instead of ID for user freindly interface
    iquantity = getPositiveInt(input('Enter the amount of '+ item +' sold: '))
    #displays performances to aid user in identifying id numbers for foreign keys
    perfList = DBManager.showAll(Performance)
    for ob in perfList:
        print(ob)
    iperfID = getPositiveInt(input('Enter the ID of the performance where the item(s) were sold: '))
    #validates the existance of an object before trying to add sales item to db
    perf = DBManager.getObjectByID('Performance', iperfID)
    DBManager.addNewObject('Sale', desc.id, iquantity, perf.id)

def getTSpI():
    #provides user with a list of items to aid in identifying ID number
    itemList = DBManager.showAll(Item)
    for ob in itemList:
        print(ob)
    iID = getPositiveInt(input('Enter the ID number of the item: '))
    #calls method to query the database for sales by item ID
    DBManager.getSalesByID(iID)

def getTSpP():
    #provides user with a list of items to aid in identifying ID number
    #and identifies if there are no performances to query
    perfList = DBManager.showAll(Performance)
    if not perfList:
        print ('No performances in databse, try adding a new performance')
    else:
        for ob in perfList:
            print(ob)
        pID = getPositiveInt(input('Enter the ID number of the performance: '))
        #calls method to query the database for sales by performance ID
        DBManager.getSalesByPerf(pID)

if __name__ == '__main__':
    main()
