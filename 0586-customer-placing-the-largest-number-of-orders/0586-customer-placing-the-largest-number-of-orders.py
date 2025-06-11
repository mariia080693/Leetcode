import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()

    """
    # long solution
    
    orders_new = orders.groupby('customer_number')['order_number'].size().reset_index()
    max_count = orders_new['order_number'].max()
    orders_new = orders_new[orders_new['order_number'] == max_count]
    return orders_new[['customer_number']]
    """
    