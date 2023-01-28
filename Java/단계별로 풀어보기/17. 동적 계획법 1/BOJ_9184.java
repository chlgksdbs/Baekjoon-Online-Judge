package algorithm;

import java.util.Scanner;

public class BOJ_9184 {
	static int[][][] dp;
	
	public static int w(int[][][] dp, int a, int b, int c) {
		if (dp[a + 50][b + 50][c + 50] != 0) return dp[a + 50][b + 50][c + 50];
		
		// 초기 a, b, c에 대한 조건
		if (a <= 0 || b <= 0 || c <= 0) return 1;
		if (a > 20 || b > 20 || c > 20) return w(dp, 20, 20, 20);
		
		// 함수 실행 부분
		if (a < b && b < c) {
			dp[a + 50][b + 50][c + 50] = w(dp, a, b, c-1) + w(dp, a, b-1, c-1) - w(dp, a, b-1, c);
		}
		else {
			dp[a + 50][b + 50][c + 50] = w(dp, a-1, b, c) + w(dp, a-1, b-1, c) + w(dp, a-1, b, c-1) - w(dp, a-1, b-1, c-1);
		}
		
		return dp[a + 50][b + 50][c + 50];
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		dp = new int[101][101][101]; // 3차원 dp 테이블 생성
		
		while (true) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int z = sc.nextInt();
			
			// 반복문 종료 조건
			if (x == -1 && y == -1 && z == -1) break;
			
			System.out.println("w(" + x + ", " + y + ", " + z + ") = " + w(dp, x, y, z));
			
		}
	}
}
