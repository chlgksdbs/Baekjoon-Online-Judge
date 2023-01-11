import java.util.Scanner;

public class Main {
	public static int fibonacci(int x) {
		if (x == 0) return 0;
		if (x == 1 || x == 2) return 1;
		
		int answer = fibonacci(x - 1) + fibonacci(x - 2);
		
		return answer;
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		System.out.println(fibonacci(n));
	}
}
