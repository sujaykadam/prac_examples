interface Compute{
	void add(int a, int b);
}

class p2{
	public static void main(String args[]){
		Compute c1=(int a, int b)->{System.out.println(a+b);};
		c1.add(10,20);

		Compute c2=(int a, int b)-> System.out.println(a+b);
		c2.add(10,20);
		
		Compute c3=(a, b)->{System.out.println(a+b);};
		c3.add(10,20);

		Compute c4=(a, b)-> System.out.println(a+b);
		c4.add(10,20); 
	}
}