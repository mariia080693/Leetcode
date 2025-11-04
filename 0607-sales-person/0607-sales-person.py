import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
   merged = pd.merge(orders, company, on = 'com_id', how = 'left')
   sale_red = merged.loc[merged['name']=='RED', 'sales_id'].unique()
   result = sales_person[~sales_person['sales_id'].isin(sale_red)][['name']]

   return result

    