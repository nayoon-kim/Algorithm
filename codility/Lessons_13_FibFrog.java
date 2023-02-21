import java.util.*;

class Point {
    public int pos;
    public int count;
    public Point(int pos, int count) {
        this.pos = pos;
        this.count = count;
    }
    public String toString()
    {
        return "pos: " + this.pos + ", count: " + this.count;
    }
}
public class Lessons_13_FibFrog {
    Queue<Point> queue;
    static int[] fib;
    static boolean[] F;
    static List<Integer> list;
    static int MIN = -1;
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
        list.add(0);
        for(int i = 0, size = A.length; i < size; i++) {
            if (A[i] == 1)
                list.add(i + 1);
        }
        list.add(A.length + 1);
        destination = A.length + 1;
        queue = new LinkedList<>();
        queue.add(new Point(0, 0));

        while(!queue.isEmpty()) {
            Point temp = queue.poll();

            if (list.size() - 1 == temp.pos) {
                MIN = temp.count;
                break;
            }
            for(int i = list.size() - 1; i > temp.pos; i--) {
                if (F[list.get(i) - list.get(temp.pos)])
                    queue.add(new Point(i, temp.count + 1));
            }
        }

        return MIN;
    }
}
