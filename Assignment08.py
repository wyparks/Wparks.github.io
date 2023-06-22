# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Your Name>,<Today's Date>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass  # remove after code is added
    # TODO: Add Code for Product class (Constructor, Properties, & Methods)
    # constructor __init__(self, xxxxx)

    def __init__(self, product_name, product_price):
        self._product_name = product_name
        self._product_price = product_price
    # --Properties--
    # Product Name
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value.title()
     # Product Price
    @property
    def product_price(self):
       return self._product_price

    @product_price.setter
    def product_price(self, value):
        self._product_price = value

    # Methods
    def __str__(self):
        return f"{self.product_name},{self.product_price}"
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        global file_obj  # using global file variable across all functions
        file_obj = open(file_name, "r")
        for line in file_obj:
            data = line.split(",")
            row = Product(data[0], data[1])
            lstOfProductObjects.append(row)
        file_obj.close()
        return lstOfProductObjects
    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, lstOfProductObjects):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        global file_obj  # using global here to be consistent across functions
        file_obj = open(file_name, 'w')  # opening file
        for i in lstOfProductObjects:
            file_obj.write(i.__str__() + '\n')  # writing list to file
        file_obj.close()
        return lstOfProductObjects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items():

        print_current_list_items(lstOfProductObjects):

        input_product_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        return input("Which option would you like to perform? [1 to 4] - ")

    @staticmethod
    def output_current_products_in_list(lstOfProductObjects):
        """ Shows the current Tasks in the list of dictionaries rows

        :param lstOfProductObjects: (list) of rows you want to display
        :return: nothing
        """
        print()
        print("******* The current products are: *******")
        for row in lstOfProductObjects:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks
    @staticmethod
    def input_new_product():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        product_new = input('Please enter the product you wish to add: ')  # getting task from user
        price_new = input(f'Enter the price of {product_new}: ')  # getting priority
        return Product(product_name=product_new, product_price=price_new)
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
strFileName = 'products.txt'
lstOfProductObjects = []
FileProcessor.read_data_from_file(file_name=strFileName, lstOfProductObjects=lstOfProductObjects)
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
while True:
    IO.print_menu_items()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    if choice_str.strip() == '1':
        IO.output_current_products_in_list(lstOfProductObjects)
        continue
    elif choice_str.strip() == '2':  # Add a new Task
        new_product = IO.input_new_product()
        lstOfProductObjects.append(new_product)
        continue  # to show the menu
    elif choice_str == '3':  # Save Data to File
        FileProcessor.write_data_to_file(file_name=strFileName, lstOfProductObjects=lstOfProductObjects)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
# Main Body of Script  ---------------------------------------------------- #
