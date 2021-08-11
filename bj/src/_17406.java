import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _17406 {
    static int N, M, K, result;
    static int[][] origin, map, orders;
    static boolean[] isSelected;
    static int[] order;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        origin = new int[N][M];
        map = new int[N][M];
        orders = new int[K][3];
        order = new int[K];
        isSelected = new boolean[K];
        result = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < M; j++)
                origin[i][j] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i  < K; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            orders[i][0] = Integer.parseInt(st.nextToken());
            orders[i][1] = Integer.parseInt(st.nextToken());
            orders[i][2] = Integer.parseInt(st.nextToken());
        }
        // 1. 순열로 순서 결정하고
        // 2. 결정한 순서대로 turnAround돌리기
        permutation(0);
        System.out.println(result);
    }

    private static void permutation(int cnt) {
        if (cnt == K) {
            turn();
            return;
        }

        for(int i = 0; i < K; i++) {
            if(isSelected[i]) continue;

            order[cnt] = i;
            isSelected[i] = true;
            permutation(cnt + 1);
            isSelected[i] = false;
        }
    }

    private static void turn() {
        for(int i = 0; i < N; i++) {
            for(int j = 0 ; j < M; j++)
                map[i][j] = origin[i][j];
        }
        for(int k: order) {
            int sx = orders[k][0] - orders[k][2] - 1, sy = orders[k][1] - orders[k][2] - 1;
            int tx = orders[k][0] + orders[k][2] - 1, ty = orders[k][1] + orders[k][2] - 1;
            int min = Math.min(tx - sx, ty - sy) / 2;
            for (int i = 0; i < min; i++) {
                turnAround(k, sx + i, sy + i, tx - i, ty - i);
            }
        }

        Min();
    }
    private static void turnAround(int k, int sx, int sy, int tx, int ty) {

        int last = map[sx][sy];

        for (int i = sy + 1; i < ty + 1; i++) {
            int temp = map[sx][i];
            map[sx][i] = last;
            last = temp;
        }
        for (int i = sx + 1; i < tx + 1; i++) {
            int temp = map[i][ty];
            map[i][ty] = last;
            last = temp;
        }

        for (int i = ty - 1; i > sy - 1; i--) {
            int temp = map[tx][i];
            map[tx][i] = last;
            last = temp;
        }
        for (int i = tx - 1; i > sx - 1; i--) {
            int temp = map[i][sy];
            map[i][sy] = last;
            last = temp;
        }
    }
    private static void Min() {
        int answer = 0;
        for(int i = 0; i < N; i++) {
            answer = 0;
            for(int j = 0; j < M; j++) {
                answer += map[i][j];
            }
            result = Math.min(answer, result);
        }
    }
}
