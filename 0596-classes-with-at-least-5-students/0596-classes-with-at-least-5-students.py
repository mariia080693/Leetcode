import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses_new = courses.groupby('class')['student'].nunique().reset_index()
    courses_new = courses_new[courses_new['student'] >= 5]
    return courses_new[['class']]
    