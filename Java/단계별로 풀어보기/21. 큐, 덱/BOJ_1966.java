package baekjoon.algorithm;

import java.awt.Point;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_1966 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt(); // 문서의 개수
			int M = sc.nextInt(); // 몇 번째로 인쇄되었는지 궁금한 문서
			
			Queue<Point> queue = new LinkedList<>();
			int[] maxNum = new int[N]; // 입력된 값의 오름차순 정렬
			int idx = N - 1; // maxNum을 가리키는 인덱스
			
			for (int i = 0; i < N; i++) {
				int tmp = sc.nextInt();
				maxNum[i] = tmp;
				queue.add(new Point(i, tmp)); // queue에 인덱스에 대한 정보와 값을 입력
			}
			
			Arrays.sort(maxNum); // 오름차순 정렬
			
			int cnt = 0; // 몇 번째로 출력되는지에 대한 정보
			
			while (true) {
				// 현재 가장 큰 값이 queue의 front에 있는 경우
				if (maxNum[idx] == queue.peek().y) {
					// 해당 값이 찾는 값인 경우 반복문 종료
					if (M == queue.peek().x) {
						cnt++;
						break;
					}
					// 해당 값이 찾는 값이 아닌 경우 poll, idx 값 감소, cnt 값 증가
					queue.poll();
					idx--;
					cnt++;
				}
				else {
					queue.add(queue.poll());
				}
			}
			
			System.out.println(cnt);
		}
	}
}
