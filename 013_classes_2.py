# interface Printable {
#     void printInfo();
# }
# class Book implements Printable {
#     public void printInfo() {
#         System.out.println("Це книга");
#     }
# }
# public class Main {
#     static void printDocument(Printable doc) {
#         doc.printInfo();
#     }
#     public static void main(String[] args) {
#         Book book = new Book();
#         printDocument(book);
#     }
# }

class Book:
    def print_info(self):
        print("Це книга")

class Report:
    def print_info(self):
        print("Це звіт: фінансовий звіт за місяць")

def print_document(doc):
    doc.print_info()

book = Book()
print_document(book) 

report = Report()
print_document(report)