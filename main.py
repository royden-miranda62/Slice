import tabulate as tb

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


"""FUNCTIONS"""


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
payer_id = int(input("    -> "))

tuple(people)  # converting the list into a tuple to make it immutable.

print()


""" STAGE 2 - MENU """

print("Enter menu items: \n")
while True:
    item_name = input("Item name: ").title().strip()
    item_price = float(input("Price: "))
    total_qty = int(input("Quantity ordered: "))
    split_choice = input("Item shared? (Y/N): ")

    total_price = item_price * total_qty
    split_flag = True if split_choice in "yY" else False
    ordered_qty = 0

    menu.append([item_name, item_price, total_qty, total_price, split_flag, ordered_qty])
    print()

    add_more_choice = input("Add more items? (Y/N): ")
    if add_more_choice in "nN":
        break

    print()

print()


""" STAGE 3 - ORDER """

for person in people:
    print(f"        {person}'s Order:")

    order = []

    while True:
        print("    Menu")
        print("No.\tItem Name\tRemaining Quantity")
        for id, item in enumerate(menu, start=1):
            print(f"{id}.\t{item[0]}\t{item[4]}")

        item_id = int(input(f"Choose item (1-{len(menu)}): "))
        while True: 
            qty_chosen = int(input("Enter quantity: "))
            if qty_chosen <= 0:
                print("Invalid quantity.")
            else:
                break
            

        item_chosen = menu[item_id - 1]  # mapping the chosen item to the menu

        # item index reference: 
        # 0 = item name ; 1 = item price ; 2 = total quantity
        # 3 = total price ; 4 = split flag ; 5 = ordered quantity
        
        if item_chosen[4] == True:
            item_chosen[5] += qty_chosen
            print(f"{item_chosen[0]} added.")
        else: 
            # subtracting chosen quantity from remaining quantity
            item_chosen[5] += qty_chosen
            if qty_chosen >= item_chosen[2]:
                print(f"{item_chosen[0]} added.")
            else:
                print(f"Cannot add {qty_chosen} of {item_chosen[0]}.")

        order.append((item_chosen, qty_chosen))

        print()

        add_more_choice = input("Add more items? (Y/N): ")
        if add_more_choice in "nN":
            break

        print()

    orders.append(order)

print(orders)