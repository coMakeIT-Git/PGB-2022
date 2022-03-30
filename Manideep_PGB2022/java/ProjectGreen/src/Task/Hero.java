

class Hero extends Bike{ 
    public int gear,speed;
    Hero()
    {
        this.gear=0;
        this.speed=0;
    }
    public void currentstate()
    {
        System.out.println("Gear="+this.gear+"\nSpeed is "+this.speed);
    }
    void run(){System.out.println("running safely");}  
    void changeGear(int newValue){this.gear=newValue;};;
    void speedUp(int increment){this.speed+=increment;}
    void applyBrakes(int decrement){this.speed-=decrement;};
    public static void main(String args[]){  
     Honda obj = new Honda();  
     obj.run();
     obj.changeGear(1);
     obj.speedUp(30);
     obj.currentstate();
     obj.applyBrakes(10);
     obj.currentstate();
    }
}
