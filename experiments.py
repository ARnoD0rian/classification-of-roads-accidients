import pandas as pd

#определите DataFrame
df = pd.DataFrame({'team':['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
 'points': [25, 12, 15, 14, 19, 23, 25, 29],
 'assists': [5, 7, 7, 9, 12, 9, 9, 4],
 'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})

#список названия столбцов
list(df)

['team', 'points', 'assists', 'rebounds']

#переименуйте названия колонок
df.rename(columns = {'team':'team_name', 'points':'points_scored'}, inplace = True )

#посмотреть обновленный список названий колонок
list(df)
print(df)