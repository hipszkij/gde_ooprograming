public class Member {
    private String memberId;
    private String name;
    private String email;

    public Member(String memberId, String name, String email) {
        this.memberId = memberId;
        this.name = name;
        this.email = email;
    }

    @Override
    public String toString() {
        return "Member{" +
               "memberId='" + this.memberId + '\'' +
               ", name='" + this.name + '\'' +
               ", email='" + this.email + '\'' +
               '}';
    }
}
