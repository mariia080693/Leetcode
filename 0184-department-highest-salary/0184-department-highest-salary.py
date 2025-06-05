import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    df_merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_x', '_y'))

   
    max_salary_per_dept = df_merged.groupby('departmentId')['salary'].transform('max')

    
    top_employees = df_merged[df_merged['salary'] == max_salary_per_dept]

    
    result = top_employees[['name_y', 'name_x', 'salary']].rename(columns={
        'name_y': 'Department',
        'name_x': 'Employee',
        'salary': 'Salary'
    })

    return result
            