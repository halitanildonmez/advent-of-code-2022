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
            while((line=br.readLine())!=null) {
                if (!line.isEmpty()) {
                    int mid = line.length() % 2 == 0 ? line.length() / 2 : line.length() / 2 - 1;
                    String first = line.substring(0, mid);
                    String second = line.substring(mid);
                    //System.out.println(first + " " + second);

                    Set<String> c1 = new HashSet<>();
                    Set<String> c2 = new HashSet<>();
                    for (char c : first.toCharArray()) {
                        c1.add(c + "");
                    }
                    for (char c : second.toCharArray()) {
                        c2.add(c + "");
                    }
                    List<String> collect = c1.stream().filter(c2::contains).toList();
                    List<String> collect1 = c2.stream().filter(c1::contains).toList();
                    //System.out.println(collect);
                    //System.out.println(collect1);

                    char c =  collect1.get(0).charAt(0) ;
                    int pos = getPos(c);
                    //System.out.println(c + " " + pos);
                    sum += pos;

                }
            }
            System.out.println(sum);
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