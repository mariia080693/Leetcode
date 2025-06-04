import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
      products_new = products.melt(id_vars='product_id', 
                       value_vars=['store1', 'store2', 'store3'],
                       var_name='store', 
                       value_name='price')
    
      products_new = products_new.dropna(subset=['price'])
      return products_new

    