interface Find{
	int sub(int a, int b);
}

class p3{
	public static void main(String args[]){
		Find c1=(int a, int b)->{return (a-b);};
		System.out.println(c1.sub(10,20));

		Find c2=(int a, int b)->(a-b);
		System.out.println(c2.sub(10,20));
		
		Find c3=(a, b)->{return (a-b);};
		System.out.println(c3.sub(10,20));

		Find c4=(a, b)->(a-b);
		System.out.println(c4.sub(10,20)); 
	}
}