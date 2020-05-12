import java.lang.Math;

interface MyMath{
	double sqroot(double d);
}

class p4{
	public static void main (String args[]){
		MyMath m1 = (d)->Math.sqrt(d);
		System.out.println(m1.sqroot(25));

	}
}