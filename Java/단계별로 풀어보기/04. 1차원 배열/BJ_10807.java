import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n]; // 크기가 n인 arr 배열 생성

        // 배열의 각 원소의 입력
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int v = sc.nextInt(); // 찾고자 하는 원소
        int vCount = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] == v) {
                vCount++;
            }
        }

        System.out.println(vCount);
    }
}
