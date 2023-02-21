public class Lessons_12_CommonPrimeDivisors {
    public int solution(int[] A, int[] B) {
        int result = 0;
        for(int i = 0, size = A.length; i < size; i++) {
            int gcd = gcd(A[i], B[i]);

            if (A[i] == B[i]) {
                result++;
                continue;
            }
            if (gcd == 1) {
                continue;
            }

            int a = A[i];
            boolean gcd_a_flag = false;
            while(a != 1)
            {
                int gcd_a = gcd(a, gcd);
                if (gcd_a == 1) {
                    gcd_a_flag = true;
                    break;
                }
                a /= gcd_a;
            }

            if (gcd_a_flag) {
                continue;
            }

            int b = B[i];
            boolean gcd_b_flag = false;
            while(b != 1)
            {
                int gcd_b = gcd(b, gcd);
                if (gcd_b == 1) {
                    gcd_b_flag = true;
                    break;
                }
                b /= gcd_b;
            }

            if (gcd_b_flag) {
                continue;
            }

            result++;
        }
        return result;
    }

    public static int gcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        int gcd = 0;
        while(true)
        {
            if (a % b == 0) {
                gcd = b;
                break;
            }
            int temp = a;
            a = b;
            b = temp % b;
        }
        return gcd;
    }
}
