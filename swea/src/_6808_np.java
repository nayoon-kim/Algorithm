import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Scanner;


public class _6808_np {
    static int N = 9;
    static int[] g, y;
    static boolean[] isG;
    static int win, lose;
    static int[] numbers;

    public static void main(String[] args) throws Exception {
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
            Arrays.sort(y);

            do {
                int gnum = 0, ynum = 0, temp = 0;
                for(int i = 0; i < N;i++) {
                    temp = g[i] + y[i];
                    if (g[i] > y[i])
                        gnum += temp;
                    else if (g[i] < y[i])
                        ynum += temp;
                }
                if(gnum > ynum) win++;
                else if(ynum > gnum) lose++;
            } while(np(y));
            System.out.println("#"+test_case+" " + win + " " + lose);
        }
    }

    private static boolean np(int[] n) {
        int N = n.length;

        // step1. 뒤쪽부터 탐색을 시작한다. 꼭대기를 찾는다.
        int i = N - 1;
        while(i > 0 && n[i-1]>= n[i]) --i;

        if(i == 0) return false;

        // step2. 교환할 i - 1을 구한다.
        int j = N - 1;
        while(n[i - 1] >= n[j]) --j;

        // step3. 교환
        swap(n, i - 1, j);

        // step4. 내림차순으로 정렬된 꼭대기부터 뒤쪽을 오름차순으로 정렬
        int k = N - 1;
        while(i < k) {
            swap(n, i++, k--);
        }
        return true;
    }

    private static void swap(int[] num, int i, int j) {
        int temp = num[i];
        num[i] = num[j];
        num[j] = temp;
    }
}
