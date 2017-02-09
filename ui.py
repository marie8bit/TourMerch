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
def addNewItem():
    desc = input('Enter the new item\'s description: ')
    val = getPositiveFloat(input('Enter the price: '))
    DBManager.addNewObject('Item', desc, val)

def addNewPerformance():
    iyear = getPositiveInt(input('Enter the year of the performance: '))
    imonth = getPositiveInt(input('Enter the month of the performance: '))
    iday = getPositiveInt(input('Enter the day of the month of the performance: '))
    locCity = input('Enter the city of the performance: ')
    locState = input('Enter the State of the city of the performance: ')
    DBManager.addNewObject('Performance', iyear, imonth, iday, locCity, locState)

def addNewSale():
    DBManager.showAll(Item)
    iID = getPositiveInt(input('Enter the ID number of the item sold: '))
    desc = DBManager.getObjectByID('Item', iID)
    item = desc.description
    iquantity = getPositiveInt(input('Enter the amount of '+ item +' sold: '))
    DBManager.showAll(Performance)
    iperfID = getPositiveInt(input('Enter the ID of the performance where the item(s) were sold: '))
    perf = DBManager.getObjectByID('Performance', iperfID)
    DBManager.addNewObject('Sale', desc.id, iquantity, perf.id)

def getTSpI():
    DBManager.showAll(Item)
    iID = getPositiveInt(input('Enter the ID number of the item: '))
    DBManager.getSalesByID(iID)

def getTSpP():
    DBManager.showAll(Performance)
    pID = getPositiveInt(input('Enter the ID number of the performance: '))
    DBManager.getSalesByPerf(pID)

if __name__ == '__main__':
    main()
