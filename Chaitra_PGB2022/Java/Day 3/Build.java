import java.util.*;

//Interface
interface House{
	public void setWalls(String wall);
	public void setRoof(String roof);
}

//Abstract class
abstract class HouseBuilder{
	public void buildWalls(String Walls) {
		System.out.println("Walls Built: "+ Walls);
	}
	public void buildRoof(String Roof) {
		System.out.println("Roof Built: " + Roof);
	}
	abstract int getPlotNumber();
}


class Build extends HouseBuilder implements House, Comparable<Build> {
	int PlotNumber;
	String Name;
	String Walls;
	String Roof;
	
	//Constructor
	Build(int plotNumber, String Name){
		System.out.println("\nBuilding "+ Name + " at Plot number "+ plotNumber + "...");
		this.PlotNumber = plotNumber;
		this.Name = Name;
	}
	
	@Override 
	public int compareTo(Build b)
    {
		int c = ((Build)b).getPlotNumber();
		return this.getPlotNumber() - c;
  
    }
	
	//Interface implementation
	public void setWalls(String wall) {
		this.Walls = wall;
	}
	public void setRoof(String roof) {
		this.Roof = roof;
	}
	
	//abstract method overridden
	int getPlotNumber() {
		return this.PlotNumber;
	}
	
	//Concrete Method
	public String getname() {
		return this.Name;
	}
	
	public static void main(String args[]) {	
		//Accessing methods
		Build house1 = new Build(53, "Castle");
		house1.setWalls("Jewels");
		house1.setRoof("Stone");
		house1.buildWalls(house1.Walls);
		house1.buildRoof(house1.Roof);
		
		Build house2 = new Build(100, "Tree House");
		house2.setWalls("Teak Wood");
		house2.setRoof("Rose Wood");
		house2.buildWalls(house2.Walls);
		house2.buildRoof(house2.Roof);
		
		Build house3 = new Build(20, "Igloo");
		house3.setWalls("Ice");
		house3.setRoof("Ice Bars");
		house3.buildWalls(house3.Walls);
		house3.buildRoof(house3.Roof);
		
		//Collections:List
		ArrayList<Build> Houses = new ArrayList<Build>();
		Houses.add(house1);
		Houses.add(house2);
		Houses.add(house3);
		
		//Sorting List
		System.out.println("\nSorting houses based on Plot Number...");
		Collections.sort(Houses);
		for(Build b : Houses) {
			System.out.println(b.getPlotNumber() + "\t" + b.getname());
		}
		
		//Collections:Set
		System.out.println("\nDisplaying HashSet of house objects...");
		Set<Build> houseSet = new HashSet<>();
		houseSet.add(house1);
		houseSet.add(house2);
		houseSet.add(house3);
		Iterator i = houseSet.iterator();
		while(i.hasNext()) {
			System.out.println(i.next());
		}
		
		//Collections:Map
		System.out.println("\nDisplaying HashMap of houses...");
		HashMap<Integer, String> houseMap = new HashMap<Integer, String>();
		houseMap.put(house1.getPlotNumber(), house1.Name);
		houseMap.put(house2.getPlotNumber(), house2.Name);
		houseMap.put(house3.getPlotNumber(), house3.Name);
		for(Map.Entry m : houseMap.entrySet()){    
		    System.out.println(m.getKey()+"\t"+m.getValue());    		
		}
		
		//Iteration using Stream
		System.out.println("\nIterating List of house objects using stream...");
		Houses.stream().forEach(house->System.out.println(house.getPlotNumber()+ "\t" + house.Name));
		
	}
}

