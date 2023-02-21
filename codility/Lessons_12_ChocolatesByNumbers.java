import java.util.*;

public class Lessons_12_ChocolatesByNumbers {
    public int solution(int N, int M) {
        int temp = 0;
        List<Integer> list = new ArrayList<>();
        while(true) {
            list.add(temp % N);
            temp += M;
            if (temp % N == 0) {
                break;
            }
        }
        int result = list.size();
        return result;
    }
}
