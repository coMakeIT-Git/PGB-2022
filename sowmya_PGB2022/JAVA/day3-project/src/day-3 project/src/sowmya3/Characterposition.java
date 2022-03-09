package sowmya3;
import java.util.*;
public class Characterposition {
	public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("enter your name:");
        String str = input.nextLine();

        char []data=str.toCharArray();
        Set s = new HashSet();
        for(int i=0; i<data.length; i++){
            s.add(data[i]);
        }
        Object[] s1 = s.toArray();

        System.out.print("{ ");
        for(int i=0; i<s.size(); i++){
            System.out.print(s.toArray()[i]+"=");
            Collection t = new ArrayList();
            char c=(Character) s1[i];
            for(int j=0;j<data.length; j++){
                if(c==data[j]){
                    t.add(j);
                }
            }
            System.out.print(t+ ", ");

        }
        System.out.print("}");

    }

}
