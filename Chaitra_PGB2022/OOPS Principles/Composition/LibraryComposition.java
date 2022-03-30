    import java.io.*;   
    import java.util.*;   
   
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

    //Composition : Library is composed of books  
    class Library {   
        // reference to refer to list of books.   
        private final List<Books> books;   
        Library(List<Books> books)  
        {  
            this.books = books;  
        }   
        //Getting total number of books  
        public List<Books> getTotalbooksInLibrary()   
        {   
            return books;   
        }   
    }   
    class LibraryComposition{   
        public static void main(String[] args)   
        {   
            //Creating the Objects of Books class.   
        	Books b1 = new Books("Famous Five", "Enid Blyton");
        	Books b2 = new Books("Harry Potter", "J.K. Rowling");		
        	Books b3 = new Books("Nancy Drew", "Carolyn Keene");
        	Books b4 = new Books("The Alchemist", "Paulo Coelho");
    		
            //Creating list which contains the no. of books.   
            List<Books> books = new ArrayList<Books>();   
            books.add(b1);   
            books.add(b2);   
            books.add(b3);
            books.add(b4);
            Library Library = new Library(books);   
            List<Books> book = Library.getTotalbooksInLibrary();   
            for (Books b : book) {
            	System.out.println("Name : " + b.Name + "\tAuthor: " + b.Author);   
            }   
        }   
    }  
