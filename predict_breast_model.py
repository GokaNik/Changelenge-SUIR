import joblib
import pandas as pd
import sys
import json
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import warnings
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Загрузка модели
model = joblib.load('C://Users//kladm//Python study//study//breast_cancer_model.pkl')


def predict_from_file(file_path):
    try:
        # Загрузка данных
        data = pd.read_csv(file_path)  # Или другой формат, если нужно

        # Проверка на пустые данные
        if data.empty:
            raise ValueError("Загруженные данные пусты.")

        # Убедитесь, что данные имеют правильные признаки
        expected_columns = ['feature1', 'feature2', 'feature3']  # Замените на ваши признаки
        if not all(col in data.columns for col in expected_columns):
            raise ValueError(f"Отсутствуют необходимые столбцы: {expected_columns}")

        # Делаем предсказания
        predictions = model.predict(data)

        # Печатаем предсказания в формате JSON
        print(json.dumps(predictions.tolist()))  # Возвращаем как список

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    # Проверяем, передан ли путь к файлу через аргументы командной строки
    if len(sys.argv) < 2:
        # Если нет, открываем диалог выбора файла
        Tk().withdraw()  # Скрыть основное окно Tkinter
        file_path = askopenfilename(title="Выберите файл CSV", filetypes=[("CSV files", "*.csv")])

        if not file_path:  # Если пользователь отменил выбор файла
            print("Ошибка: Не выбран файл.", file=sys.stderr)
            sys.exit(1)
    else:
        file_path = sys.argv[1]

    predict_from_file(file_path)



