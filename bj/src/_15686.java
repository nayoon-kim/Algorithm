import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _15686 {
    // N: 도시의 열과 행
    // M: 살아남을 치킨집의 개수
    // C: 현재 남아있는 치킨집의 개수
    // result: 도시의 치킨 거리
    // numbers: 조합의 경우의 수를 저장할 변수, 어떤 치킨 집을 남길 지 결정
    // map: 도시의 정보, 치킨집은 표시하지 않는다.
    // chicken: 치킨집 정보, 최대 13개까지 올 수 있다.
    // clone: 도시의 정보 + 치킨 집이 저장될 변수
    static int N, M, C, result = Integer.MAX_VALUE;
    static int[] numbers;
    static int[][] map, chicken, clone;

    public static void main(String[] args) throws Exception {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        clone = new int[N][N];
        chicken = new int[13][2];
        numbers = new int[M];

        int cnt = 0;
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 2) {
                    // chicken 변수에 치킨 집 정보를 저장한다.
                    chicken[cnt][0] = i;
                    chicken[cnt++][1] = j;
                    // 해당 위치는 빈 공간으로 바꾼다.
                    map[i][j] = 0;
                    C++;
                }
            }
        }

        combination(0, 0);
        System.out.println(result);
    }

    private static void combination(int cnt, int start) {
        if (cnt == M) {
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) 
                    clone[i][j] = map[i][j];
            }
            // 살릴 치킨 집 위치를 clone 변수에 표시한다.
            for(int i = 0; i < M; i++)
                clone[chicken[numbers[i]][0]][chicken[numbers[i]][1]] = 2;

            // 치킨 거리를 구한다.
            chickenStreet();
            return;
        }

        for(int i = start; i < C; i++) {
            numbers[cnt] = i;
            combination(cnt+1, i + 1);
        }
    }

    // 치킨 거리 구하는 메소드
    private static void chickenStreet() {
        int count = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(map[i][j] == 1) {
                    int a = Integer.MAX_VALUE, x = 0, y = 0;
                    for(int k = 0; k < N; k++) {
                        for(int n = 0; n < N; n++) {
                            int result= Math.abs(k - i) + Math.abs(j - n);
                            if (clone[k][n] == 2 && a > result)
                                a = result;
                        }
                    }
                    count += a;
                }
            }
        }
        result = Math.min(result, count);
    }
}
