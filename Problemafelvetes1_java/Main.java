import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        // Könyvek létrehozása
        Book book1 = new Book("B001", "1984", "George Orwell", 1949);
        Book book2 = new Book("B002", "Brave New World", "Aldous Huxley", 1932);

        // Tagok létrehozása
        Member member1 = new Member("M001", "John Doe", "john.doe@example.com");
        Member member2 = new Member("M002", "Jane Smith", "jane.smith@example.com");

        // Kölcsönzések létrehozása
        Loan loan1 = new Loan("L001", book1, member1, LocalDate.of(2022, 3, 1), LocalDate.of(2022, 3, 15));
        Loan loan2 = new Loan("L002", book2, member2, LocalDate.of(2022, 3, 5), LocalDate.of(2022, 3, 19));

        // Információk megjelenítése
        System.out.println("Könyvek:");
        System.out.println(book1);
        System.out.println(book2);
        System.out.println();

        System.out.println("Tagok:");
        System.out.println(member1);
        System.out.println(member2);
        System.out.println();

        System.out.println("Kölcsönzések:");
        System.out.println(loan1);
        System.out.println(loan2);
        System.out.println();
    }
}
