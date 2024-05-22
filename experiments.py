from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

# Загрузка набора данных Iris
iris = load_iris()
X, y = iris.data, iris.target

# Определение параметров для поиска
class_weight = {
    1: 1.78, 
    2: 0.50,  
    3: 0.95,
    4: 1.35
    }
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': range(3, 10),
    'min_samples_split': range(2, 11),
    'class_weight': ['balanced', class_weight]
}

# Создание объекта классификатора
dt_classifier = DecisionTreeClassifier()

# Использование GridSearchCV для поиска оптимальных параметров
grid_search = GridSearchCV(dt_classifier, param_grid, cv=5)

# Обучение и поиск лучших параметров
grid_search.fit(X, y)

# Печать результатов
print("Наилучший параметр class_weight:", grid_search.best_params_)