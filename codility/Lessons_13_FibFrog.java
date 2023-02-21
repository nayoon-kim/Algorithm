import java.util.*;

public class Lessons_13_FibFrog {
    static int[] fib;
    static boolean[] F;
    static List<Integer> list;
    static int MIN = Integer.MAX_VALUE;
    static int destination;
    public int solution(int[] A) {
        int max = 27;
        fib = new int[max];
        fib[0] = 0;
        fib[1] = 1;
        fib[2] = 1;
        F = new boolean[200000];
        F[0] = true;
        F[1] = true;

        for(int i = 3; i < max; i++) {
            fib[i] = fib[i-1] + fib[i-2];
            F[fib[i]] = true;
        }

        list = new ArrayList<>();
        for(int i = 0, size = A.length; i < size; i++) {
            if (A[i] == 1)
                list.add(i + 1);
        }
        list.add(A.length + 1);
        destination = A.length + 1;
        for(int i = 0, size = list.size(); i < size; i++) {
            if (F[list.get(i)]) {
                findMin(i, 1);
            }
        }

        return MIN;
    }

    public static void findMin(int index, int count)
    {
        if (list.size() - 1 <= index) {
            MIN = count < MIN ? count : MIN;
            return;
        }

        for(int i = index + 1, size = list.size(); i < size; i++) {
            if (F[list.get(i) - list.get(index)]) {
                findMin(i, count + 1);
            }
        }
    }
}
