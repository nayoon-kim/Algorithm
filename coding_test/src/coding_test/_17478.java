package coding_test;

import java.io.*;

public class _17478 {
	static String msg = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n";
	static String[] chatbot = {"\"재귀함수가 뭔가요?\"\n",
			"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n",
			"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n",
			"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n",
			"라고 답변하였지.\n"};
	static String answer = "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n";
	static int num;
	static BufferedReader br;
	static BufferedWriter bw;
	
	public static void recursion(int count) throws IOException {
		
		if (count == -1)
			return;
		StringBuilder prefix = new StringBuilder();
		for(int i = 0; i < num - count; i++)
			prefix.append("____");
		String str_prefix = prefix.toString();
		if (count == 0) {
			bw.write(str_prefix+chatbot[0]);
			bw.write(str_prefix+answer);
		} else {
			for(int i = 0, size = chatbot.length - 1; i < size; i++) {
				bw.write(str_prefix+chatbot[i]);
			}	
		}
		recursion(count-1);
		bw.write(str_prefix + chatbot[chatbot.length - 1]);
		
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		//		Scanner sc = new Scanner(System.in);
		num = Integer.parseInt(br.readLine());
		bw.write(msg);
		recursion(num);
		bw.close();
	}
}
