import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int k = sc.nextInt();
        
        Integer[] arr = new Integer[n];
        
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        // Arrays.sort() : 자바 정렬 메소드
        // Collections.reverseOrder() : 기본 자바 정렬 메소드는 오름차순으로 정렬함, 따라서 내림차순 정렬을 위해 사용
        // Collections.reverseOrder() 사용 시, int형 사용 불가 => 배열의 자료형을 Integer로 변경
        Arrays.sort(arr, Collections.reverseOrder());
        
        System.out.println(arr[k - 1]);
    }
}
