import java.util.Scanner;

public class _3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean[] rest = new boolean[42];
        int count = 0;
        for(int i = 0; i < 10; i++) {
            int t = sc.nextInt() % 42;

            if (rest[t]) continue;
            rest[t] = true;
            count++;
        }
        System.out.println(count);
    }
}
