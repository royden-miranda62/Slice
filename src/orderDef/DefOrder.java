package orderDef;

import java.util.Scanner;

// menu item declaration
class MenuItem {
    String itemName;
    int itemQty;

    MenuItem(String n, int q) {
        itemName = n;
        itemQty = q;
    }
}

public class DefOrder {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);

        // dummy person list
        String[] people = { "Amogh", "Bhautik", "Priyam", "Siddharth", "Royden" };
        int numOfPeople = people.length;

        // dummy menu
        MenuItem[] menu = {
                new MenuItem("null1", 3),
                new MenuItem("null2", 2),
                new MenuItem("null3", 1),
                new MenuItem("null4", 5)
        };
        int menuSize = menu.length;

        // array to store the number of times each item was ordered
        int[] orderCount = new int[menuSize];
        for (int item = 0; item < orderCount.length; item++)
            orderCount[item] = 0;

        // 2d array to store orders for each person
        // [i][j]: i identifies a person, j identifies an order
        MenuItem[][] selectedItems = new MenuItem[numOfPeople][menuSize];
        MenuItem slcItem;

        for (int person = 0; person < numOfPeople; person++) {
            System.out.println("Name: " + people[person]);

            // displaying menu
            System.out.println("Menu: ");
            System.out.printf("--------------------\n");
            System.out.printf("| No. | Item | Qty |\n");
            System.out.printf("--------------------\n");
            for (int i = 0; i < menu.length; i++)
                System.out.printf("| %-2s | %-4s | %-2s |\n",
                        (i + 1) + ".", menu[i].itemName, menu[i].itemQty);
            System.out.printf("--------------------\n");

            // item stack to hold items for each person, gets reset on every iteration
            MenuItem[] itmStack = new MenuItem[menuSize];
            int top = -1;

            while (true) {
                System.out.print("Choose item with quantity: ");
                int itm = inp.nextInt();
                int qty = inp.nextInt();

                // indicates that an item has been ordered by one person
                orderCount[itm - 1]++;

                MenuItem curItem = menu[itm - 1];

                if (qty > curItem.itemQty)
                    System.out.println("Error: Quantity chosen exceeds available quantity.");

                else {
                    // prevents the item from being over-ordered by the next person
                    curItem.itemQty -= qty;

                    slcItem = new MenuItem(curItem.itemName, qty);
                    itmStack[++top] = slcItem;
                }

                System.out.print("Add more? (y/n): ");
                char ch = inp.next().charAt(0);
                if (ch == 'n' || ch == 'N')
                    break;
                else if (top == menuSize - 1) {
                    System.out.println("Cannot choose more items.");
                    break;
                }
            }

            // displaying person's order
            System.out.println("\n" + people[person] + "'s Order: ");

            System.out.print("--------------\n");
            System.out.print("| Item | Qty |\n");
            System.out.print("--------------\n");
            for (int i = 0; i < itmStack.length - 1; i++)
                System.out.printf("| %-5s | %-2s |\n",
                        itmStack[i].itemName, itmStack[i].itemQty);
            System.out.print("--------------\n");

            // adding items to 2d array
            selectedItems[person] = itmStack;
        }

        

        inp.close();
    }
}
