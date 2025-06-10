import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher_new = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')
    return teacher_new

    