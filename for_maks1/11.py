
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd
import mglearn
from IPython.display import display
from pandas.plotting import scatter_matrix
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pickle
import joblib
plt.rc('font', family='Verdana')

import json

with open("synthetic_clients_correlated1.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    # print(data_np)
# Нормализация данных
dataset = pd.json_normalize(data)
def standart(dataset):

    dataset.drop(["clientId", "currentMethod", "organizationId", "availableMethods", "claims"], axis=1, inplace=True)
    dataset.loc[dataset['segment'] == 'Средний бизнес', 'segment'] = 1
    dataset.loc[dataset['segment'] == 'Малый бизнес', 'segment'] = 0
    dataset.loc[dataset['segment'] == 'Крупный бизнес', 'segment'] = 2
    dataset.loc[dataset['role'] == 'Сотрудник', 'role'] = 0
    dataset.loc[dataset['role'] == 'ЕИО', 'role'] = 1
    return dataset
dataset=standart(dataset)


scaler1 = StandardScaler()
scaled_data1 = scaler1.fit_transform(dataset)

# Применение PCA для снижения размерности
pca = PCA(n_components=2)  # Снижение размерности до 2 компонентов для наглядности
principalComponents = pca.fit_transform(scaled_data1)

tsne = TSNE(n_components=2, max_iter=1000, random_state=1)
X_tsne=tsne.fit_transform(dataset)
# kmeans=KMeans(n_clusters=3)
# kmeans.fit(X_tsne)
with open('super_model2.pkl', 'rb') as f:
    # pickle.dump(kmeans,f)
    kmeans=pickle.load(f)
print(kmeans)
dataset['Cluster'] = kmeans.predict(X_tsne)
features = ['segment', 'role', 'organizations',
            'mobileApp', 'signatures.common.mobile', 'Cluster']

numeric_features = dataset.select_dtypes(include=[np.number])

plt.rcParams.update({'font.size': 8})

axes = scatter_matrix(numeric_features, figsize=(12, 12), c=dataset['Cluster'],
                      alpha=0.9, cmap='viridis', diagonal='kde')

for ax in axes.ravel():  # Проходим по всем объектам Axes
    ax.xaxis.label.set_rotation(90)  # Поворачиваем метки на X
    ax.yaxis.label.set_rotation(0)  # Убираем поворот на Y
    ax.tick_params(axis='x', labelrotation=90)  # Поворачиваем значения на X
    ax.tick_params(axis='y', labelrotation=0)  # Оставляем значения на Y горизонтальными


# plt.suptitle("Scatter Matrix with Clusters")
# plt.show()


# clusters = kmeans.predict(X_tsne)




plt.figure(figsize=(8, 6))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=dataset['Cluster'], cmap='viridis', s=50, alpha=0.8)
plt.title("t-SNE Visualization of Clusters")
plt.xlabel("t-SNE Component 1")
plt.ylabel("t-SNE Component 2")
plt.show()

