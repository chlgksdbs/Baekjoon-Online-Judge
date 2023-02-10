package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_1620 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(st.nextToken()); // 도감에 수록되어 있는 포켓몬의 개수
		int m = Integer.parseInt(st.nextToken()); // 내가 맞춰야 하는 문제의 개수
		
		Map<String, Integer> pokemon = new HashMap<String, Integer>();
		String[] pokemonName = new String[n + 1];
		
		// 입력 부분
		for (int i = 1; i <= n; i++) {
			String inputStr = br.readLine();
			pokemon.put(inputStr, i); // (1) HashMap에 값을 추가 (입력)
			pokemonName[i] = inputStr; // (2) String 배열에 값을 추가 (입력)
		}
		
		for (int i = 0; i < m; i++) {
			String temp = br.readLine(); // 입력
			if (pokemon.containsKey(temp)) {
				sb.append(pokemon.get(temp) + "\n");
			}
			else {
//				// 모든 키를 순회 -> but, 해당 코드 시간 초과 발생!
//				// 키와 매핑된 값이랑  equals() 메서드에 전달된 값이랑 일치하면 반복문 종료
//				for (String key : pokemon.keySet()) {
//					// 키가 null 이면 NullPointerException 예외 발생
//					if (pokemon.get(key).equals(Integer.parseInt(temp))) {
//						sb.append(key + "\n");
//						break;
//					}
//				}
				// 위 코드는 O(n x m)의 시간 복잡도를 가져서 시간 초과 발생
				// 아래의 코드는 입력 시에 저장한 배열의 인덱스를 찾는 탐색만 수행
				// 따라서 O(n)의 시간 복잡도를 가져서 정상 수행
				sb.append(pokemonName[Integer.parseInt(temp)] + "\n");
			}
		}
		
		System.out.print(sb);
	}
}
