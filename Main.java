import java.io.IOException; //находит иключения/ошибки
import java.util.Map;
import com.fasterxml.jackson.databind.ObjectMapper; //класс библиотеки jackson для работы с JSON
import java.io.File;
import java.io.BufferedReader; //класс чтения текстовых данных из входного потока
import java.io.InputStreamReader; //преобразование байтового потока в символьный
import java.io.File; //класс для работы с файлами и dir


public class Main {
    public static void main(String[] args) {

        try {

            //путь к json файлу с инфой о пользователе
            String filePath = "C://Users//kladm//ITMO//ChellengeH//synthetic_data.json";


            ProcessBuilder pb = new ProcessBuilder("python",
                    "C://Users//kladm//Python study//study//script_forml.py", //скрипт
                    filePath); //json файл

            pb.redirectErrorStream(true); //объединяем поток вывода и ошибок, чтобы можно было обрабатывать их вместе

            Process process = pb.start(); //запуск процесса выполнения скрипта

            String readyfilePath = "C://Users//kladm//Python study//study//example.json";

            JsonReader jsonReader = new JsonReader();

            Map<String, Integer> data = jsonReader.readJsonFile(readyfilePath);

            //выводим ключи и значения
            // entry хранит пару ключ-значение (проходим entry по парам ключ-знач)
            for (Map.Entry<String, Integer> entry : data.entrySet()) {
                System.out.println(entry.getKey() + ' ' + entry.getValue());
            }


        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}

