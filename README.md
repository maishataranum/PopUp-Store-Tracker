#The "Boston's Pop-Up ShopTracker" is a Python-based software designed for store owners and consumers in Boston to locate pop-up stores. Opening pop-up stores is a pretty common strategy for many branded shop owners to test their new merchandises’ sales. They are usually open for a short period of time, mostly during the summer and the location varies every year. It could be a small street shop or could be part of a shopping mall. One of the common problems for consumers is that it is difficult to keep track of these pop-up stores on when and where they will be open, as well as the merchandise that will be available in those stores. The software offers various functions, including summarizing goods availability in specific areas, store hours and time periods, providing detailed information about goods, their prices, and sorting them based on shop categories. Customers can utilize this tool to find shop details (location, goods, hours, etc) and owners can use the data to optimize shopping experiences, identify trends and meet customer demand. By using this software, both shop owners and customers can enhance their pop-up stores shopping experiences in Boston.

class Shop:
    def __init__(self, shop_type, area, date):
        self.shop_type = shop_type
        self.area = area
        self.date = date

shops = [Shop('Shoes', 'Downtown', '2023-06-25'),
          Shop('Shirts', 'OutletMall', '2023-06-27'),
          Shop('Pants', 'Downtown', '2023-06-27'),
          Shop('Coats', 'OutletMall', '2023-06-28'),
          Shop('Shirts', 'Downtown', '2023-06-29'),
          Shop('Shoes', 'OutletMall', '2023-06-30'),
          Shop('Pants', 'Downtown', '2023-06-30'),
          Shop('Coats', 'OutletMall', '2023-05-01'),
          Shop('Shirts', 'Downtown', '2023-05-01')]

def summarize_all_data(shop_list):
    downtown_count = summarize_by_area(shop_list, 'Downtown')
    outletmall_count = summarize_by_area(shop_list, 'OutletMall')
    dates = set([shop.date for shop in shop_list])
    date_counts = {}
    for date in dates:
        date_counts[date] = summarize_by_date(shop_list, date)
    most_date = max(date_counts, key=date_counts.get)
    if downtown_count > outletmall_count:
        most_area = 'Downtown'
    else:
        most_area = 'OutletMall'
    return {'most_area': most_area,'most_date': most_date, 'downtown_count': downtown_count, 'outletmall_count': outletmall_count, 'date_counts': date_counts}

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

while True:
    print("What type of data would you like to know?")
    print("1. Summarize all data")
    print("2. Summarize by area")
    print("3. Summarize by date")
    print("4. Detail by shop type")
    print("5. Find most common shop type")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        data = summarize_all_data(shops)
        print(f"Area with most shops: {data['most_area']}")
        print(f"Date with most shops: {data['most_date']}")
        most_common_shop = find_most_common_shop(shops)
        print(f"Most common shop type: {most_common_shop}")


    elif choice == '2':
        area = input("Enter the area: ")
        count = summarize_by_area(shops, area)
        print(f"Number of shops in {area}: {count}")
    elif choice == '3':
        date = input("Enter the date (YYYY-MM-DD): ")
        count = summarize_by_date(shops, date)
        print(f"Number of shops on {date}: {count}")
    elif choice == '4':
        shop_type = input("Enter the shop type: ")
        details = detail_by_shop_type(shops, shop_type)
        print(f"Details of {shop_type} goods:")
        for detail in details:
            print(detail)
    elif choice == '5':
        most_common = find_most_common_shop(shops)
        print(f"Most common shop type: {most_common}")
    elif choice == '6':
        data = summarize_all_data(shops)
        write_to_file(data, 'shop_summary.txt')
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
