import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1987 {
    static int R, C, result;
    static int[][] map;
    static int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
    static boolean[] isSelected;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new int[R][C];
        isSelected = new boolean[26];
        for(int i = 0; i < R; i++) {
            String str = br.readLine();
            for(int j = 0; j < C; j++) {
                map[i][j] = str.charAt(j) - 65;
            }
        }
//        System.out.println(Arrays.deepToString(map));
        check(0, 0, 1);
        System.out.println(result);
    }
    private static void check(int tx, int ty, int cnt) {
        result = result < cnt ? cnt : result;

        isSelected[map[tx][ty]] = true;

        for(int i = 0; i < 4; i++) {
            int x = tx + dr[i], y = ty + dc[i];
            if (x < 0 || x >= R || y < 0 || y >= C) continue;
            if (isSelected[map[x][y]]) continue;
            check(x, y, cnt + 1);
        }
        isSelected[map[tx][ty]] = false;
    }
}