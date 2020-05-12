import java.io.*;
import java.lang.Math.*;

class Circle{
	private double radius;

	public Circle(double radius){
		this.radius=radius;
	}

	public void show(){
		System.out.println("Radius: "+radius);
	}
	public void area(){
		double res=Math.PI*Math.pow(radius,2);
		System.out.printf("Area: %.2f",res);
	} 
}

class CircleTest{
	public static void main(String ars[])throws IOException{
		
		double radius=0.0;

		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);

		System.out.println("Enter radius: ");
		radius=Double.parseDouble(br.readLine());

		Circle c1 = new Circle(radius);
		c1.show();
		c1.area();
	}

}