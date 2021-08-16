import java.util.Scanner;

public class _1592 {
    static int N, M, L;
    static int[] people;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        L = sc.nextInt();

        people = new int[N];
        int cnt = 0, result = 0;

        while(true){
            // 홀수일 경우
            people[cnt]++;
            if (people[cnt] == M) break;
            if (people[cnt] % 2 == 1)
                // 0일 경우 시계 방향으로 두 번째 -> 2
                // 0일 경우 시계 방향으로 네 번째 -> 4 (0 + 4) % 5
                // 1일 경우 시계 방향으로 네 번째 -> 0 (1 + 5) % 5
                // 2일 경우 시계 방향으로 네 번째 -> 3, 4, 0, 1 (2 + 4) % 5
                cnt = (cnt + L) % N;
            else
                // 0일 경우 반시계 방향으로 두 번째 -> 3 (5 - 2 = 3) 1, 2, 3
                // 0일 경우 반시계 방향으로 세 번째 -> 2 (5 - 3 = 2) 1, 2
                // 1일 경우 반시계 방향으로 네 번째 -> 0, 4, 3, 2 -> (5 - 4 = 1 + 1)  2
                // 2일 경우 반시계 방향으로 네 번째 -> (5 - 4 = 1 + 2) 3 -> 1, 0, 4, 3
                cnt = (cnt + (N - L)) % N;
            result++;
        }
        System.out.println(result);
    }
}
