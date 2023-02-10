package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class BOJ_11478 {
	
	static String str; // 문제에서 주어진 문자열
	static int strSize; // 문자열의 길이
	static int totalCnt = 0; // 서로 다른 부분 문자열의 개수
	
	// 부분 문자열을 구하는 함수
	// size : 부분 문자열의 길이
	public static void subSentence(int size) {
		Set<String> strSet = new HashSet<>();
		
		for (int i = 0; i <= strSize - size; i++) {
			 
			String tempStr = str.substring(i, i + size); // 임시로 저장할 부분 문자열
			
			// 해당 문자열이 포함되어있지 않은 경우에는 포함시키고 count 값 증가
			if (!strSet.contains(tempStr)) {
				strSet.add(tempStr);
				totalCnt++;
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		str = br.readLine(); // 문자열 입력
		
		strSize = str.length();
		// 부분 문자열의 길이는 1부터 str의 길이까지 수행 가능
		for (int i = 1; i <= strSize; i++) {
			subSentence(i);
		}
		
		System.out.println(totalCnt);
	}
}
