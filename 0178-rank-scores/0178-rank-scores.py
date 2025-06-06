import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores_new = scores.sort_values(by = 'score', ascending = False).reset_index(drop=True)
    #return scores_new
    scores_new['rank'] = scores_new['score'].rank(method='dense', ascending=False).astype(int)
    return scores_new[['score', 'rank']]




    

    