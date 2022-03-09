class Employee{
	int ID;
	String Name;
	
	//Constructors
	Employee(){
		System.out.println("**Employee Details**");
	}
	Employee(int ID, String Name){
		this.ID = ID;
		this.Name = Name;
	}
	
	//Getter and Setter Methods
	public int getID() {
		return this.ID;
	}
	public String getName() {
		return this.Name;
	}
	
	public void setID(int ID) {
		this.ID = ID;
	}
	public void setName(String Name) {
		this.Name = Name;
	}
	
	public void setNameID(String Name, int ID) {
		this.Name = Name;
		this.ID = ID;
	}
	
	//Overloading
	public void display() {
		System.out.println("Name:" + this.getName() + " " + "ID: " + this.getID());
	}
	
	public void display(String Name) {
		this.setName(Name);
		System.out.println("Name:" + this.getName() + " " + "ID: " + this.getID());
	}
	
	//Equals and HashCode
	@Override
	public boolean equals(Object obj) {
		if(this == obj) {
			return true;
		}
		if(!(obj instanceof Employee))
			return false;
		Employee emp = (Employee) obj;
		return (emp.ID==this.ID && emp.Name==this.Name);
	}
	
	public int hashCode() {
		return this.ID;
	}
	
	public static void main(String args[]) {
		Employee e1 = new Employee();
		Employee e2 = new Employee(101, "Luna");
		Employee e3 = new Employee(101, "Luna");
		Employee e4 = new Employee(202, "Teddy");
		
		if(e2.equals(e3)) {
			System.out.println("Name 1:" + e2.Name + " " + "ID 1: " + e2.ID);
			System.out.println("Name 2:" + e2.Name + " " + "ID 2: " + e2.ID);
			System.out.println("The objects are equal.");
		}
		if(e2.hashCode() == e3.hashCode()) {
			System.out.println("The hashcodes are equal.");
			System.out.println("");
		}
		
		e4.display();
		e4.display("Bear");
		
		
	}
	
	
}
	
