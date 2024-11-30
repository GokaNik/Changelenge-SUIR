import joblib
import pandas as pd
import sys
import json
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import numpy as np


def standart(dataset):
    dataset.drop(["clientId", "currentMethod", "organizationId", "availableMethods", "claims"], axis=1, inplace=True)
    dataset.loc[dataset['segment'] == 'Средний бизнес', 'segment'] = 1
    dataset.loc[dataset['segment'] == 'Малый бизнес', 'segment'] = 0
    dataset.loc[dataset['segment'] == 'Крупный бизнес', 'segment'] = 2
    dataset.loc[dataset['role'] == 'Сотрудник', 'role'] = 0
    dataset.loc[dataset['role'] == 'ЕИО', 'role'] = 1
    return dataset


# загрузка первого дата сета
with open("synthetic_data_realistic.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
dataset = pd.json_normalize(data)
dataset = standart(dataset)

# Загрузка модели
model = joblib.load('super_model.pkl')


def predict_from_file(file_path):
    # Загрузка данных
    with open(file_path, 'r', encoding='utf-8') as f:
        ask = json.load(f)
    ask = pd.json_normalize(ask)  # Или другой формат, если нужно

    ask = standart(ask)
    # new_row = ask.values

    new_row = ask.loc[0].to_dict()

    dataset.loc[len(dataset)] = new_row

    scaler1 = StandardScaler()
    scaled_data1 = scaler1.fit_transform(dataset)

    tsne = TSNE(n_components=2, max_iter=1000, random_state=1)
    X_tsne = tsne.fit_transform(scaled_data1)

    X_tsne = [X_tsne[len(X_tsne) - 1]][0].reshape((1, 2))

    predictions = model.predict(X_tsne)  # Делаем предсказания
    # Печатаем предсказания в формате JSON
    result = {"class": predictions[len(predictions) - 1].item()}

    print(json.dumps(result))


if __name__ == "__main__":
    # Получаем путь к файлу из аргументов
    file_path = 'synthetic_data.json'
    predict_from_file(file_path)

