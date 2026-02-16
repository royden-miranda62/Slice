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

        String[] people = { "Amogh", "Bhautik", "Priyam", "Siddharth", "Royden" };
        int numOfPeople = people.length;

        MenuItem[] menu = {
                new MenuItem("null1", 3),
                new MenuItem("null2", 2),
                new MenuItem("null3", 1),
                new MenuItem("null4", 5)
        };
        int menuSize = menu.length;

        // array to store the number of times each item was ordered
        int[] orderCount = new int[menuSize];
        for (int i = 0; i < orderCount.length; i++)
            orderCount[i] = 0;

        MenuItem[][] selectedItems = new MenuItem[numOfPeople][menuSize];
        MenuItem slcItem;

        for (int j = 0; j < numOfPeople; j++) {

            System.out.println("Name: " + people[j]);

            System.out.println("Menu: ");
            System.out.printf("--------------------\n");
            System.out.printf("| No. | Item | Qty |\n");
            System.out.printf("--------------------\n");
            for (int i = 0; i < menu.length; i++)
                System.out.printf("| %-2s | %-5s | %-2s |\n",
                        (i + 1) + ".", menu[i].itemName, menu[i].itemQty);
            System.out.printf("--------------------\n");

            MenuItem[] itmStack = new MenuItem[menuSize];
            while (true) {
                System.out.print("Choose item with quantity: ");
                int itm = inp.nextInt();
                int qty = inp.nextInt();

                orderCount[itm - 1]++;

                MenuItem curItem = menu[itm - 1];
                int top = -1;

                if (qty > curItem.itemQty)
                    System.out.println("Error: Quantity chosen exceeds more than available quantity.");

                else {
                    curItem.itemQty -= qty;

                    slcItem = new MenuItem(curItem.itemName, qty);

                    if (top != menuSize - 1) 
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
            selectedItems[j] = itmStack;

            System.out.println(people[j] + "'s Order: ");
            System.out.printf("--------------------\n");
            System.out.printf("| Item | Qty |\n");
            System.out.printf("--------------------\n");
            for (int i = 0; i < itmStack.length; i++) {
                System.out.printf("| %-5s | %-2s |\n",
                        (i + 1) + ".", itmStack[i].itemName, itmStack[i].itemQty);
            System.out.printf("--------------------\n");
            }
        }

        inp.close();
    }
}
