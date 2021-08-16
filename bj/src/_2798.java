import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2798 {
    static int N, M, R = 3, answer;
    static int[] card, numbers;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        card = new int[N];
        numbers = new int[3];

        st = new StringTokenizer(br.readLine(), " ");
        for(int n = 0; n < N; n++ )
            card[n] = Integer.parseInt(st.nextToken());

        combination(0, 0);
        System.out.println(answer);
    }

    private static void combination(int cnt, int start) {
        if (cnt == R) {
            int result = 0;
            for(int i = 0; i < R; i++)
                result += card[numbers[i]];
            answer = result <= M && result > answer ? result : answer;
            return;
        }

        for(int i = start; i < N; i++) {
            numbers[cnt] = i;
            combination(cnt + 1, i + 1);
        }

    }
}
