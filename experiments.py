from sklearn.neighbors import KDTree
import numpy as np

# Создание массива данных
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# Строим KD-дерево
kdt = KDTree(X, leaf_size=30, metric='euclidean')

# Поиск ближайших соседей
distances, indices = kdt.query(X, k=2, return_distance=True)

print(distances)
print(indices)