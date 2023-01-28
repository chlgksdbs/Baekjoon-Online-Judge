package algorithm;

import java.util.Scanner;

public class BOJ_2559 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 온도를 측정한 전체 날짜의 수
		int k = sc.nextInt(); // 합을 구하기 위한 연속적인 날짜의 수
		
		int[] tempDay = new int[n + 1];
		int[] tempSum = new int[n + 1]; // 구간 합을 저장하는 배열
		
		for (int i = 1; i < n + 1; i++) {
			tempDay[i] = sc.nextInt();
			tempSum[i] = tempSum[i - 1] + tempDay[i];
		}
		
		int maxValue = tempSum[k]; // 최대 온도의 합을 저장하는 변수
		
		for (int i = 1; i < n - k + 1; i++) {
			int tempValue = tempSum[i + k] - tempSum[i];
			if (maxValue < tempValue) maxValue = tempValue;
		}
		
		System.out.println(maxValue);
		
	}
}
