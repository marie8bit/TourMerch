import DBManager, choiceProcessor
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

if __name__ == '__main__':
    main()
