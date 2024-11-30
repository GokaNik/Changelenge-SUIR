from sklearn.cluster import KMeans,AffinityPropagation,SpectralClustering
from sklearn.cluster import AgglomerativeClustering, BisectingKMeans
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
kmeans=KMeans(n_clusters=3)
kmeans.fit(X_tsne)
with open('super_model2.pkl', 'wb') as f:
    pickle.dump(kmeans,f)
    # kmeans=pickle.load(f)
print(kmeans)

clusters = kmeans.predict(X_tsne)
silhouette_avg =silhouette_score(X_tsne, clusters)

print(f"Silhouette Coefficient: {silhouette_avg:.3f}")