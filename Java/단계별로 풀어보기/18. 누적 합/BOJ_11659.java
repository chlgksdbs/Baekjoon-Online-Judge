package algorithm;

import java.util.Scanner;

public class BOJ_11659 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 수의 개수
		int m = sc.nextInt(); // 합을 구해야 하는 횟수
		int[] numList = new int[n + 1];
		int[] sumList = new int[n + 1]; // 현재 구간까지의 합을 저장하는 배
		int[] answer = new int[m]; // 정답을 저장하는 배열
		
		// 입력
		for (int i = 1; i < n + 1; i++) {
			numList[i] = sc.nextInt();
			sumList[i] = sumList[i - 1] + numList[i];
		}
		for (int i = 0; i < m; i++) {
			int left = sc.nextInt(); // 왼쪽 구간
			int right = sc.nextInt(); // 오른쪽 구간
			
			answer[i] = sumList[right] - sumList[left - 1]; // left번째 수부터 right번째 수까지의 합을 계
		}
		
		for (int i = 0; i < m; i++) {
			System.out.println(answer[i]);
		}
		
	}
}
