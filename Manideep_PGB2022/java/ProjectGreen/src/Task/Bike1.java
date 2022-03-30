class Bike1
{   private int gear,speed;
    Bike1()
    {
        this.speed=this.gear=0;
    }
    Bike1(int s,int g)
    {
        this.speed=s;
        this.gear=g;
    }
    public void changeGear(int cg)
    {
        this.gear+=cg;
    }
    public void speedUp()
    {
        this.speed+=5;
    }
    public void speedUp(int speed)
    {
        this.speed+=speed;
    }
    public void speedDown()
    {
        this.speed-=5;
    }
    public void speedDown(int speed)
    {
        this.speed-=speed;
    }
    public int getcurrentspeed(){return this.speed;}
    public int getcurrentgear(){return this.gear;}
    public static void main(String args[])
    {
        Bike1 b=new Bike1();
        System.out.println("gear is "+b.getcurrentgear());
        System.out.println("Speed is "+b.getcurrentspeed());
        b.speedUp(20);
        b.speedUp();
        b.changeGear(2);
        System.out.println("gear is "+b.getcurrentgear());
        System.out.println("Speed is "+b.getcurrentspeed());
    }
}