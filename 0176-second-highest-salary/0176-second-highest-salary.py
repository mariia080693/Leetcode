import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee_new = employee['salary'].drop_duplicates().sort_values(ascending = False).reset_index()
    if len(employee_new['salary']) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        return pd.DataFrame({'SecondHighestSalary':[employee_new['salary'].iloc[1]]})    
    