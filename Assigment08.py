# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# RFear,12.6.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt'
lstProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products name
        product_price: (float) with the products standard price
    methods:
        __str__: returns a string
        __float__: returns a float
    changelog: (Who,When,What)
        RRoot,1.1.2030,Created Class
        RFear,12.6.2021,Modified code to complete assignment 8
    """

    # --Constructors--
    def __init__(self, product_name: str, product_price: float):
        # --Attributes--
        self.__product_name = product_name
        self.__product_price = product_price

    ## --Properties--
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, name):
        if str(name).isnumeric() == False:
            self.__product_name = name
        else:
            #raise Exception("Names cannot be numbers.")
            raise TypeError("Names cannot be numbers.")

    @property
    def product_price(self):
        return '{:.2f}'.format(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if type(value) == float:
            self.__product_price = value
        else:
            raise Exception("Prices cannot be strings.")

    ## --Methods--
    def __str__(self):
        return self.product_name

    def __float__(self):
        return self.product_price


# Processing  ------------------------------------------------------------- #
class Processor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data(file_name, list_of_objects): file name and a list of product objects
        save_data(file_name, list_of_objects): file name and a list of product objects
        add_data(list_of_obj): adds a new product and price to the list of objects

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RFear,12.6.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data(fname, list_of_obj):
        """ Read data from file_name into a list of product objects.

        :param fname: (string) file name to read from
        :param list_of_obj: (list) list of product objects
        :return: nothing
        """
        try:
            f = open(fname, 'r')
            for line in f:
                prod, price = line.split(',')
                prod, price = str(prod.strip()), float(price.strip())
                row = Product(prod, price)
                list_of_obj.append(row)
        except FileNotFoundError:
            print(f"There is no file with the name '{fname}'.  One will be created.")
            f = open(fname, "w")
            f.close()
            print(f"\nThe file '{file_name}' was created.")
        else:
            print(f"Successfully read data from the file '{fname}'.")
            f.close()

    @staticmethod
    def save_data(fname, list_of_obj):
        """ Writes data from a list of product objects to a file.

        :param fname: (string) file name to save to
        :param list_of_obj: (list) list of product objects
        :return: nothing
        """
        f = open(fname, 'w')
        for row in list_of_obj:
            f.write(row.product_name + "," + row.product_price + "\n")
        f.close()

    @staticmethod
    def add_data(list_of_obj):
        """ Shows the current product and price objects

        :param list_of_obj: (list) of data you want to display
        :return: nothing
        """
        product = ""
        price = ""
        ans = None

        while ans != "y":
            product = input("Enter a new product name: ")
            ans = input(f"\nFor the product you entered: {product}\n"
                        f"Are these results correct? [y/n] ")

        while True:
            try:
                price = float(input("\nEnter the price for the new product: "))
            except ValueError as e:
                print("Please enter a number for the price.\n")
            if type(price) == float:
                break

        row = Product(product, price)
        list_of_obj.append(row)

# Presentation (Input/Output)  -------------------------------------------- #
class IO():
    """ Performs Input and Output tasks

    methods:
        print_menu(): display a menu of choices to the user
        input_menu_choice(): gets the menu choice from a user
        input_yes_no_choice(message): gets a yes or no choice from the user
        print_current_data(list_of_obj): shows the current product and price objects

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RFear,12.6.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Data
        2) Add Product and Price
        3) Save Data to File and Exit
        ''')

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def print_current_data(list_of_obj):
        """ Shows the current product and price objects

        :param list_of_obj: (list) of data you want to display
        :return: nothing
        """
        if list_of_obj == []:
            print("There is no data in the file.")
        else:
            print("The current products and prices are: ")
            print("The output format is:")
            print("Product" + " | " + "Price")
            for row in list_of_obj:
                print(row.product_name, " | ", row.product_price)


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Gets user's menu option choice
# Option 1: Show user current data in the list of product objects
# Option 2: Let user add data to the list of product objects
# Option 3: Let user save current data to file and exit program

# Make file object, open, and read data
Processor.read_data(file_name, lstProductObjects)

while True:
    IO.print_menu()  # shows menu
    choice = IO.input_menu_choice()

    if choice == '1':  # show current data
        IO.print_current_data(lstProductObjects)

    elif choice == '2':  # add product and price
        Processor.add_data(lstProductObjects)

    elif choice == '3':  # save, or not, and exit
        valid = ['y', 'n']
        while True:
            yn_choice = IO.input_yes_no_choice(f"Save data and to '{file_name}' and exit? [y/n]: ")
            if yn_choice in valid:
                if yn_choice == "n":
                    print("Save cancelled. Exiting program.")
                else:
                    Processor.save_data(file_name, lstProductObjects)
                    print("Data saved to file. Exiting program.")
                break
        break

    else:
        print("Error: Cannot process request."
              "\nPlease enter a valid option.")
