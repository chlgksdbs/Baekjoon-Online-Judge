package baekjoon;

import java.util.Scanner;

public class BOJ_1717 {
	
	static int N, M; // 집합의 크기, 연산의 개수
	
	static int[] disjoint;
	
	// 매개변수로 주어진 입력에 대해서 대표자를 찾는 함수
	public static int findSet(int n) {
		
		// 자기 자신이 대표자인 경우, 그대로 리턴
		if (disjoint[n] == n) return n;
		// 자기 자신이 대표자가 아닌 경우, 대표자를 찾아 자신의 인덱스에 위치한 배열에 저장한 뒤 그 값을 리턴
		else return disjoint[n] = findSet(disjoint[n]);
	}
	
	// n2를 n1이 속한 집합으로 합병하는 작업을 수행하는 함수
	public static void union(int n1, int n2) {
		
		// 두 원소가 대표자가 아닐수도 있으니, 우선적으로 각 집합이 속한 대표자 찾기
		int a = findSet(n1);
		int b = findSet(n2);
		
		disjoint[b] = a; // 합집합 수행
	}
	
	// 서로소 집합을 만드는 함수 (초기 세팅)
	public static void makeSet() {
		
		disjoint = new int[N + 1];
		
		// 각 원소의 대표자는 자기 자신으로 세팅
		for (int i = 0; i <= N; i++) {
			disjoint[i] = i;
		}
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		N = sc.nextInt();
		M = sc.nextInt();
		
		makeSet();
		
		for (int i = 0; i < M; i++) {
			int num = sc.nextInt(); // 연산의 종류 (0 : union, 1 : find-set)
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			// 합집합 연산 수행
			if (num == 0) {
				union(a, b);
			}
			// 두 원소가 같은 집합에 포함되어 있는지 체크
			else if (num == 1) {
				// 대표자가 같은 경우, 두 원소는 같은 집합
				if (findSet(a) == findSet(b)) sb.append("YES" + "\n");
				// 대표자가 다른 경우, 두 원소는 다른 집합
				else sb.append("NO" + "\n");
			}
		}
		
		System.out.println(sb);
	}
}
