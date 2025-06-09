import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees_new = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    employees_new = employees_new.rename(columns = {'event_day':'day'})
    return employees_new[['day', 'emp_id', 'total_time']]

    