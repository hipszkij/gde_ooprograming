public class Book {
    private String id;
    private String title;
    private String author;
    private int publicationYear;

    public Book(String id, String title, String author, int publicationYear) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.publicationYear = publicationYear;
    }

    public String getId() {
        return this.id;
    }

    public setId(int id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Book{" +
               "id='" + this.id + '\'' +
               ", title='" + this.title + '\'' +
               ", author='" + this.author + '\'' +
               ", publicationYear=" + this.publicationYear +
               '}';
    }
}
