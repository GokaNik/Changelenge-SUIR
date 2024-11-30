import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import com.fasterxml.jackson.databind.ObjectMapper; //класс библиотеки jackson для работы с JSON
import org.apache.commons.io.IOUtils;
import java.io.File; //класс для работы с файлами и dir
import java.nio.charset.StandardCharsets;


public class Main {
    public static void main(String[] args) {

        try {

            //путь к json файлу с инфой о пользователе
            String filePath = "C://Users//kladm//ITMO//ChellengeH//synthetic_data (1).json";


            ProcessBuilder pb = new ProcessBuilder("python",
                    "C://Users//kladm//Python study//study//script_forml.py", //скрипт
                    filePath); //json файл

            pb.redirectErrorStream(true); //объединяем поток вывода и ошибок, чтобы можно было обрабатывать их вместе

            Process process = pb.start(); //запуск процесса выполнения скрипта


            InputStream is = process.getInputStream();
            String resultString = IOUtils.toString(is, StandardCharsets.UTF_8);
            System.out.println(resultString);

        } catch (IOException e) {
            e.printStackTrace(); // Обработка ошибок ввода-вывода

        } catch (Exception e) {
            e.printStackTrace(); // Обработка других исключений
        }

    }
}

