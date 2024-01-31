import pandas as pd

df = pd.read_csv("movie_dataset.csv")

x = df['Revenue (Millions)'].mean()
df['Revenue (Millions)'].fillna(x, inplace=True)

y = df['Metascore'].mean()
df['Metascore'].fillna(y, inplace=True)

# =============================================================================
# Question 1
max_rating = df['Rating'].max()

df_max_rating = df[df['Rating'] == max_rating]
max_rating_movie = df_max_rating['Title']

print('Question 1:')
print(max_rating_movie)
# =============================================================================

# =============================================================================
# Question 2
avg_rev = df['Revenue (Millions)'].mean()

print('\nQuestion 2:')
print(avg_rev)
# =============================================================================

# =============================================================================
# Question 3
df_2015_2017 = df[df['Year'].between(2015, 2017)]

avg_rev_2 = df_2015_2017['Revenue (Millions)'].mean()

print('\nQuestion 3:')
print(avg_rev_2)
# =============================================================================

# =============================================================================
# Question 4
df_2016 = df[df['Year'] == 2016]

movie_num_2016 = len(df_2016)

print('\nQuestion 4:')
print(movie_num_2016)
# =============================================================================

# =============================================================================
# Question 5
df_CN = df[df['Director'] == 'Christopher Nolan']
CN = len(df_CN)

print('\nQuestion 5:')
print(CN)
# =============================================================================

# =============================================================================
# Question 6
rat_8 = len(df[df['Rating']>= 8.0])

print('\nQuestion 6:')
print(rat_8)
# =============================================================================

# =============================================================================
# Question 7
cn_mean_rat = df_CN['Rating'].mean()

print('\nQuestion 7:')
print(cn_mean_rat)
# =============================================================================

# =============================================================================
# Question 8
average_ratings_by_year = df.groupby('Year')['Rating'].mean()

year_highest_rating = average_ratings_by_year.idxmax()

highest_average_rating = average_ratings_by_year.max()

print('\nQuestion 8:')
print(year_highest_rating)
# =============================================================================

# =============================================================================
# Question 9
df_2006 = df[df['Year'] == 2006]
movie_num_2006 = len(df_2006)

percentage_increase = ((movie_num_2016 - movie_num_2006) / movie_num_2006) * 100

print('\nQuestion 9:')
print(percentage_increase)
# =============================================================================

# =============================================================================
# Question 10
from collections import Counter

# Split the 'Actors' column to get individual actor names (handling both ', ' and ',')
all_actors = df['Actors'].apply(lambda x: [actor.strip() for actor in x.split(',')]).explode()

# Count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0][0]

print('\nQuestion 10:')
print(most_common_actor)

# =============================================================================

# =============================================================================
# Question 11
all_genres = df['Genre'].str.split(',').explode()

unique_genres = all_genres.nunique()

print('\nQuestion 11:')
print(unique_genres)
# =============================================================================

# =============================================================================
# Question 12
num_feat= df[['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]

correlation = num_feat.corr()

print('\nQuestion 12:')
print(correlation)
# =============================================================================




