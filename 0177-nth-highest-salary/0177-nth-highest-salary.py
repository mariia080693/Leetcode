import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    if (N > len(unique_salaries)) | (N <= 0):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [unique_salaries.iloc[N - 1]]})