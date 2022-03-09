class CheckedException{
	public static void main(String args[]) {
		try {
			Class c = Class.forName("ClassXYZ");
		}
		catch(ClassNotFoundException e) {
			System.out.println("Error: Class not found!");
		}
		
	}
}

