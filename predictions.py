import joblib
import pandas as pd
import sys
import json

# Загрузка модели
model = joblib.load('model.pkl')

def predict_from_file(file_path):
    # Загрузка данных
    data = pd.read_csv(file_path)  # Или другой формат, если нужно
    predictions = model.predict(data)  # Делаем предсказания

    # Печатаем предсказания в формате JSON
    print(json.dumps(predictions.tolist()))  # Возвращаем как список

if __name__ == "__main__":
    # Получаем путь к файлу из аргументов
    file_path = sys.argv[1]
    predict_from_file(file_path)
