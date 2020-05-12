import java.io.*;

class Rectangle{
	private double length;
	private double width;

	public Rectangle(double length,double width){
		this.length=length;
		this.width=width;
	}

	public void show(){
		System.out.println("Length: "+length+" Width: "+width);
	}
	public void area(){
		double res=length*width;
		System.out.println("Area: "+res);
	} 
}

class RectangleTest{
	public static void main(String ars[])throws IOException{
		
		double len=0;
		double wi=0;

		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);

		System.out.println("Enter length:");
		len=Double.parseDouble(br.readLine());
		System.out.println("Enter width:");
		wi=Double.parseDouble(br.readLine());

		Rectangle r1 = new Rectangle(len,wi);
		r1.show();
		r1.area();
	}

}