import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 전체 사람의 수
		int[][] info = new int[n][2];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 2; j++) {
				info[i][j] = sc.nextInt();
			}
		}
		
		for (int i = 0; i < n; i++) {
			int rank = 1; // 등수
			for (int j = 0; j < n; j++) {
				if (i == j) continue; // 자신은 확인 제외
				if (info[i][0] < info[j][0] && info[i][1] < info[j][1]) rank++;
			}
			System.out.print(rank + " ");
		}
	}
}
