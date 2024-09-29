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
