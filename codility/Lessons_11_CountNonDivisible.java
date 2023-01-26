import java.util.*;

public class Lessons_11_CountNonDivisible {
    public int[] solution(int[] A) {
        int size = A.length;
        int[] result = new int[size];

        // make prime number
        int MAX = 100000; // input range 1 ~ 100,000
        boolean[] visited = new boolean[MAX + 1];

        // use 'sieve of Eratosthenes'
        for(int i = 2; i <= MAX; i++) {
            if (!visited[i]) {
                for(int j = i + i; j <= MAX; j += i) {
                    visited[j] = true;
                }
            }
        }

        // count number of each element in array
        Map<Integer, Integer> map = new HashMap<>();
        for(int a: A) {
            int temp = map.getOrDefault(a, 0);
            map.put(a, temp + 1);
        }

        int a = 0;
        for(int i = 0; i < size; i++) {
            a = A[i];
            if (a == 1) {
                result[i] = size - map.get(1);
            }
            else if (!visited[a]) { // if prime number
                result[i] = size - map.get(a) - map.getOrDefault(1, 0);
            }
            else { // if not prime number
                result[i] = size;
                for(int j = 1; j <= Math.sqrt(a); j++) { // use 'lesson 10'
                    if (a % j == 0) {
                        if (a / j != j) {
                            result[i] -= map.getOrDefault(a / j, 0);
                        }
                        result[i] -= map.getOrDefault(j, 0);
                    }
                }
            }
        }

        return result;
    }
}
