import java.util.Scanner;

public class _8958 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < T; i++){
            String str = sc.nextLine();
            sb.append(count(str)).append("\n");
        }
        sb.setLength(sb.length() - 1);
        System.out.println(sb.toString());
    }
    private static int count(String str) {
        int count = 0, result = 0;
        for(int i = 0, size = str.length(); i < size; i++) {
            switch(str.charAt(i)) {
                case 'O':
                    count++;
                    break;
                case 'X':
                    count = 0;
                    break;
            }
            result += count;
        }
        return result;
    }
}
