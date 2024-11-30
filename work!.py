import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pickle
from sklearn import metrics


#clientId,organizationId,segment,role,organizations,currentMethod,mobileApp,signatures.common.mobile,
# signatures.common.web,signatures.special.mobile,signatures.special.web,availableMethods,claims


with open("synthetic_data.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
dataset = pd.json_normalize(data)

dataset.drop(["clientId", "currentMethod", "organizationId", "availableMethods", "claims"], axis=1, inplace=True)
#print(dataset)

dataset.loc[dataset['segment'] == 'Средний бизнес', 'segment'] = 1
dataset.loc[dataset['segment'] == 'Малый бизнес', 'segment'] = 0
dataset.loc[dataset['segment'] == 'Крупный бизнес', 'segment'] = 2
dataset.loc[dataset['role'] == 'Сотрудник', 'role'] = 0
dataset.loc[dataset['role'] == 'ЕИО', 'role'] = 1


#========================
scaler1 = StandardScaler()
scaled_data1 = scaler1.fit_transform(dataset)

# Применение PCA для снижения размерности
pca = PCA(n_components=2)  # Снижение размерности до 2 компонентов для наглядности
principalComponents = pca.fit_transform(scaled_data1)

drevo1 = AgglomerativeClustering(linkage='ward', n_clusters=3)
drevo1.fit(principalComponents)
drevo_cl = drevo1.labels_

sil_avg_drevo1 = metrics.silhouette_score(principalComponents, drevo_cl)
#========================

kk = dataset.values

# Масштабирование данных
scaler = MinMaxScaler()
#scaler = StandardScaler()
X_scaled = scaler.fit_transform(kk)

# Применение t-SNE для визуализации
tsne = TSNE(n_components=2, max_iter=1000, random_state=1)
X_tsne = tsne.fit_transform(X_scaled)

# 
kmeans=KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=1)
kmeans.fit(X_tsne)

drevo = AgglomerativeClustering(linkage='ward', n_clusters=3)
drevo.fit(X_tsne)
drevo_cl = drevo.labels_

spectral_model = SpectralClustering(
    n_clusters=3,  # Количество кластеров
    affinity="nearest_neighbors",  # Тип аффинити (метода близости)
    n_neighbors=10,  # Количество ближайших соседей для построения графов
    assign_labels="discretize"  # Метод назначения меток кластеров
)
spectral_model.fit(X_tsne)
scpectral_cl = spectral_model.labels_

clusters = kmeans.predict(X_tsne)
ind_0= []
ind_1= []
ind_2 = []
for i in range(0, len(clusters)):
    if clusters[i] == 0:
        ind_0.append(i)
    elif clusters[i] == 1:
        ind_1.append(i)
    else:
        ind_2.append(i)
"""
print(dataset.iloc[ind_0])
print("------------------")
print(dataset.iloc[ind_1])
print("------------------")
print(dataset.iloc[ind_2])
"""

filename = 'model_ml_clastr.sav'
pickle.dump(kmeans, open(filename, 'wb')) 

silhouette_avg = metrics.silhouette_score(X_tsne, clusters)
sil_avg_drevo = metrics.silhouette_score(X_tsne, drevo_cl)
sil_spec = metrics.silhouette_score(X_tsne, scpectral_cl)


print(f"Silhouette Coefficient: {silhouette_avg:.3f}")
print(f"Silhouette Coefficient: {sil_avg_drevo:.3f}")
print(f"Silhouette Coefficient: {sil_spec:.3f}")
print(f"Silhouette Coefficient: {sil_avg_drevo1:.3f}")


"""
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], cmap='viridis')
plt.show()
"""




