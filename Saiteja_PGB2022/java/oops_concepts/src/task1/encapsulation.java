package task1;

class encapsulation
{   private int penprice,penid,penmodelno;

public int getpenid() {
	return penid;
}
    public int getpenprice() {
    	return penprice;
    }
    public int getpenmodelno() {
    	return penmodelno;
    }
    public void setpenprice(int x) {
    	penmodelno = x;
    }
    public void setpenmodelno(int x) {
    	penmodelno = x;
    }
    public void setpenid(int x) {
    	penid = x;
    }
    public static void main(String args[])
    {
        encapsulation b=new encapsulation();
        b.setpenmodelno(12020);
        b.setpenprice(100);
        b.setpenid(1);
        System.out.println("pen id:"+ b.getpenid());
        System.out.println("pen model:"+ b.getpenmodelno());
        System.out.println("pen price:"+ b.getpenprice());
    }
}
