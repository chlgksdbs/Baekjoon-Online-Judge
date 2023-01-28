package algorithm;

import java.util.Scanner;

public class BOJ_1912 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 수의 개수
		int[] arr = new int[n + 1]; // n개의 수를 입력받는 배열
		
		for (int i = 1; i < n + 1; i++) {
			arr[i] = sc.nextInt();
		}
		
		int[] dp = new int[n + 1]; // dp 테이블 생성
		
		dp[1] = arr[1]; // 기저값 설정
		int maxValue = dp[1]; // 최댓값을 저장하는 변수
		
		for (int i = 2; i < n + 1; i++) {
			// idea : 현재 지점에서의 최댓값을 갱신
			// (1) 이전까지의 dp 값 + 현재 arr 
			// (2) 현재 arr 값 중 최댓값인 경우로 dp 테이블에 저장
			
			dp[i] = Math.max(dp[i - 1] + arr[i], arr[i]);
			maxValue = Math.max(maxValue, dp[i]); // 최댓값 갱신
		}
		
		System.out.println(maxValue);
		
	}
}
