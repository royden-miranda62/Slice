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

"""STAGE 1 - PEOPLE"""

num_people = int(input("Enter the number of people: "))
print("Enter their names: ")
for i in range(num_people):
    name = input()
    people.append(name.title())

people.sort()  # sorting the list for fixed identification.

print("Who paid?")
for id, person in enumerate(people, start=1):
    print(f"{id}. {person}")
payer_id = int(input())

tuple(people)  # converting the list into a tuple to make it immutable.

print()


""" STAGE 2 - MENU """

while True:
    print("Enter menu items: \n")

    item_name = input("Item Name: ")
    item_price = float(input("Price: "))
    total_qty = int(input("Quantity Ordered: "))

    total_price = item_price * total_qty
    order_qty = 0

    menu.append([item_name, item_price, total_qty, total_price, order_qty])
    print()

    add_more_choice = input("Add more items? (Y/N): ")
    if add_more_choice in "nN":
        break

    print()

print()


""" STAGE 3 - ORDER """

for person in people:
    print(person)

    order = []

    while True:
        print("Menu")
        for id, item in enumerate(menu, start=1):
            print(f"{id}. {item}")

        item_id = int(input(f"Choose item (1-{len(menu)}): "))
        qty_chosen = int(input("Enter quantity: "))

        item_chosen = menu[item_id - 1] # mapping the chosen item to the menu
        
        order.append((item_chosen, qty_chosen))

        print()

        add_more_choice = input("Add more items? (Y/N): ")
        if add_more_choice in "nN":
            break

    orders.append(order)
