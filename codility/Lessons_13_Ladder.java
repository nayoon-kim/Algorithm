import java.util.*;

public class Lessons_13_Ladder {
    public int[] solution(int[] A, int[] B) {
        Queue<Integer> queue = new LinkedList<>();
        int size = A.length;
        int[] result = new int[size];

        for(int i = 0; i < size; i++) {
            queue = new LinkedList<>();
            queue.add(0);
            int r = 0;
            while(!queue.isEmpty()) {
                int temp = queue.poll();

                for(int j = 1; j < 3; j++) {
                    if (temp + j == A[i]) {
                        r += 1;
                    } else if (temp + j < A[i]) {
                        queue.add(temp + j);
                    }
                }
            }
            result[i] = r % (int)Math.pow(2, B[i]);
        }

        return result;
    }
}
