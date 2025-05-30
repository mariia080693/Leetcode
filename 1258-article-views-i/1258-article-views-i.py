import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    new_views = views[views['author_id'] == views['viewer_id']][['author_id']].drop_duplicates().sort_values(by='author_id', ascending=True)
    new_views.rename(columns = {'author_id':'id'}, inplace = True)
    return new_views