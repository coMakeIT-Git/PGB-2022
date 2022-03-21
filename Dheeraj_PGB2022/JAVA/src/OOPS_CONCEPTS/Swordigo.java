package OOPS_CONCEPTS;

import java.util.ArrayList;

interface Game {
	void details();
	void setType();
}

// Inheritance and Abstraction
abstract class MobileGame implements Game{
	public String type;
	
	// Polymorphism
	@Override 
	public void setType() {
		this.type = "Mobile";
	}
	
	// Abstraction
	abstract void minReq(String Name);
	
}


class skin{
	String name;
	int skinID;
	
	skin(String name, int skinID){
		this.name = name;
		this.skinID = skinID;
	}
	
	public void printDetails() {
		System.out.println("Skin Name : "+this.name+", Skin ID : "+this.skinID);
	}
	
}


class Player{
	String userName;
	int userID;
	// Encapsulation
	private int passwordHash;
	// Encapsulation
	private int coins = 0;
	// Encapsulation
	private int age = 0;
	public ArrayList<skin> skins = new ArrayList<skin>();
	
	Player(){
		this.userName = "Guest";
		this.userID = this.userName.hashCode();
		this.setPasswordHash("Guest");
	}
	
	Player(String userName, String password, int age){
		this.userName = userName;
		this.userID = this.userName.hashCode();
		this.setPasswordHash(password);
		this.setAge(age);
	}

	// Encapsulation
	public void setPasswordHash(String password) {
		this.passwordHash = genPasswordHash(password);
	}
	
	int genPasswordHash(String password) {
		return password.hashCode();
	}
	
	String getUserName() {
		return this.userName;
	}
	
	int getUserID() {
		return this.userID;
	}
	
	int getRemCoins() {
		return this.coins;
	}
	
	int addCoins(int coins) {
		this.coins += coins;
		return this.coins;
	}
	
	void getPlayerDetails() {
		System.out.println("Player Name : "+this.userName+"\nPlayer ID : "+this.userID+"\nRemaining Coins : "+this.coins);
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}
	
    public ArrayList<skin> getTotalOwnedSkins(){        
        return skins;   
     } 
	
}

//Inheritance
public class Swordigo extends MobileGame{
	int Downloads, size, ram, age, androidVersion;
	float Version;
	String Company, Name;
	public ArrayList<Player> onlinePlayerList = new ArrayList<Player>();
	public Object player;
	
	
	// Polymorphism
	Swordigo(){
		this.player = new Player();
		this.onlinePlayerList.add((Player) this.player);
		details();
	}
	
	// Polymorphism
	Swordigo(String name, String password, int age){
		if (validateAge(age)) {
			this.player = new Player(name, password, age);
			this.onlinePlayerList.add((Player) this.player);
		} else {
			System.out.println("Age Requirements Not Met");
		}
		details();
		
	}
	
	Swordigo(ArrayList<Player> opl){
		for (Player p : opl) { 
			this.onlinePlayerList.add(p);
		}
	}

	// Polymorphism
	@Override
	public void details() {
		this.Name = "Swordigo";
		this.Downloads = 10000000;
		this.Version = (float) 1.1;
		this.Company = "Dheeraj Inc";
	}

	// Polymorphism
	@Override
	void minReq(String Name) {
		this.ram = 4;
		this.age = 18;
		this.androidVersion = 8;
	}
	
	boolean validateAge(int age) {
		if (age < this.age){
			return false;
		}
		return true;
	}
	
	public void addOnlinePlayer(Player p) {
		this.onlinePlayerList.add((Player) p);
	}
	
	public void addOnlinePlayer(String name, String password, int age) {
		this.player = new Player(name, password, age);
		this.onlinePlayerList.add((Player) this.player);
	}
	
	public ArrayList<Player> listOnlinePlayers() {
		return this.onlinePlayerList;
	}
	
	
	public static void main(String[] args) {
		
		// Assosiation
		Player player1 = new Player("Dheeraj", "notapasswordlol123", 21);
		skin s1 = new skin("Glacier", 1011);
		skin s2 = new skin("Fire", 1012);
		skin s3 = new skin("Ice", 1013);
		
		player1.skins.add(s1);
		player1.skins.add(s2);
		player1.skins.add(s3);
		
		// Aggregation
		System.out.println("Player '"+player1.getUserName()+"' Has Skin: \n");
		s1.printDetails();
		
		
		System.out.println("\nPrinting Online Players List : \n");
		Player p1 = new Player("Rahul", "lol123", 20);
		Player p2 = new Player("Rajesh", "lol123", 20);
		
		ArrayList<Player> pl = new ArrayList<Player>();   
		pl.add(p1);
		pl.add(p2);
		
		Swordigo game1 = new Swordigo(pl);
		
		game1.listOnlinePlayers();
        
		// Composition in Java
        ArrayList<Player> playerlist = game1.listOnlinePlayers();
        for (Player p : playerlist) {   
    		p.getPlayerDetails();
        }  
        
    }   
	
}