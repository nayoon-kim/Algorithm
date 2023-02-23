import java.util.*;

public class Lessons_13_FibFrog {
    public int solution(int[] A) {
        int[] aA = new int[A.length + 2];
        aA[0] = 0;
        aA[A.length + 1] = 1;
        for(int i = 0; i < A.length; i++) {
            aA[i + 1] = A[i];
        }

        int max = 27;
        int[] fib = new int[max];
        fib[0] = 0;
        fib[1] = 1;
        fib[2] = 1;
        for(int i = 2; i < max; i++)
        {
            fib[i] = fib[i - 1] + fib[i - 2];
        }

        int AMaxSize = A.length + 1;
        boolean[] visited = new boolean[AMaxSize];

        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(0, 0));

        while(!queue.isEmpty()) {
            Point point = queue.poll();

            for(int i = 2; i < max; i++) {
                int temp = point.x + fib[i];
                if (temp == A.length + 1) {
                    return point.y + 1;
                } else {
                    if (temp < A.length + 1 && aA[temp] == 1 && !visited[temp]) {
                        visited[temp] = true;
                        queue.add(new Point(temp, point.y + 1));
                    }
                }
            }
        }
        return -1;
    }

    class Point {
        public int x;
        public int y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public String toString() {
            return "[x: " + x + ", y: " + y + "]";
        }
    }
}
