import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class _6808 {
    static int N = 9;
    static int[] g, y;
    static boolean[] isG;
    static int win, lose;
    static int[] numbers;

    private static void permutation(int cnt, int flag) {
        if (cnt == N) {
            int gnum = 0, ynum = 0, temp = 0;
            for(int i = 0; i < N;i++) {
                temp = g[i] + numbers[i];
                if (g[i] > numbers[i])
                    gnum += temp;
                else if (g[i] < numbers[i])
                    ynum += temp;
            }
            if(gnum > ynum) win++;
            else if(ynum > gnum) lose++;
            return;
        }
        for(int i = 0; i < N; i++) {
            if((flag & (1<<i)) != 0) continue;

            numbers[cnt] = y[i];
            permutation(cnt+1, (flag | 1<<i));
        }
    }
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("res/s_input.txt"));
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++) {

            isG = new boolean[19];
            g = new int[9];
            y = new int[9];
            numbers = new int[9];
            win = 0;
            lose = 0;

            for(int i = 0; i < 9; i++){
                g[i] = sc.nextInt();
                isG[g[i]] = true;
            }
            int cnt = 0;
            for(int i = 1; i <= 18; i++) {
                if(isG[i]) continue;
                y[cnt++] = i;
            }

            permutation(0, 0);
            System.out.println("#"+test_case+" " + win + " " + lose);
        }
    }
}
