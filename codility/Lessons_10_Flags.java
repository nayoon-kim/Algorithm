import java.util.*;

public class Lessons_10_Flags {

    public int solution(int[] A) {
        List<Integer> peaks = new ArrayList<>();
        Map<Integer, Integer> next_peaks = new HashMap<>();
        int result = 0;

        // if A size less than 3
        if (A.length < 3) {
            return result;
        }

        // check peak
        for(int a = 1, size = A.length; a < size - 1; a++) {
            if (A[a - 1] < A[a] && A[a] > A[a + 1]) {
                peaks.add(a);
            }
        }

        int peak_count = peaks.size();

        // if peak none
        if (peak_count == 0) {
            return result;
        }

        int peak_s = peaks.get(0);
        int peak_e = peaks.get(peak_count - 1);

        // check next peak
        for(int i = 0; i < peak_count - 1; i++) {
            next_peaks.put(peaks.get(i), peaks.get(i + 1));
        }
        next_peaks.put(peak_e, -1);

        // check minimal flags
        double temp_flags = Math.sqrt(peak_e - peak_s);
        int min_flags = (int)temp_flags;
        if (temp_flags > (int)temp_flags || min_flags == 0) {
            min_flags += 1;
        }

        int temp = 0;
        int p = 0;
        for(int i = min_flags; i > 0; i--) {
            temp = 1;
            p = peak_s;
            for(int a: peaks) {
                if (temp == i) { // 3full of flags num
                    break;
                }
                if (next_peaks.get(a) - p >= i) {
                    temp += 1;
                    // System.out.println(next_peaks.get(a) + ", " + p + ", " + i);
                    p = next_peaks.get(a);
                }
            }
            if (result <= temp) {
                result = temp;
            } else {
                break;
            }
            // System.out.println(result);
        }

        return result;
    }
}
