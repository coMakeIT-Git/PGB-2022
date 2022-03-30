package util;
import java.util.*;
public class Student {
String id;
String name;
String dob;
public boolean equals(Object obj) {
	if(this == obj) {
		return true;
	}		
	if(obj == null) {
		return false;
	}
	if(getClass()!= obj.getClass()) {
		return false;
	}
	Student z = (Student) obj;
	return this.getid().equals(z.getid());
	}
	public Student() {

	}
	public Student(String name) {
	super();
	this.name = name;
	}
	public String getid() {
	return id;
	}
	public void setid(String id) {
	this.id = id;
	}	
	public String toString() {
		return "Student [id=" + id + ", name=" + name + "]";
	}
	public int hashCode(){
	final int p = 17;
	int r = 1;
	r = p * r + ((id==null)?0:id.hashCode());

	return r;
	}
}