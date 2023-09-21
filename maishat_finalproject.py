"""
Maisha Taranum
Class: CS 521 - Summer 2
Date: 08/15/2023
Final Project
Description of Problem: Boston’s Pop-Up ShopTracker using Python.
"""
# Import the Shop class from the shop_class.py file
from shop_class import Shop

class Shop:
    def __init__(self, shop_type, area, date, prices, store_hours):
        self.shop_type = shop_type
        self.area = area
        self.date = date
        self.prices = prices
        self.store_hours = store_hours

# Create instances of the Shop class using the imported class

shops = [Shop('shoes', 'downtown', '2023-06-25', [50, 60, 70],\
              '10:00 AM - 8:00 PM'),
          Shop('shirts', 'outletmall', '2023-06-27', [25, 30],\
               '9:00 AM - 9:00 PM'),
          Shop('pants', 'downtown', '2023-06-27', [40, 45],\
               '10:30 AM - 7:30 PM'),
          Shop('coats', 'outletmall', '2023-06-28', [80],\
               '9:30 AM - 8:30 PM'),
          Shop('shirts', 'downtown', '2023-06-29', [20, 22],\
               '11:00 AM - 6:00 PM'),
          Shop('shoes', 'outletmall', '2023-06-30', [55, 65],\
               '10:00 AM - 9:00 PM'),
          Shop('pants', 'downtown', '2023-06-30', [50, 55, 60],\
               '11:00 AM - 8:00 PM'),
          Shop('coats', 'outletmall', '2023-05-01', [90, 95],\
               '10:00 AM - 7:00 PM'),
          Shop('shirts', 'downtown', '2023-05-01', [18, 20],\
               '12:00 PM - 5:00 PM')]


def display_store_goods(store_goods):
    print("Available goods in the store:")
    print("-----------------------------")
    for item in store_goods:
        print(f"{item.shop_type} in {item.area} on {item.date}:\
              Prices - {item.prices}, Store Hours - {item.store_hours}")

def summarize_all_data(shop_list):
    downtown_count = summarize_by_area(shop_list, 'downtown')
    outletmall_count = summarize_by_area(shop_list, 'outletmall')
    dates = set([shop.date for shop in shop_list])
    date_counts = {}
    for date in dates:
        date_counts[date] = summarize_by_date(shop_list, date)
    most_date = max(date_counts, key=date_counts.get)
    if downtown_count > outletmall_count:
        most_area = 'downtown'
    else:
        most_area = 'outletmall'
    return {'most_area': most_area,'most_date': most_date,\
            'downtown_count': downtown_count, 'outletmall_count': \
                outletmall_count, 'date_counts': date_counts}

def summarize_by_area(shop_list, area):
    area_count = 0
    for shop in shop_list:
        if shop.area == area:
            area_count += 1
    return area_count

def summarize_by_date(shop_list, date):
    date_count = 0
    for shop in shop_list:
        if shop.date == date:
            date_count += 1
    return date_count

def detail_by_shop_type(shop_list, shop_type, specific_shop=None):
    details = []
    for shop in shop_list:
        if shop.shop_type == shop_type:
            if specific_shop is None or shop == specific_shop:
                details.append((shop.shop_type, shop.area, shop.date))
    return details

def find_most_common_shop(shop_list):
    shop_counts = {}
    for shop in shop_list:
        if shop.shop_type in shop_counts:
            shop_counts[shop.shop_type] += 1
        else:
            shop_counts[shop.shop_type] = 1
    most_common = max(shop_counts, key=shop_counts.get)
    return most_common

def write_to_file(output, filename):
    with open(filename, 'w') as f:
        f.write(str(output))

def get_item_price(shop_list, shop_type):
    for shop in shop_list:
        if shop.shop_type == shop_type:
            return shop.prices
    return None

def get_store_hours(shop_list, shop_type):
    for shop in shop_list:
        if shop.shop_type == shop_type:
            return shop.store_hours
    return None

while True:
    print("What type of data would you like to know?")
    print("1. Summarize all data")
    print("2. Summarize by area")
    print("3. Summarize by date")
    print("4. Detail by shop type")
    print("5. Find most common shop type")
    print("6. Get price of an item")
    print("7. Get store hours of an item")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")
    if choice == '1':
        data = summarize_all_data(shops)
        print(f"Area with most shops: {data['most_area']}")
        print(f"Date with most shops: {data['most_date']}")
        most_common_shop = find_most_common_shop(shops)
        print(f"Most common shop type: {most_common_shop}")

#Summarize by area (enter input: downtown or outletmall)
    elif choice == '2':
        area = input("Enter the area: ")
        count = summarize_by_area(shops, area)
        print(f"Number of shops in {area}: {count}")

#Summarize by date (enter input: 2023-05-01 or 2023-06-30)
    elif choice == '3':
        date = input("Enter the date (YYYY-MM-DD): ")
        count = summarize_by_date(shops, date)
        print(f"Number of shops on {date}: {count}")

#Summarize by goods (enter input: pants, shoes, shirts or coats)
    elif choice == '4':
        shop_type = input("Enter the shop type: ")
        details = detail_by_shop_type(shops, shop_type)
        print(f"Details of {shop_type} goods:")
        for detail in details:
            print(detail)

#Most trendy sold items
    elif choice == '5':
        most_common = find_most_common_shop(shops)
        print(f"Most common goods type: {most_common}")

# Get item price (enter input: pants, shoes, shirts or coats)
    elif choice == '6':
        shop_type = input("Enter the item's shop type: ")
        item_prices = get_item_price(shops, shop_type)
        if item_prices:
            print(f"Prices of {shop_type}: {item_prices}")
        else:
            print(f"{shop_type} not found in the store.")

# Get store hours of operation (enter input: pants, shoes, shirts or coats)
    elif choice == '7':
        shop_type = input("Enter the item's shop type: ")
        store_hours = get_store_hours(shops, shop_type)
        if store_hours:
            print(f"Store hours of {shop_type}: {store_hours}")
        else:
            print(f"{shop_type} not found in the store.")

# Get summary of all in an output file
    elif choice == '8':
        data = summarize_all_data(shops)
        write_to_file(data, 'shop_summary.txt')
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
