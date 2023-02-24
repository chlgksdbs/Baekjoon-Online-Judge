package baekjoon;

import java.util.Scanner;

public class BOJ_2630 {
	
	static int N; // 종이 한 변의 길이 (2^1 ~ 2^7)
	static int whiteCount;
	static int blueCount;
	
	static int[][] map; // 색종이
	
	/**
	 * 
	 * @param r : 시작 열의 위치
	 * @param c : 시작 행의 위치
	 * @param size : 현재 잘려진 색종이의 한 변의 길이
	 */
	public static void cut(int r, int c, int size) {
		
		// 기저 조건 : 더 이상 자를 수 없는 경우 갯수를 count 하고 함수 종료
		if (size == 1) {
			if (map[r][c] == 0) whiteCount++;
			else blueCount++;
			
			return;
		}
		
		int wCnt = 0;
		int bCnt = 0;
		
		// 현재 잘려진 색종이를 체크
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				if (map[i][j] == 0) wCnt++;
				else bCnt++;
			}
		}
		
		// 색종이가 하나의 색으로 칠해져 있는 경우, 그것의 count를 증가시키고 함수 종료
		if (wCnt == 0) {
			blueCount++;
			return;
		}
		else if (bCnt == 0) {
			whiteCount++;
			return;
		}
		
		int half = size / 2; // 한 변의 길이를 2로 나눔 (색종이를 1/4 등분)
		
		// 쿼드 트리 형성
		cut(r, c, half);
		cut(r, c + half, half);
		cut(r + half, c, half);
		cut(r + half, c + half, half);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		
		map = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = sc.nextInt();
			}
		} // 입력 종료
		
		cut(0, 0, N);
		
		System.out.println(whiteCount);
		System.out.println(blueCount);
	}
}
