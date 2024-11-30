import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import java.util.Map;

public class JsonReader {
    // Метод для считывания JSON-файла и возврата данных в виде Map
    // ключ - знач типа String
    public Map<String, Integer> readJsonFile(String filePath) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();

        //метод возвращает объект типа Map(String, string), который содержит данные из джсон файла
        return objectMapper.readValue(new File(filePath), Map.class);
    }
}
