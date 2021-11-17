def home_pg():
    print("""
    -------------------------------------------
    ----ONLINE FOOD ORDER MANAGEMENT SYSTEM----
    -WELCOME TO SPIDERMAN ONLINE FOOD SERVICES-
    -------------------------------------------

    Choose your option (1-4)
    1.View as Guest
    2.Login as Customer
    3.Login as Admin
    4.Exit
    """)
    home_pg_choice = input(">>> ")
    if home_pg_choice == "1":
        # call guest_menu function
        guest_menu()

    elif home_pg_choice == "2":
        # call customer login function
        cs_login_pg()

    elif home_pg_choice == "3":
        # call admin login function
        adm_login_pg()

    elif home_pg_choice == "4":
        # call exit function
        exit()

    else:
        print("Invalid code! Please try again.")
        # call home page function
        home_pg()


def admin_pg():
    print("""
    <<<<<<<<<<<<<<ADMIN>>>>>>>>>>>>>>>
    1. Add Item
    2. Modify Item
    3. Remove Item
    4. View Food Categories
    5. View Menu
    6. Display Order Record
    7. Display Payment Record
    8. LOGOUT""")
    admin_choice = input(">>> ")
    if admin_choice == "1":
        # call add menu function
        adm_addMenu()
    elif admin_choice == "2":
        adm_modifyMenu()
    elif admin_choice == "3":
        # call remove menu function
        adm_removeMenu()
    elif admin_choice == "4":
        menu_category_only()
    elif admin_choice == "5":
        # call menu function
        menu_only()
        back = input('\nPress (B) to Back >>> ')
        if back == 'B':
            admin_pg()
        else:
            print("Invalid code! Please try again.")
            menu_only()
    elif admin_choice == '6':
        # call search order function
        adm_order_search()
    elif admin_choice == '7':
        # call search payment function
        adm_payment_search()
    elif admin_choice == '8':
        # call home page function
        home_pg()
    else:
        print('invalid, please choose again!!!')
        admin_pg()


def adm_addMenu():
    additem = input("""
            <Add Item>
    -----FOOD CATEGORIES-----
        1. Appetizers
        2. Soup
        3. Noodles
        4. Rice
        5. Beverages

    Please select a category (1-5):
    (Enter "B" to back)
    >>> """)
    if additem == '1':
        while True:
            print("\n>>>>>>>>>>>>>>>>>>>>Add Item<<<<<<<<<<<<<<<<<<<<<")
            print("\nExisting appetizers menu:")
            # call function to print menu
            menu_appetizers()
            # call function to add appetizers
            add_menu_appetizers()
    elif additem == '2':
        while True:
            print("\n>>>>>>>>>>>>>>>>>>>>Add Item<<<<<<<<<<<<<<<<<<<<<")
            print("\nExisting soup menu:")
            # call function to print menu
            menu_soup()
            # call function to add soup
            add_menu_soup()
    elif additem == '3':
        while True:
            print("\n>>>>>>>>>>>>>>>>>>>>Add Item<<<<<<<<<<<<<<<<<<<<<")
            print("\nExisting noodles menu:")
            # call function to print menu
            menu_noodles()
            # call function to add noodles
            add_menu_noodles()
    elif additem == '4':
        while True:
            print("\n>>>>>>>>>>>>>>>>>>>>Add Item<<<<<<<<<<<<<<<<<<<<<")
            print("\nExisting rice menu:")
            # call function to print menu
            menu_rice()
            # call function to add rice
            add_menu_rice()
    elif additem == '5':
        while True:
            print("\n>>>>>>>>>>>>>>>>>>>>Add Item<<<<<<<<<<<<<<<<<<<<<")
            print("\nExisting beverages menu:")
            # call function to print menu
            menu_beverages()
            # call function to add beverages
            add_menu_beverages()
    elif additem == 'B':
        # call function to back to admin page
        admin_pg()
    else:
        print("Invalid code! Please try again.")
        adm_addMenu()


def adm_removeMenu():
    removeitem = input("""
          <Remove Item>
    -----FOOD CATEGORIES-----
        1. Appetizers
        2. Soup
        3. Noodles
        4. Rice
        5. Beverages
    \n(Enter "B" to back)
    Please select an option (1-5):
    >>> """)
    if removeitem == '1':
        while True:
            print(">>>>>>>>>>>>>>>>>>>Remove Item<<<<<<<<<<<<<<<<<<<")
            # call function to remove appetizers
            remove_menu_appetizers()
            print("\nUpdated!")
    elif removeitem == '2':
        while True:
            print(">>>>>>>>>>>>>>>>>>>Remove Item<<<<<<<<<<<<<<<<<<<")
            # call function to remove soup
            remove_menu_soup()
            print("\nUpdated!")
    elif removeitem == '3':
        while True:
            print(">>>>>>>>>>>>>>>>>>>Remove Item<<<<<<<<<<<<<<<<<<<")
            # call function to remove noodles
            remove_menu_noodles()
            print("\nUpdated!")
    elif removeitem == '4':
        while True:
            print(">>>>>>>>>>>>>>>>>>>Remove Item<<<<<<<<<<<<<<<<<<<")
            # call function to remove rice
            remove_menu_rice()
            print("\nUpdated!")
    elif removeitem == '5':
        while True:
            print(">>>>>>>>>>>>>>>>>>>Remove Item<<<<<<<<<<<<<<<<<<<")
            # call function to remove beverages
            remove_menu_beverages()
            print("\nUpdated!")
    elif removeitem == 'B':
        # call function to back to admin page
        admin_pg()


def adm_modifyMenu():
    modifyitem = input("""
          <Modify Item>
    -----FOOD CATEGORIES-----
        1. Appetizers
        2. Soup
        3. Noodles
        4. Rice
        5. Beverages

    Please select a category (1-5):
    (Enter "B" to back)
>>> """)
    if modifyitem == '1':
        # call function to modify appetizer
        modify_appetizer()
    elif modifyitem == '2':
        # call function to modify soup
        modify_soup()
    elif modifyitem == '3':
        # call function to modify noodles
        modify_noodles()
    elif modifyitem == '4':
        # call function to modify rice
        modify_rice()
    elif modifyitem == '5':
        # call function to modify beverages
        modify_beverages()
    elif modifyitem == 'B':
        # call function to back to admin page
        admin_pg()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        adm_modifyMenu()


def menu_only():
    print("<<<<<<<<<<<<<<<<<<<<<MENU>>>>>>>>>>>>>>>>>>>>>\n")
    # call function to print appetizers menu
    menu_appetizers()
    print("")
    # call function to print soup menu
    menu_soup()
    print("")
    # call function to print noodles menu
    menu_noodles()
    print("")
    # call function to print rice menu
    menu_rice()
    print("")
    # call function to print beverages menu
    menu_beverages()


# ck

def menu_category_only():
    category_choice = input("""
    <<<<<<<<<<<<<Food Categories>>>>>>>>>>>>>

    1. Appetizer
    2. Soup
    3. Noodles
    4. Rice
    5. Beverages

    Please select an option (1-2):
    1. View Menu
    2. Back
>>> """)
    if category_choice == "1":
        menu_only()
        back = input('\nPress (B) to Back >>> ')
        if back == 'B':
            admin_pg()
        else:
            print("Invalid code! Please try again.")
            menu_only()
    elif category_choice == "2":
        admin_pg()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        menu_category_only()


def guest_menu():
    # call menu function
    menu_only()
    menu_choice = input("""
    Please select a following option (1-2):
    1. Take Order
    2. Back to Home Page
>>> """)
    # guest have to log in an account to take order
    if menu_choice == "1":
        print("\nSorry, you have to log in to an account to take order.")
        cs_login_pg()
    # call function to back to home page
    elif menu_choice == "2":
        home_pg()
    else:
        print("Invalid, Please Try Again!")
        guest_menu()


def registered_menu():
    print("""
    <<<<<<<<<<<<<<<CUSTOMER PAGE<<<<<<<<<<<<<<<""")
    menu_choice = input("""
    Please select a following option (1-4):
    1. View Menu
    2. View Item Cart
    3. View Order History
    4. LOGOUT

>>> """)
    if menu_choice == "1":
        # call function to show food categories
        menu_with_categories()
    elif menu_choice == "2":
        # call function to view item cart
        cs_itemCart_menu()
    elif menu_choice == "3":
        # call function to view order history
        cs_order_history()
    elif menu_choice == "4":
        # call function to exit program
        exit()
    else:
        print("Invalid code! Please Try Again.")
        # loop for invalid data
        registered_menu()


def menu_with_categories():
    category_choice = input("""
    <<<<<<<<<<<<<Food Categories>>>>>>>>>>>>>

    1. Appetizer
    2. Soup
    3. Noodles
    4. Rice
    5. Beverages
    6. VIEW ALL

    Please select a category to view items (1-6):
    [Enter "B" to back.]

>>> """)
    if category_choice == "1":
        # call specific menu
        menu_appetizers()
        menu_choice = input("""
    Please select a following option (1-2):
    1. Take Order
    2. Back
>>> """)
        if menu_choice == "1":
            # call function to add item into cart
            take_order_pg()
        elif menu_choice == "2":
            # provide back function
            menu_with_categories()
        else:
            # loop for invalid code
            print("Invalid code! Please Try Again.")
            menu_with_categories()

    elif category_choice == "2":
        # call specific menu
        menu_soup()
        menu_choice = input("""
    Please select a following option (1-2):
    1. Take Order
    2. Back
 >>> """)
        if menu_choice == "1":
            # call function to add item into cart
            take_order_pg()
        elif menu_choice == "2":
            # provide back function
            menu_with_categories()
        else:
            # loop for invalid code
            print("Invalid code! Please Try Again.")
            menu_with_categories()

    elif category_choice == "3":
        # call specific menu
        menu_noodles()
        menu_choice = input("""
    Please select a following option (1-2):
    1. Take Order
    2. Back
>>> """)
        if menu_choice == "1":
            # call function to add item into cart
            take_order_pg()
        elif menu_choice == "2":
            # provide back function
            menu_with_categories()
        else:
            # loop for invalid code
            print("Invalid code! Please Try Again.")
            menu_with_categories()

    elif category_choice == "4":
        # call specific menu
        menu_rice()
        menu_choice = input("""
    Please select a following option (1-2):
    1. Take Order
    2. Back
>>> """)
        if menu_choice == "1":
            # call function to add item into cart
            take_order_pg()
        elif menu_choice == "2":
            # provide back function
            menu_with_categories()
        else:
            # loop for invalid code
            print("Invalid code! Please Try Again.")
            menu_with_categories()

    elif category_choice == "5":
        # call specific menu
        menu_beverages()
        menu_choice = input("""
    Please select a following option (1-2):
    1. Take Order
    2. Back
>>> """)
        if menu_choice == "1":
            # call function to add item into cart
            take_order_pg()
        elif menu_choice == "2":
            # provide back function
            menu_with_categories()
        else:
            # loop for invalid code
            print("Invalid code! Please Try Again.")
            menu_with_categories()

    elif category_choice == "6":
        # call all menu function
        menu_only()
        menu_choice = input("""
    Please select a following option (1-2):
    1. Take Order
    2. Back
>>> """)
        if menu_choice == "1":
            # call function to add item into cart
            take_order_pg()
        elif menu_choice == "2":
            # provide back function
            menu_with_categories()
        else:
            # loop for invalid code
            print("Invalid code! Please Try Again.")
            menu_with_categories()
    elif category_choice == "B":
        # provide back function
        registered_menu()
    else:
        # loop for invalid code
        print("Invalid code! Please Try Again.")
        menu_with_categories()


#########################################CS_LOGIN##################################################
def cs_new_username():
    # create empty list
    temp_username_list = []
    # open customer's username and password text file
    cs_username_list = open("cs_usernpass_list.txt", "r")
    # get all exist usernames in text fie and put into temp_uername_list
    for line in cs_username_list.readlines():
        # split data in each line with ";" symbol
        data = line.split(";")
        # first data for each line are usernames
        username = data[0]
        # add username to the list
        temp_username_list.append(username)
    # close text file
    cs_username_list.close()

    print("""\n:::::::::Account Registration:::::::::
(Enter "B" to back.) 
""")
    # get username from new user
    cs_username = input("""Please enter a username: """)
    if cs_username != "B":
        # check the username is taken or not
        if cs_username in temp_username_list:
            # loop when username is invalid
            print("This username is currently taken, please use another username.")
            cs_new_username()
        else:
            # add new username to username and password text file if valid
            cs_username_list = open("cs_usernpass_list.txt", "a")
            cs_username_list.write(cs_username + ";")
            cs_username_list.close()
            # call password function
            cs_new_password()
    # back to login page
    elif cs_username == "B":
        cs_login_pg()


def cs_new_password():
    # get new password from user
    cs_password = input("Please enter a password (at least 4 characters): ")
    # check if password is longer than 3 character
    if len(cs_password) >= 4:
        # add password to username and password text file if valid
        cs_password_list = open("cs_usernpass_list.txt", "a")
        cs_password_list.write(cs_password + ";" + "\n")
        cs_password_list.close()
        print("""
Register successfully!\nYou are now directed to the login page.""")
        # back to login page to login
        cs_login_pg()
    else:
        # loop when password is invalid
        print("This password is too short, please try again.")
        cs_new_password()


def cs_login_pg():
    login_choice = input("""
    ----------------------------
    ---------LOGIN PAGE---------
    ----------------------------
    Choose your option (0-1):
    0. Sign Up as New Customer
    1. Login to Existing Account
    2. Back
>>> """)
    if login_choice == "0":
        # call function to register username
        cs_new_username()
    elif login_choice == "1":
        print("""\n:::::::::::::::::::::LOGIN:::::::::::::::::::::
(Enter "B" to back.)\n""")
        cs_exist_username = input("Please enter your username: ")
        # provide "back" function
        if cs_exist_username == "B":
            cs_login_pg()
        else:
            cs_exist_password = input("Please enter your password: ")
            # provide "back" function
            if cs_exist_password == "B":
                cs_login_pg()
            else:
                # create empty list to keep exist usernames
                temp_username_list = []
                # create empty list to keep exist password
                temp_password_list = []
                # create empty list to keep repeated password index value
                temp_password_index = []

                # open username and password text file in read mode
                cs_usernpass_list = open("cs_usernpass_list.txt", "r")
                # read and get all username and password
                for line in cs_usernpass_list.readlines():
                    data = line.split(";")
                    username = data[0]
                    password = data[1]
                    # put usernames into temp_username_list
                    temp_username_list.append(username)
                    # put passwords into temp_username_list
                    temp_password_list.append(password)
                cs_usernpass_list.close()

                # append all index value of repeated password to temp_password_index list
                for i in range(0, len(temp_password_list)):
                    if temp_password_list[i] == cs_exist_password:
                        temp_password_index.append(i)

                # check password given by user exist or not
                if cs_exist_password in temp_password_list:
                    # check whether given username is exist/ check whether username and password are matched
                    if (cs_exist_username in temp_username_list and
                            temp_username_list.index(cs_exist_username) in temp_password_index):
                        print(f"\nLogin Successfully!\nWelcome {cs_exist_username.upper()}.")
                        registered_menu()
                    else:
                        # loop if invalid credentials
                        print("Invalid username or password! Please try again.")
                        cs_login_pg()
                else:
                    # loop if invalid credentials
                    print("Invalid username or password! Please try again.")
                    cs_login_pg()

    elif login_choice == "2":
        # back to home page
        home_pg()
    else:
        # loop for invalid code
        print("Invalid, Please Try Again!")
        cs_login_pg()


#########################################ADMIN_LOGIN##################################################
def adm_login_pg():
    print("---------------ADMIN LOGIN PAGE---------------\n")
    adm_exist_username = input("""
(Enter "B" to back)
Please enter your username: """)
    adm_exist_password = input("Please enter your password: ")

    # create empty list to store all username in admin username and password text file
    temp_username_list = []
    # create empty list to store all password in admin username and password text file
    temp_password_list = []
    if adm_exist_username != "B":
        # open admin username and password text file in "r" mode
        adm_usernpass_list = open("adm_usernpass_list.txt", "r")
        # get data from text file
        for line in adm_usernpass_list.readlines():
            data = line.split(";")
            username = data[0]
            password = data[1]
            # add username to temp_username_list list
            temp_username_list.append(username)
            # add password to temp_password_list list
            temp_password_list.append(password)
        adm_usernpass_list.close()

        # check password given by user exist or not
        if adm_exist_password in temp_password_list:
            # check whether given username is exist/ check whether username and password are matched
            if (adm_exist_username in temp_username_list and
                    temp_username_list.index(adm_exist_username) == temp_password_list.index(adm_exist_password)):
                print(f"\nLogin Successfully!\nWelcome {adm_exist_username.upper()}.\n")
                admin_pg()
            else:
                # loop if invalid credentials
                print("Invalid username or password! Please try again.")
                adm_login_pg()
        else:
            # loop if invalid credentials
            print("Invalid username or password! Please try again.")
            adm_login_pg()
    elif adm_exist_username == "B":
        home_pg()


###############################################Menu###############################################################
def menu_appetizers():
    print("::::::::::::::::APPETIZERS::::::::::::::::" + " " * 2 + "RM")

    # create empty list
    temp_list = []
    # initialize records to 0
    records = 0
    menu_appetizer_list = open("menu_appetizer_list.txt", "r")
    # looping to search for the largest itemCode in menu text file
    for item in menu_appetizer_list.readlines():
        data = item.split(";")
        itemCode = data[0]
        # if itemCode larger than value of records, replace the temp_list with the Code
        if int(itemCode[1:4]) > records:
            temp_list.clear()
            temp_list.append(int(itemCode[1:4]))
            # replcae the value of records to the larger Code
            records = int(itemCode[1:4])
    menu_appetizer_list.close()

    # repeat based on the largest itemCode
    for i in range(0, temp_list[0] + 1):
        # open appetizer menu text file
        menu_appetizer_list = open("menu_appetizer_list.txt", "r")
        # Seperate data in text file
        for line in menu_appetizer_list:
            data = line.split(";")
            itemCode = data[0]
            itemDescription = data[1]
            itemPrice = data[2]
            if i == int(itemCode[1:4]):
                # calculate the total spaces consume by itemCode and itemDescription
                length_in_digit = len(itemCode + itemDescription)
                # to print the itemPrice at an exact location
                price_location = 40 - length_in_digit
                print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
        menu_appetizer_list.close()


def add_menu_appetizers():
    new_itemCode = input("""
(Enter "B" to back)
Please enter NEW item code (Ex:A1234): """)
    # open itemCode text file in "r" mode
    itemCode_list = open("itemCode_list.txt", "r")

    # create empty list to store the existing itemCode
    temp_itemCode = []

    # get itemCode from text file
    for code in itemCode_list.readlines():
        data = code.split(";")
        itemCode = data[0]
        # add existing itemCode into temp_itemCode list
        temp_itemCode.append(itemCode)

    if new_itemCode != "B":
        # check new itemCode from user is existed or not
        # data validation for new itemCode
        if (new_itemCode not in temp_itemCode and len(new_itemCode) == 4):

            # close the read only text file
            itemCode_list.close()

            # open itemCode text file again in "a" mode
            itemCode_list = open("itemCode_list.txt", "a")
            # open appetizer menu text file in "a" mode
            menu_appetizer_list = open("menu_appetizer_list.txt", "a")

            # store new itemCode into itemCode text file
            itemCode_list.write(new_itemCode + ";" + "\n")
            itemDescription = input("Please enter NEW item Description: ")
            itemPrice = input("Please enter a price for item: RM")

            # store itemCode, itemDescription and itemPrice into appetizer menu text file
            menu_appetizer_list.write(new_itemCode + "; " + itemDescription + "; " + itemPrice + "; " + "\n")
            print("""
Updated!""")
            menu_appetizer_list.close()
            itemCode_list.close()
        else:
            # loop for invalid data
            print("""
Invalid code or code is taken. Please enter another code.""")
            add_menu_appetizers()

    elif new_itemCode == "B":
        ##MODIFY FUNCTION##
        temp_keep_item = open("temp_keep_order.txt", "r")
        menu_appetizers = open("menu_appetizer_list.txt", "a")
        ##write item details back to menu if user cancel process##
        for item in temp_keep_item.readlines():
            menu_appetizers.write(item)
        temp_keep_item.close()
        menu_appetizers.close()
        ##write item code back to itemCode text file if user cancel process##
        temp_keep_item = open("temp_keep_order.txt", "r")
        itemCode_list = open("itemCode_list.txt", "a")
        for item in temp_keep_item.readlines():
            data = item.split(";")
            itemCode = data[0]
            itemCode_list.write(itemCode + ";\n")
        temp_keep_item.close()
        itemCode_list.close()

        # provide "back" function
        admin_pg()


def remove_menu_appetizers():
    # call function to print menu
    menu_appetizers()
    remove_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:A1234): """)

    if remove_itemCode != "B":
        # create empty list to store exist itemCode
        exist_code_list = []
        itemCode_list = open("itemCode_list.txt", "r")
        for codes in itemCode_list.readlines():
            data = codes.split(";")
            code = data[0]
            exist_code_list.append(code)
        itemCode_list.close()

        # if itemCode given is in the list
        if remove_itemCode in exist_code_list:
            # open appetizer menu text file in "r" mode
            menu_appetizer_list = open('menu_appetizer_list.txt', 'r')

            # create a empty list to store items that are needed
            temp_list = []

            # get data line by line in appetizer menu text file
            # get itemCode from appetizer menu text file
            for line in menu_appetizer_list.readlines():
                data = line.split(";")
                itemCode = data[0]

                # add the items that are needed to be kept to temp_list list
                if not itemCode == remove_itemCode:
                    temp_list.append(line)

                ##FOR MODIFY ITEM FUNCTION##
                # overwrite temp_keep_order text file to items that are needed to be modify
                elif itemCode == remove_itemCode:
                    temp_keep_item = open("temp_keep_order.txt", "w")
                    temp_keep_item.write(line)
                    temp_keep_item.close()

            # close read only appetizer menu text file
            menu_appetizer_list.close()
            # open appetizer menu in "w" mode
            menu_appetizer_list = open("menu_appetizer_list.txt", "w")

            # overwrite the appetizer menu text file with items info stored in temp_list list
            for item in temp_list:
                menu_appetizer_list.write(item)
            menu_appetizer_list.close()

            # same step to remove itemCode from itemCode text file#
            # create empty list to store needed itemCode
            temp_itemCode = []

            itemCode_list = open("itemCode_list.txt", "r")
            for code in itemCode_list.readlines():
                data = code.split(";")
                itemCode = data[0]
                # store needed itemCode to the list
                if not itemCode == remove_itemCode:
                    temp_itemCode.append(code)
            itemCode_list.close()
            # overwrite itemCode_list with item in temp_itemCode list
            itemCode_list = open("itemCode_list.txt", "w")
            for code in temp_itemCode:
                itemCode_list.write(code)
            itemCode_list.close()
        else:
            # loop for invalid data
            print("\nInvalid code! Please try again.\n")
            remove_menu_appetizers()
    elif remove_itemCode == "B":
        # provide "back" function
        admin_pg()


def modify_appetizer():
    print("\n>>>>>>>>>>>>>>>>>>>Modify Item<<<<<<<<<<<<<<<<<<<\n")
    remove_menu_appetizers()
    temp_keep_item = open("temp_keep_order.txt", "r")
    for item in temp_keep_item.readlines():
        data = item.split(";")
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemDescription)
        # to print the itemPrice at an exact location
        price_location = 40 - length_in_digit
        print("\n            <CURRENT MODIFY ITEM>")
        print("::::::::::::::::APPETIZERS::::::::::::::::" + " " * 2 + "RM")
        print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
        break
    add_menu_appetizers()
    menu_appetizers()
    temp_keep_item = open("temp_keep_order.txt", "r+")
    temp_keep_item.truncate(0)
    temp_keep_item.close()
    modify_appetizer()


def menu_soup():
    print(":::::::::::::::::::SOUP:::::::::::::::::::" + "  RM")

    # create empty list
    temp_list = []
    # initialize records to 0
    records = 0
    menu_soup_list = open("menu_soup_list.txt", "r")
    # looping to search for the largest itemCode in menu text file
    for item in menu_soup_list.readlines():
        data = item.split(";")
        itemCode = data[0]
        # if itemCode larger than value of records, replace the temp_list with the Code
        if int(itemCode[1:4]) > records:
            temp_list.clear()
            temp_list.append(int(itemCode[1:4]))
            # replace the value fo records to the largest Code
            records = int(itemCode[1:4])
    menu_soup_list.close()

    # repeat based on number of records
    for i in range(0, temp_list[0] + 1):
        # open appetizer menu text file
        menu_soup_list = open("menu_soup_list.txt", "r")
        # Seperate data in text file
        for line in menu_soup_list:
            data = line.split(";")
            itemCode = data[0]
            itemDescription = data[1]
            itemPrice = data[2]
            if i == int(itemCode[1:4]):
                # calculate the total spaces consume by itemCode and itemDescription
                length_in_digit = len(itemCode + itemDescription)
                # to print the itemPrice at an exact location
                price_location = 40 - length_in_digit
                print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
                # count += 1
        menu_soup_list.close()


def add_menu_soup():
    new_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:B1234): """)
    # open itemCode text file in "r" mode
    itemCode_list = open("itemCode_list.txt", "r")

    # create empty list to store the existing itemCode
    temp_itemCode = []

    # get itemCode from text file
    for code in itemCode_list.readlines():
        data = code.split(";")
        itemCode = data[0]
        # add existing itemCode into temp_itemCode list
        temp_itemCode.append(itemCode)

    if new_itemCode != "B":
        # check new itemCode from user is existed or not
        # data validation for new itemCode
        if (new_itemCode not in temp_itemCode and len(new_itemCode) == 4):
            # close the read only text file
            itemCode_list.close()

            # open itemCode text file again in "a" mode
            itemCode_list = open("itemCode_list.txt", "a")
            # open appetizer menu text file in "a" mode
            menu_soup_list = open("menu_soup_list.txt", "a")

            # store new itemCode into itemCode text file
            itemCode_list.write(new_itemCode + ";" + "\n")
            itemDescription = input("Please enter a item Description: ")
            itemPrice = input("Please enter a price for item: RM")

            # store itemCode, itemDescription and itemPrice into appetizer menu text file
            menu_soup_list.write(new_itemCode + "; " + itemDescription + "; " + itemPrice + "; " + "\n")
            print("""
Updated!""")
            menu_soup_list.close()
            itemCode_list.close()
        else:
            # loop for invalid data
            print("""
Invalid code or code is taken. Please enter another code.""")
            add_menu_soup()
    elif new_itemCode == "B":
        ##MODIFY FUNCTION##
        temp_keep_item = open("temp_keep_order.txt", "r")
        menu_soup = open("menu_soup_list.txt", "a")
        ##write item details back to menu if user cancel process##
        for item in temp_keep_item.readlines():
            menu_soup.write(item)
        temp_keep_item.close()
        menu_soup.close()
        ##write item code back to itemCode text file if user cancel process##
        temp_keep_item = open("temp_keep_order.txt", "r")
        itemCode_list = open("itemCode_list.txt", "a")
        for item in temp_keep_item.readlines():
            data = item.split(";")
            itemCode = data[0]
            itemCode_list.write(itemCode + ";\n")
        temp_keep_item.close()
        itemCode_list.close()

        # provide "back" function
        admin_pg()


def remove_menu_soup():
    # call function to print menu
    menu_soup()
    remove_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:A1234): """)

    if remove_itemCode != "B":
        # create empty list to store exist itemCode
        exist_code_list = []
        itemCode_list = open("itemCode_list.txt", "r")
        for codes in itemCode_list.readlines():
            data = codes.split(";")
            code = data[0]
            exist_code_list.append(code)
        itemCode_list.close()

        # if itemCode given is in the list
        if remove_itemCode in exist_code_list:
            # open appetizer menu text file in "r" mode
            menu_soup_list = open('menu_soup_list.txt', 'r')

            # create a empty list to store items that are needed
            temp_list = []

            # get data line by line in appetizer menu text file
            # get itemCode from appetizer menu text file
            for line in menu_soup_list.readlines():
                data = line.split(";")
                itemCode = data[0]

                # add the items that are needed to be kept to temp_list lsit
                if not itemCode == remove_itemCode:
                    temp_list.append(line)

                ##FOR MODIFY ITEM FUNCTION##
                # overwrite temp_keep_order text file to items that are needed to be modify
                elif itemCode == remove_itemCode:
                    temp_keep_item = open("temp_keep_order.txt", "w")
                    temp_keep_item.write(line)
                    temp_keep_item.close()

            # close read only appetizer menu text file
            menu_soup_list.close()
            # open appetizer menu in "w" mode
            menu_soup_list = open("menu_soup_list.txt", "w")

            # overwrite the appetizer menu text file with items info stored in temp_list list
            for item in temp_list:
                menu_soup_list.write(item)
            menu_soup_list.close()

            # same step to remove itemCode from itemCode text file#
            # create empty list to store needed itemCode
            temp_itemCode = []

            itemCode_list = open("itemCode_list.txt", "r")
            for code in itemCode_list.readlines():
                data = code.split(";")
                itemCode = data[0]
                # store needed itemCode to the list
                if not itemCode == remove_itemCode:
                    temp_itemCode.append(code)
            itemCode_list.close()
            # overwrite itemCode_list with item in temp_itemCode list
            itemCode_list = open("itemCode_list.txt", "w")
            for code in temp_itemCode:
                itemCode_list.write(code)
            itemCode_list.close()
        else:
            # loop for invalid data
            print("\nInvalid code! Please try again.\n")
            remove_menu_soup()
    elif remove_itemCode == "B":
        # provide "back" function
        admin_pg()


def modify_soup():
    print("\n>>>>>>>>>>>>>>>>>>>Modify Item<<<<<<<<<<<<<<<<<<<\n")
    remove_menu_soup()
    temp_keep_item = open("temp_keep_order.txt", "r")
    for item in temp_keep_item.readlines():
        data = item.split(";")
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemDescription)
        # to print the itemPrice at an exact location
        price_location = 40 - length_in_digit
        print("\n            <CURRENT MODIFY ITEM>")
        print("::::::::::::::::APPETIZERS::::::::::::::::" + " " * 2 + "RM")
        print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
        break
    add_menu_soup()
    menu_soup()
    temp_keep_item = open("temp_keep_order.txt", "r+")
    temp_keep_item.truncate(0)
    temp_keep_item.close()
    modify_soup()


def menu_noodles():
    print("::::::::::::::::::NOODLES:::::::::::::::::" + "  RM")

    # create empty list
    temp_list = []
    # initialize records to 0
    records = 0
    menu_noodles_list = open("menu_noodles_list.txt", "r")
    # looping to search for the largest itemCode in menu text file
    for item in menu_noodles_list.readlines():
        data = item.split(";")
        itemCode = data[0]
        # if itemCode larger than value of records, replace the temp_list with the Code
        if int(itemCode[1:4]) > records:
            temp_list.clear()
            temp_list.append(int(itemCode[1:4]))
            # replcae the value of records to the larger Code
            records = int(itemCode[1:4])
    menu_noodles_list.close()

    # repeat based on number of records
    for i in range(0, temp_list[0] + 1):
        # open appetizer menu text file
        menu_noodles_list = open("menu_noodles_list.txt", "r")
        # Seperate data in text file
        for line in menu_noodles_list:
            data = line.split(";")
            itemCode = data[0]
            itemDescription = data[1]
            itemPrice = data[2]
            if i == int(itemCode[1:4]):
                # calculate the total spaces consume by itemCode and itemDescription
                length_in_digit = len(itemCode + itemDescription)
                # to print the itemPrice at an exact location
                price_location = 40 - length_in_digit
                print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
                # count += 1
        menu_noodles_list.close()


def add_menu_noodles():
    new_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:C1234): """)
    # open itemCode text file in "r" mode
    itemCode_list = open("itemCode_list.txt", "r")

    # create empty list to store the existing itemCode
    temp_itemCode = []

    # get itemCode from text file
    for code in itemCode_list.readlines():
        data = code.split(";")
        itemCode = data[0]
        # add existing itemCode into temp_itemCode list
        temp_itemCode.append(itemCode)

    if new_itemCode != "B":
        # check new itemCode from user is existed or not
        # data validation for new itemCode
        if (new_itemCode not in temp_itemCode and len(new_itemCode) == 4):
            # close the read only text file
            itemCode_list.close()

            # open itemCode text file again in "a" mode
            itemCode_list = open("itemCode_list.txt", "a")
            # open appetizer menu text file in "a" mode
            menu_noodles_list = open("menu_noodles_list.txt", "a")

            # store new itemCode into itemCode text file
            itemCode_list.write(new_itemCode + ";" + "\n")
            itemDescription = input("Please enter a item Description: ")
            itemPrice = input("Please enter a price for item: RM")

            # store itemCode, itemDescription and itemPrice into appetizer menu text file
            menu_noodles_list.write(new_itemCode + "; " + itemDescription + "; " + itemPrice + "; " + "\n")
            print("""
Updated!""")
            menu_noodles_list.close()
            itemCode_list.close()
        else:
            # loop for invalid data
            print("""
Invalid code or code is taken. Please enter another code.""")
            add_menu_noodles()
    elif new_itemCode == "B":
        ##MODIFY FUNCTION##
        temp_keep_item = open("temp_keep_order.txt", "r")
        menu_noodles = open("menu_noodles_list.txt", "a")
        ##write item details back to menu if user cancel process##
        for item in temp_keep_item.readlines():
            menu_noodles.write(item)
        temp_keep_item.close()
        menu_noodles.close()
        ##write item code back to itemCode text file if user cancel process##
        temp_keep_item = open("temp_keep_order.txt", "r")
        itemCode_list = open("itemCode_list.txt", "a")
        for item in temp_keep_item.readlines():
            data = item.split(";")
            itemCode = data[0]
            itemCode_list.write(itemCode + ";\n")
        temp_keep_item.close()
        itemCode_list.close()

        # provide "back" function
        admin_pg()


def remove_menu_noodles():
    # call function to print menu
    menu_noodles()
    remove_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:A1234): """)

    if remove_itemCode != "B":
        # create empty list to store exist itemCode
        exist_code_list = []
        itemCode_list = open("itemCode_list.txt", "r")
        for codes in itemCode_list.readlines():
            data = codes.split(";")
            code = data[0]
            exist_code_list.append(code)
        itemCode_list.close()

        # if itemCode given is in the list
        if remove_itemCode in exist_code_list:
            # open appetizer menu text file in "r" mode
            menu_noodles_list = open('menu_noodles_list.txt', 'r')

            # create a empty list to store items that are needed
            temp_list = []

            # get data line by line in appetizer menu text file
            # get itemCode from appetizer menu text file
            for line in menu_noodles_list.readlines():
                data = line.split(";")
                itemCode = data[0]

                # add the items that are needed to be kept to temp_list lsit
                if not itemCode == remove_itemCode:
                    temp_list.append(line)

                ##FOR MODIFY ITEM FUNCTION##
                # overwrite temp_keep_order text file to items that are needed to be modify
                elif itemCode == remove_itemCode:
                    temp_keep_item = open("temp_keep_order.txt", "w")
                    temp_keep_item.write(line)
                    temp_keep_item.close()

            # close read only appetizer menu text file
            menu_noodles_list.close()
            # open appetizer menu in "w" mode
            menu_noodles_list = open("menu_noodles_list.txt", "w")

            # overwrite the appetizer menu text file with items info stored in temp_list list
            for item in temp_list:
                menu_noodles_list.write(item)
            menu_noodles_list.close()

            # same step to remove itemCode from itemCode text file#
            # create empty list to store needed itemCode
            temp_itemCode = []

            itemCode_list = open("itemCode_list.txt", "r")
            for code in itemCode_list.readlines():
                data = code.split(";")
                itemCode = data[0]
                # store needed itemCode to the list
                if not itemCode == remove_itemCode:
                    temp_itemCode.append(code)
            itemCode_list.close()
            # overwrite itemCode_list with item in temp_itemCode list
            itemCode_list = open("itemCode_list.txt", "w")
            for code in temp_itemCode:
                itemCode_list.write(code)
            itemCode_list.close()
        else:
            # loop for invalid data
            print("\nInvalid code! Please try again.\n")
            remove_menu_noodles()
    elif remove_itemCode == "B":
        # provide "back" function
        admin_pg()


def modify_noodles():
    print("\n>>>>>>>>>>>>>>>>>>>Modify Item<<<<<<<<<<<<<<<<<<<\n")
    remove_menu_noodles()
    temp_keep_item = open("temp_keep_order.txt", "r")
    for item in temp_keep_item.readlines():
        data = item.split(";")
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemDescription)
        # to print the itemPrice at an exact location
        price_location = 40 - length_in_digit
        print("\n            <CURRENT MODIFY ITEM>")
        print("::::::::::::::::APPETIZERS::::::::::::::::" + " " * 2 + "RM")
        print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
        break
    add_menu_noodles()
    menu_noodles()
    temp_keep_item = open("temp_keep_order.txt", "r+")
    temp_keep_item.truncate(0)
    temp_keep_item.close()
    modify_noodles()


def menu_rice():
    print(":::::::::::::::::::RICE:::::::::::::::::::" + "  RM")

    # create empty list
    temp_list = []
    # initialize records to 0
    records = 0
    menu_rice_list = open("menu_rice_list.txt", "r")
    # looping to search for the largest itemCode in menu text file
    for item in menu_rice_list.readlines():
        data = item.split(";")
        itemCode = data[0]
        # if itemCode larger than value of records, replace the temp_list with the Code
        if int(itemCode[1:4]) > records:
            temp_list.clear()
            temp_list.append(int(itemCode[1:4]))
            # replace the value of records to the larger Code
            records = int(itemCode[1:4])
    menu_rice_list.close()

    # repeat based on number of records
    for i in range(0, temp_list[0] + 1):
        # open appetizer menu text file
        menu_rice_list = open("menu_rice_list.txt", "r")
        # Seperate data in text file
        for line in menu_rice_list:
            data = line.split(";")
            itemCode = data[0]
            itemDescription = data[1]
            itemPrice = data[2]
            if i == int(itemCode[1:4]):
                # calculate the total spaces consume by itemCode and itemDescription
                length_in_digit = len(itemCode + itemDescription)
                # to print the itemPrice at an exact location
                price_location = 40 - length_in_digit
                print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
                # count += 1
        menu_rice_list.close()


def add_menu_rice():
    new_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:D1234): """)
    # open itemCode text file in "r" mode
    itemCode_list = open("itemCode_list.txt", "r")

    # create empty list to store the existing itemCode
    temp_itemCode = []

    # get itemCode from text file
    for code in itemCode_list.readlines():
        data = code.split(";")
        itemCode = data[0]
        # add existing itemCode into temp_itemCode list
        temp_itemCode.append(itemCode)

    if new_itemCode != "B":
        # check new itemCode from user is existed or not
        # data validation for new itemCode
        if (new_itemCode not in temp_itemCode and len(new_itemCode) == 4):
            # close the read only text file
            itemCode_list.close()

            # open itemCode text file again in "a" mode
            itemCode_list = open("itemCode_list.txt", "a")
            # open appetizer menu text file in "a" mode
            menu_rice_list = open("menu_rice_list.txt", "a")

            # store new itemCode into itemCode text file
            itemCode_list.write(new_itemCode + ";" + "\n")
            itemDescription = input("Please enter a item Description: ")
            itemPrice = input("Please enter a price for item: RM")

            # store itemCode, itemDescription and itemPrice into appetizer menu text file
            menu_rice_list.write(new_itemCode + "; " + itemDescription + "; " + itemPrice + "; " + "\n")
            print("""
Updated!""")
            menu_rice_list.close()
            itemCode_list.close()
        else:
            # loop for invalid data
            print("""
Invalid code or code is taken. Please enter another code.""")
            add_menu_rice()
    elif new_itemCode == "B":
        ##MODIFY FUNCTION##
        temp_keep_item = open("temp_keep_order.txt", "r")
        menu_rice = open("menu_rice_list.txt", "a")
        ##write item details back to menu if user cancel process##
        for item in temp_keep_item.readlines():
            menu_rice.write(item)
        temp_keep_item.close()
        menu_rice.close()
        ##write item code back to itemCode text file if user cancel process##
        temp_keep_item = open("temp_keep_order.txt", "r")
        itemCode_list = open("itemCode_list.txt", "a")
        for item in temp_keep_item.readlines():
            data = item.split(";")
            itemCode = data[0]
            itemCode_list.write(itemCode + ";\n")
        temp_keep_item.close()
        itemCode_list.close()

        # provide "back" function
        admin_pg()


def remove_menu_rice():
    # call function to print menu
    menu_rice()
    remove_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:A1234): """)

    if remove_itemCode != "B":
        # create empty list to store exist itemCode
        exist_code_list = []
        itemCode_list = open("itemCode_list.txt", "r")
        for codes in itemCode_list.readlines():
            data = codes.split(";")
            code = data[0]
            exist_code_list.append(code)
        itemCode_list.close()

        # if itemCode given is in the list
        if remove_itemCode in exist_code_list:
            # open appetizer menu text file in "r" mode
            menu_rice_list = open('menu_rice_list.txt', 'r')

            # create a empty list to store items that are needed
            temp_list = []

            # get data line by line in appetizer menu text file
            # get itemCode from appetizer menu text file
            for line in menu_rice_list.readlines():
                data = line.split(";")
                itemCode = data[0]

                # add the items that are needed to be kept to temp_list lsit
                if not itemCode == remove_itemCode:
                    temp_list.append(line)

                ##FOR MODIFY ITEM FUNCTION##
                # overwrite temp_keep_order text file to items that are needed to be modify
                elif itemCode == remove_itemCode:
                    temp_keep_item = open("temp_keep_order.txt", "w")
                    temp_keep_item.write(line)
                    temp_keep_item.close()

            # close read only appetizer menu text file
            menu_rice_list.close()
            # open appetizer menu in "w" mode
            menu_rice_list = open("menu_rice_list.txt", "w")

            # overwrite the appetizer menu text file with items info stored in temp_list list
            for item in temp_list:
                menu_rice_list.write(item)
            menu_rice_list.close()

            # same step to remove itemCode from itemCode text file#
            # create empty list to store needed itemCode
            temp_itemCode = []

            itemCode_list = open("itemCode_list.txt", "r")
            for code in itemCode_list.readlines():
                data = code.split(";")
                itemCode = data[0]
                # store needed itemCode to the list
                if not itemCode == remove_itemCode:
                    temp_itemCode.append(code)
            itemCode_list.close()
            # overwrite itemCode_list with item in temp_itemCode list
            itemCode_list = open("itemCode_list.txt", "w")
            for code in temp_itemCode:
                itemCode_list.write(code)
            itemCode_list.close()
        else:
            # loop for invalid data
            print("\nInvalid code! Please try again.\n")
            remove_menu_rice()
    elif remove_itemCode == "B":
        # provide "back" function
        admin_pg()


def modify_rice():
    print("\n>>>>>>>>>>>>>>>>>>>Modify Item<<<<<<<<<<<<<<<<<<<\n")
    remove_menu_rice()
    temp_keep_item = open("temp_keep_order.txt", "r")
    for item in temp_keep_item.readlines():
        data = item.split(";")
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemDescription)
        # to print the itemPrice at an exact location
        price_location = 40 - length_in_digit
        print("\n            <CURRENT MODIFY ITEM>")
        print("::::::::::::::::APPETIZERS::::::::::::::::" + " " * 2 + "RM")
        print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
        break
    add_menu_rice()
    menu_rice()
    temp_keep_item = open("temp_keep_order.txt", "r+")
    temp_keep_item.truncate(0)
    temp_keep_item.close()
    modify_rice()


def menu_beverages():
    print(":::::::::::::::::BEVERAGES::::::::::::::::" + "  RM")

    # create empty list
    temp_list = []
    # initialize records to 0
    records = 0
    menu_beverages_list = open("menu_beverages_list.txt", "r")
    # looping to search for the largest itemCode in menu text file
    for item in menu_beverages_list.readlines():
        data = item.split(";")
        itemCode = data[0]
        # if itemCode larger than value of records, replace the temp_list with the Code
        if int(itemCode[1:4]) > records:
            temp_list.clear()
            temp_list.append(int(itemCode[1:4]))
            # replcae the value of records to the larger Code
            records = int(itemCode[1:4])
    menu_beverages_list.close()

    # repeat based on number of records
    for i in range(0, temp_list[0] + 1):
        # open appetizer menu text file
        menu_beverages_list = open("menu_beverages_list.txt", "r")
        # Seperate data in text file
        for line in menu_beverages_list:
            data = line.split(";")
            itemCode = data[0]
            itemDescription = data[1]
            itemPrice = data[2]
            if i == int(itemCode[1:4]):
                # calculate the total spaces consume by itemCode and itemDescription
                length_in_digit = len(itemCode + itemDescription)
                # to print the itemPrice at an exact location
                price_location = 40 - length_in_digit
                print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
                # count += 1
        menu_beverages_list.close()


def add_menu_beverages():
    new_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:E1234): """)
    # open itemCode text file in "r" mode
    itemCode_list = open("itemCode_list.txt", "r")

    # create empty list to store the existing itemCode
    temp_itemCode = []

    # get itemCode from text file
    for code in itemCode_list.readlines():
        data = code.split(";")
        itemCode = data[0]
        # add existing itemCode into temp_itemCode list
        temp_itemCode.append(itemCode)

    if new_itemCode != "B":
        # check new itemCode from user is existed or not
        # data validation for new itemCode
        if (new_itemCode not in temp_itemCode and len(new_itemCode) == 4):
            # close the read only text file
            itemCode_list.close()

            # open itemCode text file again in "a" mode
            itemCode_list = open("itemCode_list.txt", "a")
            # open appetizer menu text file in "a" mode
            menu_beverages_list = open("menu_beverages_list.txt", "a")

            # store new itemCode into itemCode text file
            itemCode_list.write(new_itemCode + ";" + "\n")
            itemDescription = input("Please enter a item Description: ")
            itemPrice = input("Please enter a price for item: RM")

            # store itemCode, itemDescription and itemPrice into appetizer menu text file
            menu_beverages_list.write(new_itemCode + "; " + itemDescription + "; " + itemPrice + "; " + "\n")
            print("""
Updated!""")
            menu_beverages_list.close()
            itemCode_list.close()
        else:
            # loop for invalid data
            print("""
Invalid code or code is taken. Please enter another code.""")
            add_menu_beverages()
    elif new_itemCode == "B":
        ##MODIFY FUNCTION##
        temp_keep_item = open("temp_keep_order.txt", "r")
        menu_beverages = open("menu_beverages_list.txt", "a")
        ##write item details back to menu if user cancel process##
        for item in temp_keep_item.readlines():
            menu_beverages.write(item)
        temp_keep_item.close()
        menu_beverages.close()
        ##write item code back to itemCode text file if user cancel process##
        temp_keep_item = open("temp_keep_order.txt", "r")
        itemCode_list = open("itemCode_list.txt", "a")
        for item in temp_keep_item.readlines():
            data = item.split(";")
            itemCode = data[0]
            itemCode_list.write(itemCode + ";\n")
        temp_keep_item.close()
        itemCode_list.close()

        # provide "back" function
        admin_pg()


def remove_menu_beverages():
    # call function to print menu
    menu_beverages()
    remove_itemCode = input("""
(Enter "B" to back)
Please enter a item code (Ex:A1234): """)

    if remove_itemCode != "B":
        # create empty list to store exist itemCode
        exist_code_list = []
        itemCode_list = open("itemCode_list.txt", "r")
        for codes in itemCode_list.readlines():
            data = codes.split(";")
            code = data[0]
            exist_code_list.append(code)
        itemCode_list.close()

        # if itemCode given is in the list
        if remove_itemCode in exist_code_list:
            # open appetizer menu text file in "r" mode
            menu_beverages_list = open('menu_beverages_list.txt', 'r')

            # create a empty list to store items that are needed
            temp_list = []

            # get data line by line in appetizer menu text file
            # get itemCode from appetizer menu text file
            for line in menu_beverages_list.readlines():
                data = line.split(";")
                itemCode = data[0]

                # add the items that are needed to be kept to temp_list lsit
                if not itemCode == remove_itemCode:
                    temp_list.append(line)

                ##FOR MODIFY ITEM FUNCTION##
                # overwrite temp_keep_order text file to items that are needed to be modify
                elif itemCode == remove_itemCode:
                    temp_keep_item = open("temp_keep_order.txt", "w")
                    temp_keep_item.write(line)
                    temp_keep_item.close()

            # close read only appetizer menu text file
            menu_beverages_list.close()
            # open appetizer menu in "w" mode
            menu_beverages_list = open("menu_beverages_list.txt", "w")

            # overwrite the appetizer menu text file with items info stored in temp_list list
            for item in temp_list:
                menu_beverages_list.write(item)
            menu_beverages_list.close()

            # same step to remove itemCode from itemCode text file#
            # create empty list to store needed itemCode
            temp_itemCode = []

            itemCode_list = open("itemCode_list.txt", "r")
            for code in itemCode_list.readlines():
                data = code.split(";")
                itemCode = data[0]
                # store needed itemCode to the list
                if not itemCode == remove_itemCode:
                    temp_itemCode.append(code)
            itemCode_list.close()
            # overwrite itemCode_list with item in temp_itemCode list
            itemCode_list = open("itemCode_list.txt", "w")
            for code in temp_itemCode:
                itemCode_list.write(code)
            itemCode_list.close()
        else:
            # loop for invalid data
            print("\nInvalid code! Please try again.\n")
            remove_menu_beverages()
    elif remove_itemCode == "B":
        # provide "back" function
        admin_pg()


def modify_beverages():
    print("\n>>>>>>>>>>>>>>>>>>>Modify Item<<<<<<<<<<<<<<<<<<<\n")
    remove_menu_beverages()
    temp_keep_item = open("temp_keep_order.txt", "r")
    for item in temp_keep_item.readlines():
        data = item.split(";")
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemDescription)
        # to print the itemPrice at an exact location
        price_location = 40 - length_in_digit
        print("\n            <CURRENT MODIFY ITEM>")
        print("::::::::::::::::APPETIZERS::::::::::::::::" + " " * 2 + "RM")
        print(itemCode + "-" + itemDescription + " " * price_location, itemPrice)
        break
    add_menu_beverages()
    menu_beverages()
    temp_keep_item = open("temp_keep_order.txt", "r+")
    temp_keep_item.truncate(0)
    temp_keep_item.close()
    modify_beverages()


############################################ITEM CART############################################
def cs_itemCart_menu():
    # call function to print item in itemCart
    itemCart_items()
    item_cart_choice = input("""
    Please select an option (1-4):
    1. Main Menu
    2. Add Order
    3. Remove Item
    4. Proceed to Payment
>>> """)
    if item_cart_choice == "1":
        # back to main menu page
        registered_menu()
    elif item_cart_choice == "2":
        # call function to select item and add item to itemCart
        menu_with_categories()
    elif item_cart_choice == "3":
        # call function to remove item in itemCart
        remove_itemCart()
    elif item_cart_choice == "4":
        # check whether itemCart is empty by total Price
        cs_itemCart_list = open("cs_itemCart_list.txt", "r")
        # initialize item_price to 0
        total_price = 0
        # read data in text file line by line
        for item in cs_itemCart_list.readlines():
            data = item.split(";")
            itemPrice = float(data[2])
            # add all itemPrice to total_price
            total_price += itemPrice
        if total_price == 0:
            cart_payment_choice = input("""
    Your item cart is currently empty....

    Please select an option (1-2):
    1. Take order
    2. Back
>>> """)
            if cart_payment_choice == "1":
                # call function to select item and add item into itemCart
                menu_with_categories()
            elif cart_payment_choice == "2":
                # provide "back" function
                cs_itemCart_menu()
            else:
                # loop for invalid code
                print("Invalid code.")
                cs_itemCart_menu()
        else:
            # proceed to payment page
            payment_pg()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        cs_itemCart_menu()


def itemCart_items():
    print("""
-----------------------------------------------
-------------------ITEM CART-------------------
-----------------------------------------------

******************ITEM******************   RM""")
    # open item cart text file
    cs_itemCart_list = open("cs_itemCart_list.txt", "r")
    # initialize total_price = 0
    total_price = 0
    # read data in text file line by line
    for item in cs_itemCart_list.readlines():
        data = item.split(";")
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = float(data[2])
        # add all item price to total_price
        total_price += itemPrice
        # format of arrangemnet#
        length_in_digit = len(itemCode + itemDescription)
        price_location = 40 - length_in_digit
        print(itemCode + "-" + itemDescription + " " * price_location, "{:.2f}".format(itemPrice))
    cs_itemCart_list.close()
    print("\n", " " * 34, "---------------")
    print(" " * 35, "Total: RM", "{:.2f}".format(total_price))
    print(" " * 35, "---------------")


def remove_itemCart():
    # call function to print item in item cart
    itemCart_items()
    remove_item = input("""
Please enter the item code that you want to remove (Eg. A123):
(Enter "B" to back.)
>>> """)
    if remove_item == "B":
        # provide "back" function
        cs_itemCart_menu()
    else:
        # create empty list to store itemCode for item in item cart text file
        codes_in_itemCart = []
        cs_itemCart = open("cs_itemCart_list.txt", "r")
        for codes in cs_itemCart.readlines():
            data = codes.split(";")
            code = data[0]
            # put itemCode into the empty list
            codes_in_itemCart.append(code)

        if remove_item in codes_in_itemCart:
            cs_itemCart = open("cs_itemCart_list.txt", "r")
            # create empty listt to store itemCode for needed item
            temp_list = []
            # create empty list to store itemCode for removed item
            temp_remove_list = []
            # read itemCode in item cart text file
            for item in cs_itemCart.readlines():
                data = item.split(";")
                itemCode = data[0]
                if itemCode == remove_item:
                    if remove_item not in temp_remove_list:
                        temp_remove_list.append(itemCode)
                    else:
                        temp_list.append(item)
                elif itemCode != remove_item:
                    # codes not equal to given code store into temp_list
                    temp_list.append(item)
            cs_itemCart.close()
            # overwrite the item cart text file with new item list
            cs_itemCart = open("cs_itemCart_list.txt", "w")
            # add item in temp_list into item cart text file
            for item in temp_list:
                cs_itemCart.write(item)
            cs_itemCart.close()
            print("\nUpdated!")
            # call remove item cart function (looping)
            remove_itemCart()
        elif remove_item not in codes_in_itemCart:
            # looping for invalid code
            print("\nItem does not exist! Please try again.")
            remove_itemCart()


def invoice():
    print("""
******************ITEM******************   RM""")
    cs_itemCart_list = open("cs_itemCart_list.txt", "r")
    # initialize total_price = 0
    total_price = 0
    # read data in item cart text file
    for item in cs_itemCart_list.readlines():
        data = item.split(";")
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = float(data[2])
        # add all item price for item in item cart to total_price
        total_price += itemPrice
        # format of arrangement)
        length_in_digit = len(itemCode + itemDescription)
        price_location = 40 - length_in_digit
        print(itemCode + "-" + itemDescription + " " * price_location, "{:.2f}".format(itemPrice))
    print("\n", " " * 34, "---------------")
    print(" " * 35, "Total: RM", "{:.2f}".format(total_price))
    print(" " * 35, "---------------")


###############################################ORDER PAGE################################################
def take_order_pg():
    while True:
        order_code = input("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>ORDER<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Please enter the item code that you wish to add to your cart.
(Enter "Q" to quit) (Enter "V" to view item cart)
>>> """)
        # open appetizer text file if user input starts with A
        if order_code[0] == "A":
            menu_appetizers_list = open("menu_appetizer_list.txt", "r")
            # read data in text file
            for item in menu_appetizers_list.readlines():
                data = item.split(";")
                itemCode = data[0]
                itemDescription = data[1]
                itemPrice = data[2]
                # check whether input is exist
                if itemCode == order_code:
                    print(f"""
Item added to cart: {itemCode}- {itemDescription} """)
                    # open item cart text file and add item into text file
                    cs_itemCart = open("cs_itemCart_list.txt", "a")
                    cs_itemCart.write(itemCode + "; " + itemDescription + "; " + itemPrice + ";\n")
                    cs_itemCart.close()
                    break
            else:
                # Error message for invalid code
                print("Invalid item code! Please try again.")

        # open soup text file if user input starts with B
        elif order_code[0] == "B":
            menu_soup_list = open("menu_soup_list.txt", "r")
            # read data in text file
            for item in menu_soup_list.readlines():
                data = item.split(";")
                itemCode = data[0]
                itemDescription = data[1]
                itemPrice = data[2]
                # check whether input is exist
                if itemCode == order_code:
                    print(f"""
Item added to cart: {itemCode}- {itemDescription} """)
                    # open item cart text file and add item into text file
                    cs_itemCart = open("cs_itemCart_list.txt", "a")
                    cs_itemCart.write(itemCode + "; " + itemDescription + "; " + itemPrice + ";\n")
                    cs_itemCart.close()
                    break
            else:
                # Error message for invalid code
                print("Invalid item code! Please try again.")

        # open soup text file if user input starts with C
        elif order_code[0] == "C":
            menu_noodles_list = open("menu_noodles_list.txt", "r")
            # read data in text file
            for item in menu_noodles_list.readlines():
                data = item.split(";")
                itemCode = data[0]
                itemDescription = data[1]
                itemPrice = data[2]
                # check whether input is exist
                if itemCode == order_code:
                    print(f"""
Item added to cart: {itemCode}- {itemDescription} """)
                    # open item cart text file and add item into text file
                    cs_itemCart = open("cs_itemCart_list.txt", "a")
                    cs_itemCart.write(itemCode + "; " + itemDescription + "; " + itemPrice + ";\n")
                    cs_itemCart.close()
                    break
            else:
                # Error message for invalid code
                print("Invalid item code! Please try again.")

        # open soup text file if user input starts with D
        elif order_code[0] == "D":
            menu_rice_list = open("menu_rice_list.txt", "r")
            # read data in text file
            for item in menu_rice_list.readlines():
                data = item.split(";")
                itemCode = data[0]
                itemDescription = data[1]
                itemPrice = data[2]
                # check whether input is exist
                if itemCode == order_code:
                    print(f"""
Item added to cart: {itemCode}- {itemDescription} """)
                    # open item cart text file and add item into text file
                    cs_itemCart = open("cs_itemCart_list.txt", "a")
                    cs_itemCart.write(itemCode + "; " + itemDescription + "; " + itemPrice + ";\n")
                    cs_itemCart.close()
                    break
            else:
                # Error message for invalid code
                print("Invalid item code! Please try again.")

        # open soup text file if user input starts with E
        elif order_code[0] == "E":
            menu_beverages_list = open("menu_beverages_list.txt", "r")
            # read data in text file
            for item in menu_beverages_list.readlines():
                data = item.split(";")
                itemCode = data[0]
                itemDescription = data[1]
                itemPrice = data[2]
                # check whether input is exist
                if itemCode == order_code:
                    print(f"""
Item added to cart: {itemCode}- {itemDescription} """)
                    # open item cart text file and add item into text file
                    cs_itemCart = open("cs_itemCart_list.txt", "a")
                    cs_itemCart.write(itemCode + "; " + itemDescription + "; " + itemPrice + ";\n")
                    cs_itemCart.close()
                    break
            else:
                # Error message for invalid code
                print("Invalid item code! Please try again.")
        elif order_code == "Q":
            # provice "quit" function
            menu_with_categories()
        elif order_code == "V":
            # call function to view itemCart
            cs_itemCart_menu()
        else:
            # loop for invalid code
            print("Invalid code! Please try again.")
            take_order_pg()


def payment_pg():
    print(f"""
--------------------PAYMENT--------------------\n
                   -INVOICE-""")
    # call function to print invoice
    invoice()
    payment_choice = input("""
    Press "Y" to proceed, "M" to modify item cart, "B" to back to Main Menu.
>>> """)
    if payment_choice == "B":
        # provide "back" function
        registered_menu()
    elif payment_choice == "M":
        # call function to modify itemCart
        cs_itemCart_menu()
    elif payment_choice == "Y":
        # get order person name to proceed to payment
        oder_person = input("""Please enter your name: """)
        # payment options
        payment_option = input("""
    Please select your payment option (1-3):

    1. Credit Card/ Debit Card
    2. Online Banking
    3. Back
>>> """)
        if payment_option == "3":
            # provide "back" function
            payment_pg()
        elif (payment_option == "1") or (payment_option == "2"):
            # double payment confirmation
            payment_confirmation = input("""
                **Payment Confirmation**

    Are you sure to proceed payment?
    (Press "Y" to proceed, "N" to cancel payment process.)
>>> """)
            if payment_confirmation == "Y":
                # open itemCart text file in read mode
                cs_itemCart_list = open("cs_itemCart_list.txt", "r+")
                # open customer order history text file in append mode
                cs_order_history = open("cs_order_history.txt", "a")
                # open admin received order text file in append mode
                adm_received_order = open("adm_received_order.txt", "a")

                # read data in item cart text file
                for item in cs_itemCart_list.readlines():
                    # write order person name from user to customer order history text file first
                    cs_order_history.write(oder_person + "; ")
                    # write item in item cart text file to customer order history text file after order person name
                    cs_order_history.write(item)
                    # write order person name from user to admin received order text file first
                    adm_received_order.write(oder_person + "; ")
                    # write item in item cart text file to admin received order text file after order person name
                    adm_received_order.write(item)
                # clear item cart text file
                cs_itemCart_list.truncate(0)
                cs_itemCart_list.close()
                # provide single blank row in text file
                cs_order_history.write("\n")
                cs_order_history.close()
                # provide single blank row in text file
                adm_received_order.write("\n")
                adm_received_order.close()
                # call after payment page function
                after_payment()
            elif payment_confirmation == "N":
                # provide "back" function
                payment_pg()
            else:
                # loop for invalid code
                print("Invalid code! Please try again.")
                payment_pg()
        else:
            # loop for invalid code
            print("Invalid code! Please try again.")
            payment_pg()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        payment_pg()


def after_payment():
    after_payment_choice = input("""
    Payment Successful!
    Merchant is now preparing your order.......

    Please select an option (1-3):
    1. View Order History
    2. Main Menu
    3. Log Out
>>> """)
    if after_payment_choice == "1":
        # call function to print order history
        cs_order_history()
    elif after_payment_choice == "2":
        # call menu function
        registered_menu()
    elif after_payment_choice == "3":
        # call function to exit program
        exit()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        after_payment()


def cs_order_history():
    print("""
----------------ORDER HISTORY----------------""")
    # create empty list to store records
    temp_list = []

    # loop customer order history text file to count number of orders
    with open("cs_order_history.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    # loop customer order history based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("cs_order_history.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp customer order history text file in overwrite mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "w")
        # overwrite the text file with order
        temp_cs_order_history.write(item)
        temp_cs_order_history.close()
        # open temp customer order history text file in read mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "r")
        # read data in temp customer order history text file
        for item in temp_cs_order_history.readlines():
            data = item.split(";")
            orderPerson = data[0]
            # print order person name for once before items details
            print("\n            - Oder From:", orderPerson, "-")
            print("******************ITEM******************   RM")
            break
        temp_cs_order_history.close()

        # open temp customer order history text file in read mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "r")
        # initialize total price to 0
        total_price = 0
        # read data in temp customer order history text file
        for item in temp_cs_order_history.readlines():
            data = item.split(";")
            orderPerson = data[0]
            itemCode = data[1]
            itemDescription = data[2]
            itemPrice = float(data[3])
            # add item price for item in temp customer order history text file to total_price
            total_price += itemPrice
            # format of arrangment#
            length_in_digit = len(itemCode + itemDescription)
            price_location = 40 - length_in_digit
            print(itemCode + "-" + itemDescription + " " * price_location, "{:.2f}".format(itemPrice))
        temp_cs_order_history.close()
        if total_price != 0:
            # print calculation only when order exist
            print("\n", " " * 34, "---------------")
            print(" " * 35, "Total: RM", "{:.2f}".format(total_price))
            print(" " * 35, "---------------")
            print("")
    history_choice = input("""
    Please select an option (1-2):
    1. Main Menu
    2. Take Order
>>> """)
    if history_choice == "1":
        # call menu fucntion
        registered_menu()
    elif history_choice == "2":
        # call function to select item and add item to itemCart
        menu_with_categories()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        cs_order_history()


def adm_order_search():
    order_search_choice = input("""
    -------------------Search Orders-------------------
    Please select an option (1-3):
    1. Show Pending Orders
    2. Show Completed Orders
    3. Back
>>> """)

    if order_search_choice == "1":
        pending_order_choice = input("""
    --------------Search Pending Orders--------------
    Please select an option (1-3):
    1. Show All Orders
    2. Show Specific Order
    3. Back
>>> """)
        if pending_order_choice == "1":
            # call function to show all pending orders
            admin_show_all_orders()
        elif pending_order_choice == "2":
            print(f"""
EXISTING PENDING ORDERS UNDER NAME: 
""")
            # call function to show pending orders order person name
            show_pending_order_csName()
            cs_order_choice = input("""
    (Enter "B" to back.)
    Please enter the customer name to view orders:
>>> """)
            if cs_order_choice != "B":
                # check whether order person name is exist
                exist_name = []
                temp_keep = open("temp_glob.txt", "r")
                for cs_choice in temp_keep.readlines():
                    data = cs_choice.split(";")
                    cs_name = data[0]
                    exist_name.append(cs_name)
                temp_keep.close()
                if cs_order_choice in exist_name:
                    # store order person name from admin input to temp_view_order_history list
                    temp_keep = open("temp_glob.txt", "w")
                    temp_keep.write(cs_order_choice)
                    temp_keep.close()
                    # call function to show specific orders based on order person name provided
                    specific_orders()
                else:
                    temp_keep.close()
                    # loop for invalid order person name
                    print("\nOrder does not exist...")
                    adm_order_search()
            elif cs_order_choice == "B":
                # provide "back" function
                adm_order_search()
        elif pending_order_choice == "3":
            # provide "back" function
            adm_order_search()
    elif order_search_choice == "2":
        # call function to search completed orders
        adm_completed_order()
    elif order_search_choice == "3":
        # provide "back" function
        admin_pg()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        adm_order_search()


def show_pending_order_csName():
    # create empty list to store records
    temp_list = []

    # loop admin reveived order text file to count number of orders
    with open("adm_received_order.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    temp_keep = open("temp_glob.txt", "r+")
    temp_keep.truncate(0)
    temp_keep.close()
    temp_keep = open("temp_glob.txt", "a")
    # loop admin received order text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("adm_received_order.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp admin received order text file in overwrite mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "w")
        # overwrite the text file with order
        temp_adm_received_order.write(item)
        temp_adm_received_order.close()
        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        # read data in temp admin received order text file

        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]
            temp_keep.write(orderPerson+ ";" + "\n")
            temp_keep.close()
            # print order person name
            print("    " + orderPerson)
            break


def admin_show_all_orders():
    # create empty list to store orders in text file
    temp_list = []

    # calculate number of orders in text file
    with open("adm_received_order.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # store orders in temp_list order by order
    for item in order:
        temp_list.append(item)
    # calculate number of orders by getting number of items in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    # loop admin received order text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("adm_received_order.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp admin received order text file in overwrite mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "w")
        # overwrite the text file with order
        temp_adm_received_order.write(item)
        temp_adm_received_order.close()
        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        # read data in temp customer order history text file
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]
            # print order person name for once before items details
            print("\n         - Oder From:", orderPerson, "-")
            print("******************ITEM******************")
            break
        temp_adm_received_order.close()

        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        # read data in temp admin received order text file
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            itemCode = data[1]
            itemDescription = data[2]
            # print itemCode and itemDescription
            print(itemCode + "-" + itemDescription)
            temp_adm_received_order.close()
    received_order_choice = input("""
    Please select an option (1-2):
    1. Mark specific order as done.
    2. Back
>>> """)

    if received_order_choice == "1":
        print(f"""
    EXISTING PENDING ORDERS UNDER NAME:
        """)
        # call function to show pending orders order person name
        show_pending_order_csName()
        cs_order_choice = input("""
    (Enter "B" to back.)
    Please enter the customer name to view orders:
>>> """)
        if cs_order_choice != "B":
            # check whether order person name from admin input is exist
            exist_name = []
            temp_keep = open("temp_glob.txt", "r")
            for cs_choice in temp_keep.readlines():
                data = cs_choice.split(";")
                cs_name = data[0]
                exist_name.append(cs_name)
            temp_keep.close()
            if cs_order_choice in exist_name:
                # store order person name to temp_view_order_csName
                temp_keep = open("temp_glob.txt", "w")
                temp_keep.write(cs_order_choice)
                temp_keep.close()
                # call function to show specific order based on order person name provided
                specific_orders()
            else:
                # loop for invalid order person name
                print("\nOrder does not exist...")
                adm_order_search()
        elif cs_order_choice == "B":
            # provide "back" function
            adm_order_search()
    elif received_order_choice == "2":
        # provide "back" function
        adm_order_search()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        admin_show_all_orders()


def specific_orders():
    # create empty list to store records
    temp_list = []

    # loop admin received order text file to count number of orders
    with open("adm_received_order.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    # loop admin received order text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("adm_received_order.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp admin received order text file in overwrite mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "w")
        # overwrite the text file with order
        temp_adm_received_order.write(item)
        temp_adm_received_order.close()
        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        # read data in temp admin received order text file
        temp_keep = open("temp_glob.txt", "r")
        cs_choice = temp_keep.readline()

        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]
            # print order person name once before item in text file
            if orderPerson in cs_choice:
                print("\n         - Order From:", orderPerson, "-")
                print("******************ITEM******************")
                break

        temp_adm_received_order.close()
        temp_keep.close()
        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        # read data in temp admin received order text file
        temp_keep = open("temp_glob.txt", "r")
        cs_choice = temp_keep.readline()
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]
            itemCode = data[1]
            itemDescription = data[2]
            # print the order details from person requested by admin
            if orderPerson in cs_choice:
                print(itemCode + "-" + itemDescription)
        temp_adm_received_order.close()
        temp_keep.close()
    admin_mark_as_done()


def admin_show_all_payments():
    print("""
                [PAYMENT DETAILS]""")
    # create empty list to store records
    temp_list = []

    # loop customer order history text file to count number of orders
    with open("cs_order_history.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    # loop customer order history text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("cs_order_history.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp customer order history text file in overwrite mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "w")
        # overwrite the text file with order
        temp_cs_order_history.write(item)
        temp_cs_order_history.close()
        # open temp customer order history text file in read mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "r")
        # read data in temp customer order history text file
        for item in temp_cs_order_history.readlines():
            data = item.split(";")
            orderPerson = data[0]
            # print order person name once before item in text file
            print("\n           - Paid By:", orderPerson, "-")
            print("******************ITEM******************   RM")
            break
        temp_cs_order_history.close()

        # open temp customer order history text file in read mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "r")
        # initialize total price to 0
        total_price = 0
        # read data in temp customer order history text file
        for item in temp_cs_order_history.readlines():
            data = item.split(";")
            itemCode = data[1]
            itemDescription = data[2]
            itemPrice = float(data[3])
            # add all item price for item in text file to total_price
            total_price += itemPrice
            # format of arrangment#
            length_in_digit = len(itemCode + itemDescription)
            price_location = 40 - length_in_digit
            print(itemCode + "-" + itemDescription + " " * price_location, "{:.2f}".format(itemPrice))
        print("\n", " " * 34, "---------------")
        print(" " * 35, "Total: RM", "{:.2f}".format(total_price))
        print(" " * 35, "---------------")
        print("")
        temp_cs_order_history.close()


def show_payment_csName():
    # create empty list to store records
    temp_list = []

    # loop customer order history text file to count number of orders
    with open("cs_order_history.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0

    temp_keep = open("temp_glob.txt", "r+")
    temp_keep.truncate(0)
    temp_keep.close()
    # loop customer order history text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("cs_order_history.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp customer order history text file in overwrite mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "w")
        # overwrite the text file with order
        temp_cs_order_history.write(item)
        temp_cs_order_history.close()
        # open temp customer order history text file in read mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "r")
        # read data in temp customer order history text file

        for item in temp_cs_order_history.readlines():
            data = item.split(";")
            orderPerson = data[0]
            temp_keep = open("temp_glob.txt", "a")
            temp_keep.write(orderPerson+";"+"\n")
            temp_keep.close()
            # print order person name
            print("    " + orderPerson)
            break


def adm_payment_search():
    payment_search_choice = input("""
    ----------------Search Payments----------------
    Please select an option (1-3):
    1. Show All Payments
    2. Show Specific Payment
    3. Back
>>> """)
    if payment_search_choice == "1":
        # call function to show all payments details
        admin_show_all_payments()
        all_payment_choice = input("""
    Enter 'B' to back.
>>> """)
        if all_payment_choice == "B":
            # provide "back" function
            adm_payment_search()
        else:
            # loop for invalid input
            adm_payment_search()

    elif payment_search_choice == "2":
        print(f"""
    EXISTING PAYMENT UNDER NAME:
""")
        # call function to show existence order person name who paid
        show_payment_csName()
        view_csName = input("""
    (Enter "B" to back.)
    Please enter the customer name to view payment:
>>> """)
        if view_csName != "B":
            exist_name = []
            temp_keep = open("temp_glob.txt", "r")
            for cs_choice in temp_keep.readlines():
                data = cs_choice.split(";")
                cs_name = data[0]
                exist_name.append(cs_name)
            temp_keep.close()
            if view_csName in exist_name:
                temp_keep = open("temp_glob.txt", "w")
                temp_keep.write(view_csName)
                temp_keep.close()
                # call function to show specific payment details based on order person name provided
                specific_payment()
            else:
                # loop for invalid order person name
                print("\nPayment does not exist....")
                adm_payment_search()
        elif view_csName == "B":
            # provide "back" function
            adm_payment_search()
        else:
            # loop for invalid code
            print("Invalid code! Please try again.")
            adm_payment_search()
    elif payment_search_choice == "3":
        # provide "back" function
        admin_pg()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        adm_payment_search()


def specific_payment():
    print("""
            [PAYMENT DETAILS]""")
    # create empty list to store records
    temp_list = []

    # loop customer order history text file to count number of orders
    with open("cs_order_history.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    # loop customer order history text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("cs_order_history.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp customer order history text file in overwrite mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "w")
        # overwrite the text file with order
        temp_cs_order_history.write(item)
        temp_cs_order_history.close()
        # open temp customer order history text file in read mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "r")
        temp_keep = open("temp_glob.txt", "r")
        cs_choice = temp_keep.readline()
        # read data in temp customer order history text file
        for item in temp_cs_order_history.readlines():
            data = item.split(";")
            orderPerson = data[0]
            if orderPerson in cs_choice:
                # print order person name once before item in text file
                print("\n         - Oder From:", orderPerson, "-")
                print("******************ITEM******************")
                break
        temp_cs_order_history.close()
        temp_keep.close()

        # open temp customer order history text file in read mode
        temp_cs_order_history = open("temp_cs_order_history.txt", "r")
        temp_keep = open("temp_glob.txt", "r")
        cs_choice = temp_keep.readline()
        # initialize total price to 0
        total_price = 0
        # read data in temp customer order history text file
        for item in temp_cs_order_history.readlines():
            data = item.split(";")
            orderPerson = data[0]
            itemCode = data[1]
            itemDescription = data[2]
            itemPrice = float(data[3])
            if orderPerson in cs_choice:
                # add all item price for item in text file to total_price
                total_price += itemPrice
                # format of arrangment#
                length_in_digit = len(itemCode + itemDescription)
                price_location = 40 - length_in_digit
                print(itemCode + "-" + itemDescription + " " * price_location, "{:.2f}".format(itemPrice))
        # print calculation format only when item exist
        if total_price != 0:
            print("\n", " " * 34, "---------------")
            print(" " * 35, "Total: RM", "{:.2f}".format(total_price))
            print(" " * 35, "---------------")
        temp_cs_order_history.close()
        temp_keep.close()
    specific_payment_choice = input("""
    Enter 'B' to back.
>>> """)
    if specific_payment_choice == "B":
        # provide "back" function
        adm_payment_search()
    else:
        # loop for invalid input
        adm_payment_search()


def admin_mark_as_done():
    mark_as_done_choise = input("""
    Please select an option (1-2):
    1. Mark current order as done.
    2. Back
>>> """)
    if mark_as_done_choise == "1":
        # create empty list to store records
        temp_list = []

        # loop admin received order text file to count number of orders
        with open("adm_received_order.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        # put orders into temp_list order by order
        for item in order:
            temp_list.append(item)
        # count number of records by getting number of item in temp_list
        number_of_records = len(temp_list)

        # initialize count to 0
        count = 0
        # loop admin received order text file based on number of records
        for i in range(0, number_of_records - 1):
            # read order one by one
            with open("adm_received_order.txt") as f:
                lines = f.read()
            order = lines.split("\n\n")
            item = order[0 + count]
            count += 1

            # open temp admin received order text file in overwrite mode
            temp_adm_received_order = open("temp_adm_received_order.txt", "w")
            # overwrite the text file with order
            temp_adm_received_order.write(item)
            temp_adm_received_order.close()
            # open temp admin received order text file in read mode
            temp_adm_received_order = open("temp_adm_received_order.txt", "r")
            temp_keep = open("temp_glob.txt", "r")
            cs_choice = temp_keep.readline()

            # read data in temp admin received order text file
            for info in temp_adm_received_order.readlines():
                data = info.split(";")
                orderPerson = data[0]

                # write order details from order person provided by admin to adm_received_history text file
                if orderPerson in cs_choice:
                    # open admin received history text file in append mode
                    adm_received_history = open("adm_received_history.txt", "a")
                    adm_received_history.write(info)
                    adm_received_history.close()

                # write order details from other order person to temp_keep_order text file
                elif orderPerson not in cs_choice:
                    temp_keep_order = open("temp_keep_order.txt", "a")
                    temp_keep_order.write(info)
                    temp_keep_order.close()
            temp_keep.close()
            # provide blank spaces after first record written into text file
            if count > 1:
                temp_keep_order = open("temp_keep_order.txt", "a")
                temp_keep_order.write("\n\n")


        adm_received_history = open("adm_received_history.txt", "a")
        # provide blank space to adm_received_history text file
        adm_received_history.write("\n\n")
        adm_received_history.close()

        # open admin received order text file in overwrite mode
        adm_received_order = open("adm_received_order.txt", "w")
        # open temp keep order text file in read+ mode
        temp_keep_order = open("temp_keep_order.txt", "r+")
        for details in temp_keep_order:
            # overwrite admin received order text file with item in temp_keep_order text file
            adm_received_order.write(details)
        adm_received_order.close()
        # clear temp_keep_order text file
        temp_keep_order.truncate(0)
        temp_keep_order.close()
        print("\nUpdated!")
        # call function to search order (looping)
        adm_order_search()

    elif mark_as_done_choise == "2":
        # provide "back" function
        adm_order_search()

    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        admin_mark_as_done()


def show_all_completed_orders():
    print("""
    ----------ALL COMPLETED ORDERS----------""")
    # create empty list to store records
    temp_list = []

    # loop admin received history text file to count number of orders
    with open("adm_received_history.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    # loop admin received history text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("adm_received_history.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp admin received order text file in overwrite mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "w")
        # overwrite the text file with order
        temp_adm_received_order.write(item)
        temp_adm_received_order.close()
        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")

        # read data in temp admin received order text file
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]
            # print order person name once before item in text file
            print("\n         - Oder From:", orderPerson, "-")
            print("******************ITEM******************")
            break
        temp_adm_received_order.close()

        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        # read data in temp admin received order text file
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            itemCode = data[1]
            itemDescription = data[2]
            # print itemCode and itemDecription in text file
            print(itemCode + "-" + itemDescription)


def show_compl_order_csName():
    # create empty list to store records
    temp_list = []

    # loop admin received history text file to count number of orders
    with open("adm_received_history.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0

    temp_keep = open("temp_glob.txt", "r+")
    temp_keep.truncate(0)
    temp_keep.close()

    # loop admin received history text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("adm_received_history.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp admin received order text file in overwrite mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "w")
        # overwrite the text file with order
        temp_adm_received_order.write(item)
        temp_adm_received_order.close()
        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")

        # read data in temp admin received order text file
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]
            temp_keep = open("temp_glob.txt", "a")
            temp_keep.write(orderPerson+ ";" + "\n")
            temp_keep.close()
            # print completed orders order person name
            print("    " + orderPerson)
            break


def adm_completed_order():
    search_completed_order_choice = input("""
      -Search Completed Orders-

    Please select an option (1-3):
    1. Show All Orders
    2. Show Specific Order
    3. Back
>>> """)
    if search_completed_order_choice == "1":
        # call function to show all completed orders
        show_all_completed_orders()
        complete_order_choice = input("""
    (Enter "B" to back.)
>>> """)
        if complete_order_choice == "B":
            # provide "back" function
            adm_completed_order()
        else:
            # loop for invalid input
            adm_completed_order()
    elif search_completed_order_choice == "2":
        print(f"""
    EXISTING COMPLETED ORDER UNDER NAME:
""")
        # call function to show completed orders order person name
        show_compl_order_csName()
        view_csName = input("""
    (Enter "B" to back.)
    Please enter the customer name to view order: """)
        if view_csName != "B":
            exist_name = []
            temp_keep = open("temp_glob.txt", "r")
            for cs_choice in temp_keep.readlines():
                data = cs_choice.split(";")
                cs_name = data[0]
                exist_name.append(cs_name)
            temp_keep.close()
            # check whether order person name from user input valid or not
            if view_csName in exist_name:
                temp_keep = open("temp_glob.txt", "w")
                temp_keep.write(view_csName)
                temp_keep.close()
                # call function to show specific order based on order person name provided
                specific_completed_orders()
            else:
                # loop for invalid input
                print("Order does not exist....")
                adm_completed_order()
        elif view_csName == "B":
            # provide "back" function
            adm_completed_order()
        else:
            # loop for invalid code
            print("Invalid code! Please try again.")
            adm_completed_order()
    elif search_completed_order_choice == "3":
        # provide "back" function
        adm_order_search()
    else:
        # loop for invalid code
        print("Invalid code! Please try again.")
        adm_completed_order()


def specific_completed_orders():
    # create empty list to store records
    temp_list = []

    # loop admin received history text file to count number of orders
    with open("adm_received_history.txt") as f:
        lines = f.read()
    order = lines.split("\n\n")
    # put orders into temp_list order by order
    for item in order:
        temp_list.append(item)
    # count number of records by getting number of item in temp_list
    number_of_records = len(temp_list)

    # initialize count to 0
    count = 0
    # loop admin received history text file based on number of records
    for i in range(0, number_of_records - 1):
        # read order one by one
        with open("adm_received_history.txt") as f:
            lines = f.read()
        order = lines.split("\n\n")
        item = order[0 + count]
        count += 1

        # open temp admin received order text file in overwrite mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "w")
        # overwrite the text file with order
        temp_adm_received_order.write(item)
        temp_adm_received_order.close()
        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        temp_keep = open("temp_glob.txt", "r")
        cs_choice = temp_keep.readline()
        # read data in temp admin received order text file
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]

            if orderPerson in cs_choice:
                # print order person name once before item in text file
                print("""
    ---------COMPLETED ORDER---------""")
                print("\n         - Oder From:", orderPerson, "-")
                print("******************ITEM******************")
                break
        temp_adm_received_order.close()

        # open temp admin received order text file in read mode
        temp_adm_received_order = open("temp_adm_received_order.txt", "r")
        # read data in temp admin received order text file
        for item in temp_adm_received_order.readlines():
            data = item.split(";")
            orderPerson = data[0]
            itemCode = data[1]
            itemDescription = data[2]
            if orderPerson in cs_choice:
                # print itemCode and itemDecription in text file
                print(itemCode + "-" + itemDescription)
        temp_adm_received_order.close()
        temp_keep.close()
    specific_completed_choice = input("""
    (Enter "B" to back.)
>>> """)
    if specific_completed_choice == "B":
        # provide "back" function
        adm_completed_order()
    else:
        # loop for invalid input
        adm_completed_order()


def exit():
    print('\n*****************************************************\n')
    print('Thank you for visiting SPIDERMAN ONLINE FOOD SERVICES')
    print('Exiting....')
    print('\n*****************************************************\n')
    exit_choice = input("""
    -Enter any character to continue-
>>> """)
    if exit_choice != " ":
        home_pg()


home_pg()

