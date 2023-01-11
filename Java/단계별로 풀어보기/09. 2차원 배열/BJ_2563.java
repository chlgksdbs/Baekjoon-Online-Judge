import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int total = 0;
		int n = sc.nextInt();
		int[][] paper = new int[100][100];
		
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				paper[i][j] = 0;
			}
		}
		
		for (int i = 0; i < n; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			for (int j = 0; j < 10; j++) {
				for (int k = 0; k < 10; k++) {
					paper[y + j][x + k] = 1; // 색칠하기
				}
			}
		}
		
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (paper[i][j] == 1) total++;
			}
		}
		
		System.out.println(total);
		
	}
}
