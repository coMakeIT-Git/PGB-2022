
public class medicineTypes {  
		static String type, scope, form; 
		  
		protected medicineTypes(String type, String scope, String form) {  
		    medicineTypes.type = type;  
		    medicineTypes.scope = scope;  
		    medicineTypes.form = form;  
		}  
		void display(){  
			System.out.println(type+" can be used for "+scope);  
			System.out.println(form+" is the only form we prefer");  
			}  
}
