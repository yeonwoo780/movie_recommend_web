import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df2 = pd.read_csv("./model/tmdb.csv", encoding = 'utf-8')
count = TfidfVectorizer(stop_words="english")
count_matrix = count.fit_transform(df2['soup'])

cos_sim = cosine_similarity(count_matrix, count_matrix)
# print(cos_sim)

indices = pd.Series(df2.index, index=df2['title'])
idx = indices['Avatar']

sim_scores = list(enumerate(cos_sim[idx]))
sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse = True)
sim_scores = sim_scores[1:11]
print(sim_scores)

sim_indices = [i[0] for i in sim_scores]
tit = df2['title'].iloc[sim_indices]
dat = df2['release_date'].iloc[sim_indices]
return_df = pd.DataFrame(columns = ['Title', 'Year'])
return_df['Title'] = tit
return_df['Year'] = dat
print(return_df)