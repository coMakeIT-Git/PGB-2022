public class facilitiesAvailable extends ambulanceBookings{
		String fname;
		double charges;
		int PhoneNumber;
		public facilitiesAvailable(String fname, double charges, int PhoneNumber) {
			this.fname = fname;
			this.charges = charges;
			this.PhoneNumber = PhoneNumber;
		}
		public void display() {

			System.out.println("Name of facility is-----" + fname);
			System.out.println("Charges of facility is------" + charges);
		}
		public void PrintDetails() {
			System.out.println("CALL FOR MORE QUERIES:---------"+PhoneNumber);
		}

}
