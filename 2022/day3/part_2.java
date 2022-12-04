import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private static final Integer ENABLE_DEBUG = 0;
    private static final String DEBUG = "src/test.txt";
    private static final String INPUT = "src/input.txt";

    public static void main(String[] args) {
        List<String> lines = new ArrayList<>();

        try (FileReader fr= new FileReader(ENABLE_DEBUG == 1 ? DEBUG : INPUT))
        {
            BufferedReader br = new BufferedReader(fr);
            String line;
            int sum = 0;
            int res = 0;
            Set<Character> cc = new HashSet<>();
            while((line=br.readLine())!=null) {
                if (!line.isEmpty()) {
                    lines.add(line);
                    sum++;
                }
                if (sum == 3) {
                    List<Character> ff = new ArrayList<>();
                    for (char c : lines.get(0).toCharArray()) {
                        ff.add(c);
                    }
                    for (int i = 1; i < lines.size(); i++) {
                        List<Character> tmo = new ArrayList<>();
                        for (char c : lines.get(i).toCharArray()) {
                            tmo.add(c);
                        }
                        ff.retainAll(tmo);
                    }
                    System.out.println(ff);
                    sum = 0;
                    res += getPos(ff.get(0));
                    lines = new ArrayList<>();
                }
            }
            System.out.println(res);
        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }

    private static int getPos(char c) {
        if (Character.isUpperCase(c)) {
            int temp = (int)c;
            int temp_integer = 64; //for upper case
            if(temp<=90 & temp>=65)
                return 26 + temp-temp_integer;
        }
        int temp = (int)c;
        int temp_integer = 96; //for lower case
        if(temp<=122 & temp>=97)
            return temp-temp_integer;
        return -1;
    }

}