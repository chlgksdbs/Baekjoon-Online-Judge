package baekjoon;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ_9506 {
	
	static StringBuilder sb;
	
	// 해당 수가 약수들의 합으로 표현이 가능한 지 체크하는 함수
	public static void isPossible(int n) {
		
		List<Integer> divisor = new ArrayList<>(); // n의 약수들의 리스트
		int sum = 0; // 약수들의 합을 체크
		
		for (int i = 1; i < n; i++) {
			// i가 n의 약수인 경우, List에 저장
			if (n % i == 0) {
				divisor.add(i);
				sum += i;
			}
		}
		
		// n이 완전 수인 경우
		if (sum == n) {
			sb.append(n + " = ");
			for (int i = 0; i < divisor.size(); i++) {
				sb.append(divisor.get(i) + " + ");
			}
			sb.delete(sb.length() - 2, sb.length());
			sb.append("\n");
		}
		// n이 완전 수가 아닌 경우
		else {
			sb.append(n + " is NOT perfect." + "\n");
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		sb = new StringBuilder();
		
		while (true) {
			int n = sc.nextInt();
			
			if (n == -1) break; // 종료 조건
			
			isPossible(n); // 약수 체크 및 출력 대기
		}
		
		System.out.println(sb);
	}
}
