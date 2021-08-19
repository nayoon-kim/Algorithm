import java.io.*;
import java.util.StringTokenizer;

public class _3109 {
    static int R, C;
    static int[] dr = {-1, 0, 1}, dc = {1, 1, 1};
    static char[][] map;
    static boolean[][] isVisited;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new char[R][C];
        isVisited = new boolean[R][C];
        for(int i = 0; i < R; i++) {
            String str = br.readLine();
            for(int j = 0; j < C; j++)
                map[i][j] = str.charAt(j);
        }

        int answer = 0;

        for(int i = 0; i < R; i++) {
            answer += pipeline(i, 0);
        }
        System.out.println(answer);
    }

    private static int pipeline(int x, int y) {
        if (y == C - 1) {
            return 1;
        }

        for(int i = 0; i < 3; i++) {
            int dx = x + dr[i], dy = y + dc[i];
            if (dx < 0 || dx >= R || dy < 0 || dy >= C) continue;
            if (map[dx][dy] == '.' && !isVisited[dx][dy]) {
                isVisited[dx][dy] = true;
                int answer = pipeline(dx, dy);
                if (answer == 1) return 1;
            }
        }

       return 0;
    }
}
