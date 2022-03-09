interface House{
	public void setWalls(String wall);
}

class MethodReference{
	private String Name;
	
	//Constructor
	MethodReference(String Name){
		System.out.println("Building...");
	}
	
	//static method
	public static void buildWalls(String Walls) {
		System.out.println("Walls Built: "+ Walls);
	}
	
	//Non-static method
	public void setName(String Name) {
		this.Name = Name;
		System.out.println("Name: " + Name);
	}
	
	public static void main(String args[]) {
		
		//Reference to a constructor
		House h1 = MethodReference::new;
		h1.setWalls("Tree House");
		
		//Instance Reference
		MethodReference ref = new MethodReference("Tree House");
		House h2 = ref::setName;
		h2.setWalls("Tree House");
		
		//Reference to static method
		House house = MethodReference::buildWalls;
		house.setWalls("Wood");		
	}
}