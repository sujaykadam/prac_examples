interface Center{
	void nrc();
	default void cab(){
		System.out.println("Center is doing cab");
	}
}

class Mah implements Center{
	public void nrc(){
		System.out.println("Mah is doing nrc");
	}
}

class test{
	public static void main(String args[]){
		Mah m = new Mah();
		m.nrc();
		m.cab();
		
		//g uses lambda function
		Center g = ()->{System.out.println("Guj is doin nrc");};
		g.nrc();
		g.cab();

	}
}