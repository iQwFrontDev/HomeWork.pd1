import pandas as pd

#Задание №1

df_movie = pd.read_csv('movies.csv')
df_rating = pd.read_csv('ratings.csv')

df_merged = df_movie.merge(df_rating, on = 'movieId', how='left')
rating_filter = df_merged[df_merged.rating == 5]
rating_result = rating_filter.groupby('title').count().sort_values('rating', ascending=False)
df_rename = rating_result.rename(columns={'rating': 'count_5'})
# print(df_rename.head())

#Задание №2

df_power = pd.read_csv('power.csv')
# print(df_power[ df_power['country'].str.contains('est', case=False) ]['country'].unique())
df_filter_country = df_power[ (df_power['country']=='Lithuania') | (df_power['country']=='Latvia') | (df_power[
                                                                                                       'country'] ==
                                                                                              'Estonia')]

df_filter_year = df_filter_country[(df_filter_country['year'] >= 2005) & (df_filter_country['year'] <= 2010) & (
    df_filter_country['quantity'] > 0)]

df_filter_category = df_filter_year[df_filter_year['category'].isin([4, 12, 21])]
df_group = df_filter_category.groupby(['country', 'category','year'])['quantity']. sum().reset_index()
df_result =  df_group.sort_values(by=['country', 'year' ], ascending=[True, True])

# print(df_result.head())

#Задание №3

page_url = 'https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html'

df = pd.read_html(page_url, attrs = {'class': 'docutils'}, encoding='utf-8')

# print(df)