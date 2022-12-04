import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Main {

    private static final Integer ENABLE_DEBUG = 0;
    private static final String DEBUG = "src/test.txt";
    private static final String INPUT = "src/input.txt";

    public static void main(String[] args) {
        Map<Integer, List<String>> calorieMap = new HashMap<>();
        Map<Integer, Integer> calorieMap2 = new HashMap<>();
        List<String> lines = new ArrayList<>();
        int sum = Integer.MIN_VALUE;

        try (FileReader fr= new FileReader(ENABLE_DEBUG == 1 ? DEBUG : INPUT))
        {
            BufferedReader br = new BufferedReader(fr);
            String line;
            int index = 0;

            while((line=br.readLine())!=null) {
                if (!line.isEmpty() || line.strip().length() > 0) {
                    lines.add(line);
                } else {
                    calorieMap.put(index, lines);

                    index++;

                    List<Integer> collect = lines.stream().map(Integer::parseInt).collect(Collectors.toList());
                    int t = 0;

                    for (Integer integer : collect) {
                        t += integer;
                    }

                    calorieMap2.put(index, t);
                    lines = new ArrayList<>();
                    if (t > sum) {
                        sum = t;
                    }
                }

            }
        }
        catch(IOException e) {
            e.printStackTrace();
        }

        //System.out.println(sum);
        List<Map.Entry<Integer, Integer>> l = new ArrayList<>(calorieMap2.entrySet());
        l.sort(Map.Entry.comparingByValue());
        for (Map.Entry<Integer, Integer> integerIntegerEntry : l) {
            System.out.println(integerIntegerEntry.getKey() + " " + integerIntegerEntry.getValue());
        }
        //System.out.println(calorieMap);
    }
}