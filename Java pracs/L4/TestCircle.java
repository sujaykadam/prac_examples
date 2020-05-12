class Circle{
	private double radius;

	public Circle(double radius){
		this.radius=radius;
	}

	public double area(){
		return 3.1459*radius*radius;
	}

	public double circum(){
		return 3.1459*2*radius;
	}
}

class TestCircle{
	public static void main(String args[]){
		Circle c1= new Circle(5.256);
		System.out.println("Area: "+c1.area()+" Circumference: "+c1.circum());
	}
}
