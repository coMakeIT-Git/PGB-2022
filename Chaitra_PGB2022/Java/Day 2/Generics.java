class Generics<K, V>{
	private K key;
	private V value;
	
	public void setKV(K key, V value) {
		this.key = key;
		this.value = value;
	}
	
	public K getKey() {
		return this.key;
	}
	
	public V getValue() {
		return this.value;
	}
	
	public static void main(String args[]) {
		Generics<String, Integer> g1 = new Generics<String, Integer>();
		Generics<Integer, String> g2 = new Generics<Integer, String>();
		
		g1.setKV("Luna", 101);
		g2.setKV(202, "Teddy");
		
		System.out.println("Key 1: "+ g1.getKey() + "\t" + "Value 1: " + g1.getValue());
		System.out.println("Key 2: "+ g2.getKey() + "\t" + "Value 2: " + g2.getValue());
		
	}
}

