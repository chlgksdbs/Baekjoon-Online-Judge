import java.util.Scanner;

public class Main {
	public static boolean isPrimeNumber(int x) { // 소수인지 확인하는 함수
		if (x == 1) return false;
		for(int i = 2; i <= (int)Math.sqrt(x); i++) {
			if (x % i == 0) return false;
		}
		
		return true;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int i = 1; i <= T; i++) {
			int n = sc.nextInt();
			int pn = 0;
			
			for (int j = 2; j <= (n / 2); j++) {
				if (isPrimeNumber(j) && isPrimeNumber(n - j)) {
					pn = j;
				}
			}
			
			System.out.println(pn + " " + (n - pn));
		}
	}
}
