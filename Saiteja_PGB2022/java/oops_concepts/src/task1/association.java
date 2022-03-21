package task1;

//class bank
class penbrand
{
private String name;

//bank name
penbrand(String name)
{
this.name = name;
}

public String getbrandName()
{
return this.name;
}
}

//employee class
class price
{
private int amount;

//employee name
price(int amount)
{
this.amount = amount;
}

public int getpriceamount()
{
return this.amount;
}
}

//Association between both the
//classes in main method
class association
{
public static void main (String[] args)
{
penbrand bank = new penbrand("cello");
price emp = new price(100);

System.out.println(bank.getbrandName() +
" is price of " + emp.getpriceamount());
}
}