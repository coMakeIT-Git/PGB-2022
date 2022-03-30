package comakeit;


abstract class Hospital{
	String doctor;
	String specialization;
	int years;
	public Hospital(String doctor, String specialization, int years) {
		this.doctor = doctor;
		this.specialization = specialization;
		this.years = years;
	}
	public String getDoctor() {
		return doctor;
	}
	public void setDoctor(String doctor) {
		this.doctor = doctor;
	}
	public String getSpecialization() {
		return specialization;
	}
	public void setSpecialization(String specialization) {
		this.specialization = specialization;
	}
	public int getYears() {
		return years;
	}
	public void setYears(int years) {
		this.years = years;
	}
	
	void appointment() {
		
	}
	
	void treatment() {
		
	}
	
}

class Patient{
	private String name;
	private int age;
	private String problem;
	public Patient(String name, int age, String problem) {
		super();
		this.name = name;
		this.age = age;
		this.problem = problem;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getProblem() {
		return problem;
	}
	public void setProblem(String problem) {
		this.problem = problem;
	}
}

class Apollo extends Hospital{

	public Apollo(String doctor, String specialization, int years) {
		super(doctor, specialization, years);
	}
	
	void appointment() {
		System.out.println("Appointment was booked with: "+ getDoctor());
	}
	void treatment() {
		System.out.println("Treatment was given");
	}
	
	void display(Patient patient) {
		System.out.println("Specialized in: "+getSpecialization());
		System.out.println("Years of Experience: "+getYears());
		System.out.println("Patient name: "+patient.getName());
		System.out.println("Patient age: "+patient.getAge());
		System.out.println("Patient problem: "+patient.getProblem());
		
	}
}

class Yashoda extends Hospital{

	public Yashoda(String doctor, String specialization, int years) {
		super(doctor, specialization, years);
	}
	void appointment() {
		System.out.println("Appointment was booked with: "+ getDoctor());
	}
	void treatment() {
		System.out.println("Treatment was given...");
	}
	
	void display(Patient patient) {
		System.out.println("Specialized in: "+getSpecialization());
		System.out.println("Years of Experience: "+getYears());
		System.out.println("Patient name: "+patient.getName());
		System.out.println("Patient age: "+patient.getAge());
		System.out.println("Patient problem: "+patient.getProblem());
		
	}
	
}

