import java.io.File;
import java.util.Scanner;

public class Zad2 {

    public static void main(String[] args) {
        long startTime = System.nanoTime();

        try {
            Scanner fileScanner = new Scanner(new File("../Covid19.txt"));
            int sum = 0;

            while (fileScanner.hasNext()) {
                String fileLine = fileScanner.nextLine();
                String[] lineArray = fileLine.split("\t| ");

                if (lineArray.length > 4)
                    try {
                        sum += Integer.parseInt(lineArray[4]);
                    } catch (Exception ignored) {}

            }

            System.out.println("Sum " + sum);
            System.out.println("Exec time: " + ((System.nanoTime() - startTime) / 1000000) + "ms");
        } catch (Exception ex) {
            System.out.println("Cannot find the file !");
        }
    }

}
