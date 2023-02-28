import java.util.*;

public class Lessons_13_Ladder {
    public int[] solution(int[] A, int[] B) {
        int size = A.length;
        int[] result = new int[size];


        for(int i = 0; i < size; i++) {
            int fib = makeFib(A[i], B[i]);
            result[i] = fib;
        }
        return result;
    }

    public static int makeFib(int a, int b)
    {
        int modulo = (int)Math.pow(2, b);
        int t1 = 1;
        int t2 = 1;
        for(int i = 2; i <= a; i++) {
            int t3 = (t1 + t2) % modulo;
            t1 = t2;
            t2 = t3;
        }

        return t2;
    }
}
