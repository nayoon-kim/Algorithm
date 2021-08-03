package coding_test;

import java.io.BufferedReader;
//import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.io.OutputStreamWriter;
public class _14889 {
	static int N, R;
	static int[] numbers;
	static int[][] map;
	static int min = Integer.MAX_VALUE;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());
		R = N / 2;
		numbers = new int[R];
		map = new int[N][N];
		for(int i = 0; i < N; i++) {
			String[] temp = br.readLine().split(" ");
			for(int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(temp[j]);
			}
		}
		
		combination(0, 0);
		System.out.println(min);
	}
	
	private static void combination(int cnt, int start) {
		if (cnt == R) {
			int result_1 = 0, result_2 = 0;
			int[] temp = new int[R];
			int a = 0;
			for(int i = 0; i < N; i++) {
				boolean isExists = false;
				for(int j = 0; j < R; j++) {
					if (numbers[j] == i)
						isExists = true;
				}
				if (!isExists)
					temp[a++] = i;
			}
			for(int i = 0; i < numbers.length; i++) {
				for(int j = 0; j < numbers.length; j++) {
					result_1 += map[numbers[i]][numbers[j]];
					result_2 += map[temp[i]][temp[j]];
				}
			}
			int result = Math.abs(result_1 - result_2);
			if (min > result)
				min = result;
			return;
		}
		for(int i = start; i < N; i++) {
			numbers[cnt] = i;
			combination(cnt + 1, i + 1);
		}
	}
}
