import java.util.*;

public class Lessons_13_Ladder {
    public int[] solution(int[] A, int[] B) {
        int size = A.length;
        int[] result = new int[size];

        double[] fib = makeFib();

        for(int i = 0; i < size; i++) {
            result[i] = (int)(fib[A[i]] % Math.pow(2, B[i]));
        }
        return result;
    }

    public static double[] makeFib()
    {
        double[] fb = new double[50001];
        fb[0] = 1.0;
        fb[1] = 1.0;

        for(int i = 2; i < 50001; i++) {
            fb[i] = fb[i - 1] + fb[i - 2];
        }

        return fb;
    }
}
