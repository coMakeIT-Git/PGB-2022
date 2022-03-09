package day2;

public class Student {
	

		int id;
		int number;
		
		Student(int id){
			this.id = id;

		}
		public int getNumber() {
			System.out.println("Student ID : "+this.id+"\nStudent Number : "+this.number);
			return this.number;
		}
		public void setNumber(int n) {
			this.number= n;
		}
		@Override
		public boolean equals(Object obj) {
			if (obj == this) {
			// TODO Auto-generated method stub
			return true;
		}
			if (obj == null) {
				return false;
			}
			
			Student st = (Student) obj;
			return (st.getNumber() == this.number && st.id == this.id);

	}
		@Override
		public int hashCode() {
			// TODO Auto-generated method stub
			final int prime = 1;
			return (prime * this.id);
		}
		void record(int id) {
			System.out.println("Student ID (overloading 1):"+id);
		}
		void record(int id,int number) {
			System.out.println("Student ID (overloading 2):"+number);
		}
		public static void main(String args[]) {
			Student s1 = new Student(1);
			s1.setNumber(1234);
			System.out.println("Student Number Using getNumber():"+s1.getNumber());
			Student s2 = new Student(1);
			s2.setNumber(1234);
			System.out.println("Student Number Using getNumber():"+s1.equals(s2));
			s1.record(9);
			s1.record(4,145);
			
		}
	}

