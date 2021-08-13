import java.io.*;
import java.util.*;

public class _17135 {
    static int N, M, D, result;
    static int[][] map, clone;
    static int[] numbers, input;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        numbers = new int[3];
        input = new int[M];
        for (int i = 0; i < M; i++) {
            input[i] = i;
        }
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }

        combination(0, 0);
        System.out.println(result);

    }

    private static void combination(int cnt, int start) {
        if (cnt == 3) {
            clone = new int[N][M];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++)
                    clone[i][j] = map[i][j];
            }

            attackEnemies();
            return;
        }

        for (int i = start; i < M; i++) {
            numbers[cnt] = input[i];
            combination(cnt + 1, i + 1);
        }
    }

    private static void attackEnemies() {
        int count = 0;
        for (int i = N - 1; i >= 0; i--) {
            // 순차적으로 내려옴

            ArrayList<int[]> arr = new ArrayList<>();
            for (int n = 0; n < 3; n++) {
                // 왼쪽부터 궁수가 있으면 적을 찾는다.
                // 공격 가능 범위만큼 거슬러 올라가서 찾는다.

                // 가장 가까운 적과 가장 왼쪽에 있는 적을 찾기 위한 변수 선언
                int a = Integer.MAX_VALUE, x = M, y = M;
                for (int d = 0; d < D && i - d >= 0; d++) {
                    for (int j = 0; j < M; j++) {
                        // 해당 위치에 적이 있고 공격 가능 범위에 들어가면 적을 쏜다.
                        if (clone[i - d][j] == 1 && (d + 1) + Math.abs(j - numbers[n]) <= D && a >= (d + 1) + Math.abs(j - numbers[n])) {
                            // 만약 지금까지 만난 적 중 가장 가까울 경우
                            if(a > (d+1) + Math.abs(j - numbers[n])) {
                                a = (d + 1) + Math.abs(j - numbers[n]);
                                x = i - d;
                                y = j;
                            }
                            // 지금까지 만난 적 중 가장 가까우면서 가장 왼쪽에 있는 적
                            else if (a == (d+1) + Math.abs(j - numbers[n]) && j < y) {
                                x = i - d;
                                y = j;
                            }
                        }
                    }
                }
                if (a != Integer.MAX_VALUE) {
                    arr.add(new int[] {x, y});
                }
            }

            for(int[] a: arr) {
                if (clone[a[0]][a[1]] == 0) continue;

                clone[a[0]][a[1]] = 0;
                count++;
            }
        }
        result = Math.max(result, count);
    }
}
/*
큰 도움을 준 반례들..

2 7 2
0 0 1 0 1 0 1
1 0 1 0 1 0 0
5

4 4 3
0 1 1 0
0 0 1 1
1 0 1 0
1 1 1 0
8

5 5 2
1 0 1 1 1
0 1 1 1 1
1 0 1 0 1
1 1 0 1 0
1 0 1 0 1
14
 */