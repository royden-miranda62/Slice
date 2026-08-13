"""GLOBAL DATA STRUCTURES"""

# `people` stores the names of the people involved
# in the split.
people = []

# `menu` stores ordered items, represented by the tuple:
# (item name, item price, total quantity, total price, split flag).
menu = []

# `orders` stores orders for each person as a nested list,
# with each inner list representing an order for a person.
# each inner list is a list of tuples, where each tuple is an item,
# represented by the tuple: (item name, quantity ordered).
# since `people` is sorted, the position of a list in `order`
# corresponds to a person in `people`.
orders = []

# `bill` stores the final amount each person has to pay.
bill = []


"""STAGE 1 - PEOPLE"""

num_people = int(input("Enter the number of people: "))
print("Enter their names: ")
for i in range(num_people):
    name = input("    -> ")
    people.append(name.title().strip())
people.sort()  # sorting the list for fixed indexing.

print(f"Who paid? (1-{num_people})")
for id, person in enumerate(people, start=1):
    print(f"{id}. {person}")
payer_id = int(input("    -> ")) - 1 

tuple(people)  # converting the list into a tuple to make it immutable.

print()


""" STAGE 2 - MENU """

print("Enter menu items: \n")
while True:
    item_name = input("Item name: ").title().strip()
    item_price = float(input("Price: "))
    total_qty = int(input("Quantity ordered: "))
    shared_choice = input("Item shared? (Y/N): ")

    total_price = item_price * total_qty
    shared_item = True if shared_choice in "yY" else False
    ordered_qty = 0

    menu.append([item_name, item_price, total_qty, total_price, shared_item, ordered_qty])
    print()

    add_more_choice = input("Add more items? (Y/N): ")
    if add_more_choice in "nN":
        break

    print()

tax_amount = float(input("Tax: "))

print()


""" STAGE 3 - ORDER """

for person in people:
    print(f"        {person}'s Order:\n")

    order = []

    while True:
        print("        Menu")
        print("Item No.\tItem Name")
        for id, item in enumerate(menu, start=1):
            print(f"{id}.\t{item[0]}")

        item_id = int(input(f"Choose item (1-{len(menu)}): ")) - 1
        item_chosen = menu[item_id]  # mapping the chosen item to the menu

        # item index reference: 
        # 0 = item name ; 1 = item price ; 2 = total quantity
        # 3 = total price ; 4 = shared item ; 5 = ordered quantity

        while True: 
            qty_chosen = int(input("Enter quantity: "))
            if qty_chosen <= 0:
                print("Invalid quantity. Input a positive quantity.")
            else:
                if item_chosen[4] == True: # if item is shared
                    item_chosen[5] += qty_chosen # chosen quantity can exceed total quantity
                    print(f"{qty_chosen} x {item_chosen[0]} added.")
                    break
                else: # if item is not shared
                    if qty_chosen + item_chosen[5] > item_chosen[2]: # chosen quantity cannot exceed total quantity
                        print(f"Cannot add {qty_chosen} of {item_chosen[0]}.")
                    else:
                        item_chosen[5] += qty_chosen  
                        print(f"{item_chosen[0]} added.")
                    break
            
        order.append((item_id, qty_chosen))

        print()

        add_more_choice = input("Add more items? (Y/N): ")
        if add_more_choice in "nN":
            break

        print()

    orders.append(order)

    print()

print()


""" STAGE 4 - CALCULATE """

for order in orders:
    bill_amount = tax_amount / num_people # initialize bill to the tax pp 

    for item in order:
        item_id = item[0]
        ordered_qty = item[1]
        menu_item = menu[item_id]

        # if item is shared, 
        #     price per person = total price / order count
        #     item price = price per person x ordered quantity
        if menu_item[4]:
            bill_amount += (menu_item[3] / menu_item[5]) * ordered_qty

        # if item is not shared item price remains as is.
        else:
            bill_amount += menu_item[1]

    bill.append(bill_amount)

""" STAGE 5 - DISPLAY   """
print("Final Amounts\n")
for i in range(num_people):
    print(f"{people[i]}: Rs. {round(bill[i], 2)}")