import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    users['name'] = users['name'].str.strip().str.lower().str.capitalize()
    users.sort_values(by = 'user_id', inplace = True)
    return users

    