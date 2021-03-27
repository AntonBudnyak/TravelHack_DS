import pandas as pd
from scipy.sparse import load_npz
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:

    def __init__(self, top_k: int = 15):
        self.top_k = top_k
        self.embeddings = load_npz('data/sparse_full.npz')
        self.pois = pd.read_csv('data/POIs_main.csv')
    
    def predict(self, idx_list, capital):

        liked_df = self.pois[self.pois.index.isin(idx_list)]
        idx_this_capital = self.pois.index[self.pois.capital == capital].values

        cat_list = liked_df.groupby('category')['xid'].count().sort_values(ascending = False).index        
        recs_by_categories = []
        for category in cat_list:
            idx_from_category = liked_df.index[liked_df.category == category].values
            avg_vector = self.embeddings[idx_from_category,:].sum(axis = 0)/len(idx_from_category)
            recs = pd.DataFrame(cosine_similarity(avg_vector,
                                   self.embeddings[idx_this_capital,:]).T).sort_values(0,ascending=False)[0:self.top_k+1].index
            recs_by_categories.append(recs)
        rec_list = []
        for i in range(self.top_k):
            for j in range(len(recs_by_categories)):
                rec_list.append(recs_by_categories[j][i]+1)
        for idx in idx_list:
            try:
                rec_list.remove(idx+1)
            except:
                pass
        return rec_list