package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ_1931 {
	
	static int N; // 회의의 수
	static int ans; // 최대 사용할 수 있는 회의의 수
	
	static class Pair implements Comparable<Pair> {
		int startTime;
		int endTime;
		
		public Pair(int startTime, int endTime) {
			this.startTime = startTime;
			this.endTime = endTime;
		}
		
		@Override
		public int compareTo(Pair o) {
			// TODO Auto-generated method stub
			// 종료 시각을 기준으로 오름차순 정렬
			return endTime != o.endTime ? endTime - o.endTime : startTime - o.startTime;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		Pair[] p = new Pair[N];
		
		for (int i = 0; i < N; i++) {
			p[i] = new Pair(sc.nextInt(), sc.nextInt());
		}
		
		Arrays.sort(p); // 종료 시각을 기준으로 오름차순 정렬 수행
		
		int nowTime = 0; // 회의 종료 시간 (다음 회의 시작의 최소 시작 시간)
		for (int i = 0; i < N; i++) {
			if (nowTime <= p[i].startTime) {
				nowTime = p[i].endTime;
				ans++;
			}
		}
		
		System.out.println(ans);
	}
}
