import java.util.*;

public class Lessons_13_Ladder {
    public int[] solution(int[] A, int[] B) {
        int size = A.length;
        int[] result = new int[size];
        boolean[] visited = new boolean[31];
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < size; i++) {
            if (map.get(B[i]) == null) {
                map.put(B[i], A[i]);
            } else {
                if (map.get(B[i]) < A[i]) {
                    map.put(B[i], A[i]);
                }
            }
        }
        for(int i = 0; i < size; i++) {
            if (visited[B[i]]) continue;
            visited[B[i]] = true;
            int[] fib = makeFib(map.get(B[i]), B[i]);

            for(int j = 0; j < size; j++) {
                if (B[i] != B[j]) continue;
                result[j] = fib[A[j]];
            }
        }
        return result;
    }

    public static int[] makeFib(int a, int b)
    {
        int modulo = (int)Math.pow(2, b);
        int[] fb = new int[a + 1];
        fb[0] = 1;
        fb[1] = 1;
        for(int i = 2; i <= a; i++) {
            fb[i] = (fb[i - 1] + fb[i - 2]) % modulo;
        }

        return fb;
    }
}
