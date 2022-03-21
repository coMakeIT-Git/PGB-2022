import java.util.*;

//Library interface for all members
interface Library{
	List<Books> books = new ArrayList<Books>();	
}

class Books{
	String Name;
	String Author;
	String Type;
	Books(String Name, String Author){
		this.Name = Name;
		this.Author = Author;
		this.Type = "";
	}
}

//Inheritance: Books - Fiction, Non-Fiction
class Fiction extends Books{	
	Fiction(String Name, String Author){
		super(Name,Author);
		this.Type = "Fiction";
	}
}

class NonFiction extends Books{	
	NonFiction(String Name, String Author){
		super(Name, Author);
		this.Type = "Non-Fiction";
	}
}

//Abstract class for Library Management
abstract class LibraryManagement{
	public abstract void viewBooks();
	public abstract boolean checkAvailability(Books b);
	public abstract boolean approveIssue(Books b);
	
}

//Librarian manages the Library
class Librarian extends LibraryManagement implements Library{
	
	public void viewBooks(){
		System.out.println("\nName\t\tAuthor\t\tType");
		for(int i=0;i<20;i++) {
			System.out.print("---");
		}
		System.out.println();
		for(Books x : books) {
			System.out.println(x.Name + "\t" + x.Author + "\t" + x.Type);
		}
	}
	
	public boolean checkAvailability(Books b) {
		if(books.contains(b)) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public boolean approveIssue(Books b) {
		if(checkAvailability(b)) {
			return true;
		}
		else {
			return false;
		}
	}
}


//Aggregation: Student "has an" address
class Address {  
	String Street, Door;   
	public Address(String Door, String Street) {  
	    this.Street = Street;  
	    this.Door = Door;  	   
	}    
}  

//Student uses the library
//Encapsulation of Student data using private and getters-setters
class Student implements Library{
	String Name;
	private int ID;
	private String IssueStatus;
	Address address;
	
	Student(String Name, int ID){
		this.Name = Name;
		this.ID = ID;	
	}
	
	Student(String Name, int ID, Address a){
		this.Name = Name;
		this.ID = ID;	
		this.address = a;
	}
	
	public void setIssueStatus(String IS) {
		this.IssueStatus = IS;
	}
	
	public String getIssueStatus() {
		return this.IssueStatus;
	}
	
	//Polymorphism : Method issueBook() has two forms
	public void issueBook(Books b, String Name, Map<Books, Student> IL) {
		Librarian l = new Librarian();
		if(l.approveIssue(b)) {
			//Associating Student with book
			IL.put(b, this);
			System.out.println("\nBook " + '"' + b.Name + '"' + " issued by " + Name + "...");
			int index = books.indexOf(b);
			books.remove(index);		
			setIssueStatus("True");
		}
		else {
			System.out.println("\nSorry " + Name + ", Book "  + '"' + b.Name + '"' + " is not available!");
		}
	}
	
	public void issueBook(Books b, String Name, int ID, Map<Books, Student> IL) {
		Librarian l = new Librarian();
		if(l.approveIssue(b)) {
			//Associating Student with book
			IL.put(b, this);
			System.out.println("\nBook " + '"' + b.Name + '"' +  " issued by " + Name + " having ID " + ID + "...");
			int index = books.indexOf(b);
			books.remove(index);		
			setIssueStatus("True");
		}
		else {
			System.out.println("Book " + b.Name + " not available");
		}
	}
	
	public void returnBook(Books b) {
		System.out.println("\nReturning book " + '"' + b.Name + '"' + "...");
		books.add(b);
		setIssueStatus("False");
	}
	
}

class library implements Library{
	public static void main(String args[]) {
		//Adding Books to the Library
		Books b1 = new Books("Famous Five", "Enid Blyton");
		Fiction f1 = new Fiction("Harry Potter", "J.K. Rowling");		
		Fiction f2 = new Fiction("Nancy Drew", "Carolyn Keene");
		NonFiction nf1 = new NonFiction("The Alchemist", "Paulo Coelho");
		
		books.add(b1);
		books.add(f1);
		books.add(f2);
		books.add(nf1);
		
		//Creating Issue List
		Map<Books, Student> IssueList = new HashMap<Books, Student>();
		
		//Get the list of books
		Librarian l = new Librarian();
		l.viewBooks();		
						
		//Adding student address
		Address a1 = new Address("H1", "Street 9");
		Address a2 = new Address("L2", "Street 16");
		
		//Creating a student instances
		Student s1 = new Student("Luna", 101, a1);	//Aggregation with address
		Student s2 = new Student("Jane", 202);
		
		//student issues a book
		s1.issueBook(nf1, s1.Name, IssueList);				
		//Get the list of books		
		l.viewBooks();
		
		//Printing the IssueList
		System.out.println("\n***Issue List***");		
		for (Map.Entry<Books, Student> entry : IssueList.entrySet()) {
			System.out.println("Book: " + entry.getKey().Name + "\tStudent: " + entry.getValue().Name);
		}	
		
		//student issues a book not available
		s2.issueBook(nf1, s2.Name, IssueList);	
		s2.issueBook(f1, s2.Name, IssueList);
		l.viewBooks();
		//Printing the IssueList
		System.out.println("\n***Issue List***");		
		for (Map.Entry<Books, Student> entry : IssueList.entrySet()) {
            System.out.println("Book: " + entry.getKey().Name + "\tStudent: " + entry.getValue().Name);
    	}			
		
		//Return the book
		s1.returnBook(nf1);
		l.viewBooks();				
	}
}

