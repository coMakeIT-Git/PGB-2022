import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


class Build implements Runnable{
	int PlotNumber;
	String Name;
	String Walls;
	int change = 0;
	
	//Constructor
	Build(int plotNumber, String Name, String Walls){			
		this.PlotNumber = plotNumber;
		this.Name = Name;
		this.Walls = Walls;
	}
	
	//Method
	public void buildWalls(String Walls, String Name, int PlotNumber) {
		synchronized(this) {
			try {
				Thread.sleep(2000);				
				System.out.println("\nBuilding "+ Name + " at Plot number "+ PlotNumber + "..." + "\nWalls Built: "+ Walls + "\t\tThread ID:" + Thread.currentThread().getId());
				//System.out.println("\nWalls Built: "+ Walls + "\t\tThread ID:" + Thread.currentThread().getId());
			}
			catch(Exception e) {
			}
		}
	}
	
	//Run
	public void run() {
		this.buildWalls(this.Walls, this.Name, this.PlotNumber);
	}
	
}

class Threadpool{
	public static void main(String args[]) {
		Runnable r1 = new Build(101, "Castle", "Jewels");
		Runnable r2 = new Build(102, "Brick House", "Bricks");
		Runnable r3 = new Build(103, "Stone House", "Stone");
		Runnable r4 = new Build(104, "Tree House", "Wood");
		Runnable r5 = new Build(105, "Igloo", "Ice");
		
		ExecutorService pool = Executors.newFixedThreadPool(3);
		
		pool.execute(r1);
		pool.execute(r2);
		pool.execute(r3);
		pool.execute(r4);
		pool.execute(r5);
		pool.shutdown();
	}
}
