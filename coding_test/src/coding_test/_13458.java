package coding_test;

import java.io.*;
import java.math.*;

public class _13458 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		long[] member = new long[n];
		String[] str_member = br.readLine().split(" ");
		for(int i = 0; i < n; i++)
			member[i] = Integer.parseInt(str_member[i]);
		String[] b_c = br.readLine().split(" ");
		long b = Integer.parseInt(b_c[0]), c = Integer.parseInt(b_c[1]);
		
		long temp = 0;
		long answer = 0;
		for (long m: member) {
			temp = m - b;
			answer += 1;
			if (temp <= 0)
				continue;
			
			answer += Math.ceil((double) temp / c);
//			System.out.println(answer);
		}
		System.out.println("answer: " + answer);
	}
}
