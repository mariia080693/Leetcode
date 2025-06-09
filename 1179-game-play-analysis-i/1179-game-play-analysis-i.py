import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_new = activity.groupby('player_id')['event_date'].min().reset_index()
    activity_new = activity_new.rename(columns = {'event_date':'first_login'})
    return activity_new[['player_id', 'first_login']]
    