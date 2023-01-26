package algorithm;

//import java.util.Arrays;
//import java.util.Collections;
//import java.util.List;
import java.util.Scanner;

public class BJ_2579 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 계단의 개수
		Integer[] stairs = new Integer[n + 1];
		
		stairs[0] = 0;
		for (int i = 1; i <= n; i++) {
			stairs[i] = sc.nextInt();
		}
		
//		// 원본 배열을 List로 변환
//		List<Integer> list = Arrays.asList(stairs);
//		
//		// Collections.reverse() 메소드를 사용하여 list를 거꾸로 변환
//		Collections.reverse(list);
//		
//		// 리스트를 배열로 변환
//		Integer[] reverseStairs = list.toArray(stairs);
		
		int[] dp = new int[n + 1]; // dp 리스트 생성
		for (int i = 0; i <= n; i++) dp[i] = 0; // dp 리스트 초기화
		
		if (n == 1) System.out.println(stairs[1]);
		else if (n == 2) {
			System.out.println(stairs[1] + stairs[2]);
		}
		else { // n이 3이상 자연수인 경우 -> 배열을 뒤집어서 실행 (마지막 계단을 필수 이므로)
			// 기저값 설정
			dp[1] = stairs[1];
			dp[2] = stairs[1] + stairs[2];
			
			for (int i = 3; i <= n; i++) {
				// (1) 현재 인덱스 기준 dp 테이블의 전 값과
				// (2) 현재 인덱스 기준 dp 테이블의 전전 값에 현재 계단의 점수를 더한 값 중 최댓값 저장
				// 내가 생각했던 코드는 아래와 같다.
//				dp[i] = Math.max(dp[i - 1], dp[i - 2] + stairs[i]);
				// dp는 항상 최적의 값을 저장해야 한다. (메모이제이션)
				// 따라서 현재 계단의 값을 더할 수 있는 아래와 같은 비교를 통해 값을 저장하는게 옳다.
				
				dp[i] = Math.max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i];
			}
			
//			// 출력 디버깅
//			for (int i = 0; i <= n; i++) {
//				System.out.print(dp[i] + " ");
//			}
//			System.out.println();
			
			System.out.println(dp[n]);
		}
	}
}
