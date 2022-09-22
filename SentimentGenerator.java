import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files


public class SentimentGenerator {
    public static void main(String[] args) {
        System.out.println("loldx");
        try {
            File myObj = new File("json.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNext()) {
                String data = myReader.next();
                if(!data.equals("*")){
                    System.out.print(data);
                }
            }
            myReader.close();
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
    }
}