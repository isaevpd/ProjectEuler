public class Triang{
	public static double triangle(double n){
		return n * (n + 1) / 2;
	}
	public static double pentagonal(double n){
		return n * (3 * n - 1) / 2;
	}
	public static double hexagonal(double n){
		return n * (2 * n - 1);
	}

	public static void main(String[] args){

		for (int t = 200; t < 100000; t++){
			for (int p = 130; p < 70000; p++){
				if (triangle(t) == pentagonal(p)){
					System.out.println(triangle(t));
					System.out.println(t);
				}
			}
		}
		System.out.println("Im done!");
	}
}