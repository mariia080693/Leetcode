import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    

    # Merge student names (optional)
    merged = pd.merge(examinations, students, on='student_id', how='left')

    # Count attendance
    attendance_counts = merged.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    # Create all possible student-subject pairs (cross join)
    students['key'] = 1
    subjects['key'] = 1
    all_pairs = pd.merge(students, subjects, on='key').drop('key', axis=1)

    # Merge counts with all pairs and fill missing with 0
    result = pd.merge(all_pairs, attendance_counts, on=['student_id', 'subject_name'], how='left')
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    # Sort
    result = result.sort_values(by=['student_id', 'subject_name']).reset_index(drop=True)

    return result
    