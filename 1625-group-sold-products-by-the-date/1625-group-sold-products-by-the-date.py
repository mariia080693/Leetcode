import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    '''
    activities_new = activities.groupby('sell_date')['product'].apply(lambda x: sorted(set(x))).reset_index(name='products')
    activities_new['num_sold'] = activities_new['products'].apply(len)
    activities_new['products'] = activities_new['products'].apply(lambda x: ','.join(x))
    result = activities_new[['sell_date', 'num_sold', 'products']].sort_values(by='sell_date').reset_index(drop=True)
    return result
    '''
    return activities.groupby(
    'sell_date'
    )['product'].agg([
    ('num_sold', 'nunique'),
    ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()