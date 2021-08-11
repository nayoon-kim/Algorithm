import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _16926 {
    static int N, M, R;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < M; j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }

        int min = Math.min(N, M) / 2;

        for(int i = 0; i < min; i++)
            turnAround(i);

        printMap();
    }

    private static void turnAround(int x) {
        int j = N - x - 1;
        int k = M - x - 1;
        for (int n = 0; n < R; n++) {
            int last = map[x][x];

            for (int i = x + 1; i < N - x; i++) {
                int temp = map[i][x];
                map[i][x] = last;
                last = temp;
            }
            for (int i = x + 1; i < M - x; i++) {
                int temp = map[j][i];
                map[j][i] = last;
                last = temp;
            }

            for (int i = j - 1; i > x - 1; i--) {
                int temp = map[i][k];
                map[i][k] = last;
                last = temp;
            }
            for (int i = k - 1; i > x - 1; i--) {
                int temp = map[x][i];
                map[x][i] = last;
                last = temp;
            }
        }
    }

    private static void printMap() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                sb.append(map[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}
