// !: My original solution is @ "./B_Squares_and_Cubes.py".. I may or may not have used generative AI to translate it to Java haha.....
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int sqrtN = (int) Math.floor(Math.sqrt(n));
            int cbrtN = (int) Math.floor(Math.cbrt(n));
            int cbrtSqrtN = (int) Math.floor(Math.cbrt(Math.sqrt(n)));
            int result = sqrtN + cbrtN - cbrtSqrtN;
            System.out.println(result);
        }

        scanner.close();
    }
}
