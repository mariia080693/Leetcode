import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    employees['bonus'] = 0
    mask =  (employees['employee_id']%2 != 0) & (employees['name'].str[0] != 'M')
    employees.loc[mask, 'bonus'] = employees['salary']
    return employees[['employee_id', 'bonus']].sort_values(by = 'employee_id')   

    