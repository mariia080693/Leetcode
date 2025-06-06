import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    a = (accounts['income'] < 20000).sum()
    b = ((accounts['income'] >= 20000) & (accounts['income'] <=50000)).sum()
    c = (accounts['income'] > 50000).sum()
    accounts_new = pd.DataFrame()
    accounts_new['category'] = ['High Salary', 'Low Salary', 'Average Salary']
    accounts_new['accounts_count'] = [c,a,b]
    return accounts_new[['category', 'accounts_count']]


    