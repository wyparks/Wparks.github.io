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
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Product,Price}
choice_str = ""  # Captures the user option selection

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
        self.product_name = product_name
        self.product_price = product_price
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
    pass
     @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        global file_obj  # using global file variable across all functions
        file_obj = open(file_name, "r")
        for line in file_obj:
            task, priority = line.split(",")
            row = {"Product": task.strip(), "Price": priority.strip()}
            list_of_rows.append(row)
        file_obj.close()
        return list_of_rows
    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        global file_obj  # using global here to be consistent across functions
        file_obj = open(file_name, 'w')  # opening file
        for i in list_of_rows:
            file_obj.write(i["Product"] + ',' + i["Price"] + '\n')  # writing list to file
        file_obj.close()
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

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
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print()
        print("******* The current products are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks
    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        task_new = input('Please enter the product you wish to add: ')  # getting task from user
        priority_new = input(f'Enter the price of {task_new}: ')  # getting priority
        return task_new, priority_new
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor .write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
# Main Body of Script  ---------------------------------------------------- #
