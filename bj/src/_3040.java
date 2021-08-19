import java.util.Scanner;

public class _3040 {
    static int N = 9, S = 7;
    static int[] small;

    public static void main(String[] args) {
        small = new int[N];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < N; i++)
            small[i] = sc.nextInt();

        combination(0, 0, 0);
    }

    private static void combination(int cnt, int start, int flag) {
        if (cnt == S) {
            int answer = 0;

            for(int i = 0; i < N; i++)
                if((flag & 1 << i) != 0) answer += small[i];

            if (answer == 100) {
                for(int i = 0; i < N; i++)
                    if((flag & 1 << i) != 0) System.out.println(small[i]);
            }
            return;
        }

        for(int i = start; i < N; i++)
            combination(cnt + 1, i + 1, (flag | 1<<i));

    }
}
