menu_items = [
'D1 ​​SODA 3',
'D2 ​​LEMONADE 3',
'D3 ​​TEA 2',
'D4 WATER 0',
'A1 ​​POTATO_CAKES 7',
'A2 ​​SPINACH_DIP 5',
'A3 ​​OYSTERS 13',
'A4 ​​CHEESE_FRIES 4',
'A5 ​​ONION_RINGS 7',
'S1 ​​COBB 14',
'S2 ​​CAESAR 13',
'S3 ​​GREEK 12',
'E1 ​​BURGER 16',
'E2 ​​PASTA 15',
'E3 ​​GNOCCHI​ 14',
'E4 ​​GRILLED_STEAK_SANDWICH 17',
'T1 ​​CARAMEL_CHEESECAKE 13',
'T2 ​​APPLE_COBBLER 12',
'T3 ​​BROWNIE_SUNDAE 9',
'T4 ​​FLAN 8'
]
drink_items = ['D1', 'D2',  'D3', 'D4']
appetizer_items = ['A1', 'A2',  'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2',  'E3', 'E4']
dessert_items =['T1', 'T2',  'T3', 'T4']
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  for item in menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), (item_price)
import random
menu_list = []
for item in menu_items:
    item_split = item.split()
    item_code = item_split[0]
    item_price = float(item_split[-1])
    item_name = " ".join(item_split[1:-1]).replace('\u200b', '')
    menu_item = {
        "code": item_code,
        "name": item_name,
        "price": item_price
    }
    if item_code not in drink_items:
        item_stock = random.randint(25, 50)
        menu_item["stock"] = item_stock
    menu_list.append(menu_item)
print(menu_list)
def show_main_menu():
  while True:
    print("Srujan")
    print("_______________________")
    print("N for a new order")
    print("C to change an order")
    print("M for Manager action")
    print("U for checking Customer Requests")
    print("X for close orders and prepare the check")
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Q':
      break
    elif user_menu_choice in 'X':
      close_order()
    elif user_menu_choice in 'N':
      print('\nNew Order')
      make_order(user_menu_choice.upper())
    elif user_menu_choice in 'M':
	    manager_menu()
    elif user_menu_choice in 'C':
	    change_order()
    elif user_menu_choice in 'U':
	    customer_request()
    else:
      print("Please enter the correct choice")

def manager_menu():
    print("\nManager Menu")
    print("A to Add an item")
    print("R to Remove an item")
    print("U to Update an item")
    choice = input("Select option: ").upper()
    global menu_list


    if choice == 'A':
        code = input("Enter new item code(e.g: D5): ").upper()
        if any(item['code'] == code for item in menu_list):
            print("Item already exists.")
            return

        name = input("Enter item name: ").upper()
        price = float(input("Enter item price: "))
        stock = None
        if code[0] != 'D':
            stock = int(input("Enter stock quantity: "))

        menu_item = {"code": code, "name": name, "price": price}
        if stock is not None:
            menu_item['stock'] = stock
        menu_list.append(menu_item)
        #print(menu_list)
        print(f"Added {name} to the menu.")

    elif choice == 'R':
      code = input("Enter item code to remove(e.g: D5): ").upper()
      for i in range(len(menu_list)):
        if menu_list[i]['code'] == code:
            del menu_list[i]
            print("Item removed successfully.")
            break
      else:
        print("Item not found.")


    elif choice == 'U':
      code = input("Enter item code to update(e.g: D5): ").upper()
      for item in menu_list:
        if item['code'] == code:
            new_name = input("Enter new name: ").upper()
            if new_name:
                item['name'] = new_name
            new_price = input("Enter new price: ")
            if new_price:
                item['price'] = float(new_price)
            print("Item updated successfully.")
            #print(menu_list)
            break
      else:
        print("Item not found.")


    else:
        print("Please enter the correct choice.")


def make_order(menu_choice):
    while True:
        menu_choice = input("Enter your choice D(drinks)/A(appetizer)/S(salads)/E(entree)/T(desserts): ").upper()
        if menu_choice in ['D', 'A', 'S', 'E', 'T']:
            print(f"Available {menu_choice} items:")
            for item in menu_list:
                if item['code'][0] == menu_choice:
                    print(f"{item['code']} - {item['name']} ${item['price']}")

            item_code = input("Choose an item from the list above (e.g., D1): ").upper()
            item_details = None
            for item in menu_list:
                if item['code'] == item_code:
                    item_details = (item['name'], item['price'])
                    break

            if item_details:
                if menu_choice not in category_dict:
                    category_dict[menu_choice] = {}
                category_dict[menu_choice][item_code] = item_details
                print(f"Added {item_details[0]} at ${item_details[1]}")
            else:
                print("Item code not found.")
        else:
            print("Invalid category. Please choose from D, A, S, E, T.")

        add_choice = input("Add another item to list? (y/n): ").lower()
        if add_choice != 'y':
            break

def close_order():
    tax_rate = 0.08  # Assuming an 8% tax rate
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("\nCheck:\n")
    global category_dict
    subtotal = 0
    for category, items in category_dict.items():
        print(f"{category}:")
        category_total = 0
        for code, details in items.items():
            name, price = details
            print(f"{code} - {name} ${price}")
            category_total += float(price)
        subtotal += category_total
    tax = subtotal * tax_rate
    total_price = subtotal + tax
    print(f"Items Total: ${subtotal:.2f}")
    print(f"Taxes: ${tax:.2f}")
    print(f"Total: ${total_price:.2f}")
    print("++++++++++++++++++++++++++++++++++++++++++++")

def current_order():
    print("Current Order:")
    global category_dict
    for category, items in category_dict.items():
      if items:
        for code, details in items.items():
            print(f"{category} items: {code}  {details[0]}  ${details[1]}")

def change_order():
    current_order()
    print("Available categories: Drinks (D), Appetizers (A), Salads (S), Entrees (E), Desserts (T)")
    existing_choice = input("Enter the category code from the order (e.g: D): ").upper()
    old_item_code = input("Enter the code of the item to replace (e.g: D5): ").upper()

    if existing_choice in category_dict and old_item_code in category_dict[existing_choice]:
        #print("Choose a category for the new item (e.g: D):")
        new_choice = input("Enter the category code (e.g: D): ").upper()

        if new_choice in category_dict:
            print(f"Available replacement items in {new_choice}:")
            for item in menu_list:
                if item['code'].startswith(new_choice) and item['code'] != old_item_code:
                    print(f"{item['code']} - {item['name']} (${item['price']})")

            new_item_code = input("Enter the code of the new item: ").upper()
            new_item_details = get_item_information(new_item_code)
            if new_item_details and (new_item_code != old_item_code or new_choice != existing_choice):
                if old_item_code in category_dict[existing_choice]:
                    del category_dict[existing_choice][old_item_code]
                category_dict[new_choice][new_item_code] = new_item_details
                print(f"Replaced {old_item_code} in {existing_choice} with {new_item_code} in {new_choice} - {new_item_details[0]} (${new_item_details[1]})")
            else:
                print("Invalid new item code or the same item selected.")
        else:
            print("Invalid destination category.")
    else:
        print("Invalid source category or item code not found.")


def customer_request():
    request = input("Enter your order request (e.g., '30 Burgers'): ")
    try:
        parts = request.split()
        quantity = int(parts[0])
        item_name = ' '.join(parts[1:])
    except ValueError:
        print("Invalid format. Please use the format 'Quantity Item'. Example: '30 Burgers'")
        return
    item_name = item_name.strip().upper()
    for item in menu_list:
        if item['name'].upper() == item_name:
            if item['code'][0] == 'D':
                print(f"{quantity} {item_name} are available. Your request is accepted")
                return
            else:
                if 'stock' in item and item['stock'] >= quantity:
                    print(f"{quantity} {item_name} are available. Your request is accepted")
                    return
                elif 'stock' in item and item['stock'] < quantity:
                    print(f"Insufficient stock for {item_name}. Only {item['stock']} left. unable to fulfill your request")
                    return
    print(f"{item_name} is not on the menu.")

if __name__ == '__main__':

    drinks = {}
    appetizers = {}
    salads = {}
    entrees = {}
    desserts = {}
    category_dict = {
                    'D': drinks,
                    'A': appetizers,
                    'S': salads,
                    'E': entrees,
                    'T': desserts
                }
    show_main_menu()