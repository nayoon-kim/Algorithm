import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class _1516 {
    static int N;
    static boolean[] built;
    static int[] time;
    static int[][] map;
    static int[] answer;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        time = new int[N + 1];
        built = new boolean[N + 1];
        map = new int[N+1][N+1];
        answer = new int[N + 1];
        Queue<Integer> queue = new LinkedList<>();

        for(int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            time[i] = Integer.parseInt(st.nextToken());
            int index = 0;
            while(true) {
                int t = Integer.parseInt(st.nextToken());
                if (t == -1) break;
                map[i][t] = 2; // i의 만족 조건들
                index++;
            }
            if (index == 0)
                queue.offer(i);
        }

        while(!queue.isEmpty()) {
            int current = queue.poll();

            boolean isWrong = false;
            int temp = 0;
            if (built[current]) continue;
            for(int i = 1; i <= N; i++) {
                if (map[current][i] == 2 && !built[i])
                    isWrong = true;
                else if (map[current][i] == 2 && built[i])
                    temp = temp < answer[i] ? answer[i] : temp;
            }
            if(isWrong)
                continue;
            built[current] = true;
            answer[current] = time[current] + temp;
            for(int i = 1; i <= N; i++) {
                if (map[i][current] == 2) { // current가 지어졌을 경우 고려해볼 수 있는 건물
                    queue.offer(i);
                }
            }
        }

        for(int i = 1; i <= N; i++)
            System.out.println(answer[i]);
    }
}
