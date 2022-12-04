import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Main {
/*
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
* shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
* */
    private static final Integer ENABLE_DEBUG = 0;
    private static final String DEBUG = "src/test.txt";
    private static final String INPUT = "src/input.txt";

    public static void main(String[] args) {
        List<String> lines = new ArrayList<>();
        int score = 0;

        try (FileReader fr= new FileReader(ENABLE_DEBUG == 1 ? DEBUG : INPUT))
        {
            BufferedReader br = new BufferedReader(fr);
            String line;
            int t = 0;
            while((line=br.readLine())!=null) {
                if (!line.isEmpty()) {
                    String []s = line.split(" ");
                    String their = s[0];
                    String mine = s[1];
                    score += newOutcome(their, mine);
                    //System.out.print(their + " " + mine + " " + score);

                    score += getShape(their, mine);
                    //System.out.println( " " + score);
                }
            }
        }
        catch(IOException e) {
            e.printStackTrace();
        }
        System.out.println(score);
    }

    private static int getShape(String t, String m) {
        /// 1 for Rock, 2 for Paper, and 3 for Scissors
        // A for Rock, B for Paper, and C for Scissors
        // X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
        if (Objects.equals(m, "Y")) {
            if (Objects.equals(t, "A"))
                return 1;
            if (Objects.equals(t, "B"))
                return 2;
            return 3;
        } else if (Objects.equals(m, "X")) {
            if (Objects.equals(t, "A"))
                return 3;
            if (Objects.equals(t, "B")) {
                return 1;
            }
            return 2;
        } else {
            if (Objects.equals(t, "A"))
                return 2;
            if (Objects.equals(t, "B"))
                return 3;
            return 1;
        }
    }

    private static int newOutcome(String t, String m) {
        // X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
        if (Objects.equals(m, "X"))
            return 0;
        if (Objects.equals(m, "Y"))
            return 3;
        return 6;
    }

    private static int outcome(String t, String m) {
        if ((t.equals("A") && m.equals("X")) ||
                (t.equals("B") && m.equals("Y")) ||
                (t.equals("C") && m.equals("Z"))) {
            return 3;
        }
        if (m.equals("X") && t.equals("B")) {
            return 0;
        }
        if (m.equals("Y") && t.equals("C")) {
            return 0;
        }
        if (m.equals("Z") && t.equals("A")) {
            return 0;
        }
        return 6;
    }
}