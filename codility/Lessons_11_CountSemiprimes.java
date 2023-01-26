import java.util.*;

public class Lessons_11_CountSemiprimes {
    public int[] solution(int N, int[] P, int[] Q) {
        int size = P.length;
        int[] result = new int[size];
        boolean[] visited = new boolean[N + 1];
        boolean[] semi_visited = new boolean[N + 1];
        int[] semi = new int[N + 1];

        // make prime numbers
        for(int i = 2; i <= N; i++) {
            if (!visited[i]) {
                for(int j = i + i; j <= N; j += i) {
                    visited[j] = true;
                }
            }
        }

        // make semi prime
        // 2, 3 are prime numbers
        for(int i = 4; i <= N; i++) {
            semi[i] = semi[i - 1];
            if (visited[i]) { // not prime number
                for(int j = 2; j <= Math.sqrt(N); j++) {
                    if (i % j == 0) {
                        if (!visited[j] && !visited[i / j]) { // prime * prime = semi_prime
                            semi[i] += 1;
                            semi_visited[i] = true;
                            break;
                        }
                    }
                }
            }
        }

        // array semi: how many numbers of semi prime number til this element
        // semi[4] = 1, semi[5] = 1, semi[6] = 2, semi[7] = 2, semi[8] = 2, semi[9] = 3, semi[10] = 4
        for(int i = 0; i < size; i++) {
            result[i] = semi[Q[i]] - semi[P[i]];
            if (semi_visited[P[i]]) {
                result[i] += 1;
            }
        }

        return result;
    }
}
