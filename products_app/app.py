import csv
import os

#
# USER INTERFACE
#

def menu(username="@prof-rossetti", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
-----------------------------------
INVENTORY MANAGEMENT APPLICATION
-----------------------------------
Welcome {username}!
There are {products_count} products in the database.
    operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.
Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def product_not_found(product_id):
    print(f"OOPS. There are no products matching the identifier '{product_id}'. Try listing products to see which ones exist.")

#
# CSV FILE / DATABASE OPERATIONS
#

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

def find_product(product_id, all_products):
    matching_products = [p for p in all_products if int(p["id"]) == int(product_id)]
    matching_product = matching_products[0]
    return matching_product

#
# CRUD OPERATIONS
#

# expecting a list of product dictionaries
def list_products(products):
    print("-----------------------------------")
    print(f"LISTING {len(products)} PRODUCTS:")
    print("-----------------------------------")
    for product in products:
        print(" #" + str(product["id"]) + ": " + product["name"])

def show_product(product):
    print("-----------------------------------")
    print("SHOWING A PRODUCT:")
    print("-----------------------------------")
    print(product)

def create_product():
    print("CREATING A NEW PRODUCT") #TODO: create a new product

def update_product():
    print("UPDATING A PRODUCT") #TODO: update a given product

def destroy_product():
    print("DESTROYING A PRODUCT") #TODO: destroy a given product

#
# SCRIPT INVOCATION
#

def run():
    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    my_menu = menu(username="@s2t2", products_count=len(products))
    operation = input(my_menu)

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    operation = operation.title() # normalize capitalization for more user-friendly comparisons, enables "LIST" and "list" and "List" to all work
    if operation == "List":
        list_products(products)
    elif operation == "Show":
        try:
            product_id = input("OK. Please specify the product's identifier: ")
            product = find_product(product_id, products)
            show_product(product)
        except ValueError as e: product_not_found(product_id)
        except IndexError as e: product_not_found(product_id)
    elif operation == "Create":
        create_product()
    elif operation == "Update":
        update_product()
    elif operation == "Destroy":
        destroy_product()
    elif operation == "Reset":
        reset_products_file()
    else:
        print("Oh, sorry, didn't recognize that operation. Please try again.")

    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
