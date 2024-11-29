from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd
import mglearn
from IPython.display import display
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


plt.rc('font', family='Verdana')

import json
with open("synthetic_data.json", 'r', encoding='utf-8') as f:
 data = json.load(f)
# Нормализация данных
dataset = pd.json_normalize(data)
dataset=dataset.drop(['clientId','organizationId','currentMethod','availableMethods'],axis=1)
dataset.loc[dataset['segment'] == 'Средний бизнес', 'segment'] = 1
dataset.loc[dataset['segment'] == 'Малый бизнес', 'segment'] = 0
dataset.loc[dataset['segment'] == 'Крупный бизнес', 'segment'] = 2
dataset.loc[dataset['role'] == 'Сотрудник', 'role'] = 0
dataset.loc[dataset['role'] == 'ЕИО', 'role'] = 1
# Масштабируем данные
scaler = StandardScaler()
dataset_scaled = scaler.fit_transform(dataset)
kmeans = KMeans(n_clusters=3, random_state=1)
kmeans.fit(dataset_scaled)
clusters = kmeans.predict(dataset_scaled)

# Понижение размерности до 2D
pca = PCA(n_components=2)
dataset_pca = pca.fit_transform(dataset_scaled)

# Центроиды в PCA-пространстве
centroids_pca = pca.transform(kmeans.cluster_centers_)

plt.figure(figsize=(8, 6))

# Точки данных
plt.scatter(dataset_pca[:, 0], dataset_pca[:, 1], c=clusters, cmap='viridis', s=50, label='Data points')

# Центроиды
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], c='red', s=200, marker='X', label='Centroids')

# Оформление
plt.title("Кластеры данных с K-Means (после PCA)")
plt.xlabel("Первая главная компонента")
plt.ylabel("Вторая главная компонента")
plt.legend()
plt.grid(True)
plt.show()






