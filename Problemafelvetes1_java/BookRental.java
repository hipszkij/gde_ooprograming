import java.time.LocalDate;

public class BookRental {
    private String loanId;
    private Book book;
    private Member member;
    private LocalDate issueDate;
    private LocalDate dueDate;

    public BookRental(String loanId, Book book, Member member, LocalDate issueDate, LocalDate dueDate) {
        this.loanId = loanId;
        this.book = book;
        this.member = member;
        this.issueDate = issueDate;
        this.dueDate = dueDate;
    }

    @Override
    public String toString() {
        return "Loan{" +
               "loanId='" + this.loanId + '\'' +
               ", book=" + this.book +
               ", member=" +this.member +
               ", issueDate=" + this.issueDate +
               ", dueDate=" + this.dueDate +
               '}';
    }
}
