import java.util.Scanner;
class Program{
   public static void main(String args[]){
      Scanner scanner = new Scanner(System.in);
      System.out.println("Enter the number:");
      int num = scanner.nextInt();
      int factorial = fact(num);
      int multiple = mult(num);
      System.out.println(factorial);
      System.out.println(multiple);
   }
   static int fact(int n)
   {
       int output;
       if(n==1){
         return 1;
       }
       output = fact(n-1)* n;
       return output;
   }
   static int mult(int num) {
   		return (num*num);
}
}