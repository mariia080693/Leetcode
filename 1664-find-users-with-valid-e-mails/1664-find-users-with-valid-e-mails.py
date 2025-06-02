import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'
    users_new = users[users['mail'].str.match(pattern)]

    return users_new

    