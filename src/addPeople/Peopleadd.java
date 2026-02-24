import java.util.Scanner;

public class Peopleadd {
    public static void main(String[] args) {

        String payingPerson = null;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of people: ");
        int numPeople = sc.nextInt();
        sc.nextLine();

        String[] people = new String[numPeople];

        System.out.println("Enter the names of the people:");
        for (int i = 0; i < numPeople; i++) {
            System.out.print("Person " + (i + 1) + ": ");
            people[i] = sc.nextLine();
        }

        System.out.println("Enter the name of the person who is paying (OPTIONAL: press enter to skip):");
        String payer = sc.nextLine().trim();

        if(!payer.isEmpty()){
            payingPerson = payer;
        }
    }
}
