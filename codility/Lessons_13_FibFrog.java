import java.util.*;

public class Lessons_13_FibFrog {
    static Map<Integer, Boolean> F;
    static int size, min;
    static int[] AA;
    public int solution(int[] A) {
        size = A.length;
        int result = 0;
        min = Integer.MAX_VALUE;
        AA = new int[size + 2];
        for(int i = 0; i < size; i++) {
            AA[i + 1] = A[i];
        }
        AA[size + 1] = 1;
        F = makeFibonacci();

        track(0, 0);

        return min;
    }

    public static void track(int start, int jump) {
        if (start == size + 1) {
            if (min > jump) {
                min = jump;
            }
            return;
        }

        for(int i = start; i < size + 2; i++) {
            // no move
            if (start - i == 0) continue;

            if (AA[i] == 1 && F.getOrDefault(i - start, false)) {
                track(i, jump + 1);
            }
        }
    }

    public static Map<Integer, Boolean> makeFibonacci() {
        int[] F = new int[size + 1];
        Map<Integer, Boolean> map = new HashMap<>();
        F[0] = 0;
        F[1] = 1;
        for(int i = 2; i <= size; i++) {
            F[i] = F[i - 1] + F[i - 2];
            map.put(F[i], true);
        }
        return map;
    }
}
