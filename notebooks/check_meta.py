import pandas as pd

df = pd.read_parquet('../outputs/data/master_events_cleaned.parquet')
euro_spain = df[(df['tournament'] == 'EURO2024') & (df['team'] == 'Spain')]
match_ids = euro_spain['match_id'].unique()

georgia_mid = None
for m in match_ids:
    if 'Georgia' in df[df['match_id']==m]['team'].unique():
        georgia_mid = m
        break

if georgia_mid:
    match_data = df[df['match_id'] == georgia_mid]
    spain_goals = len(match_data[(match_data['team'] == 'Spain') & (match_data['type'] == 'Shot') & (match_data['shot_outcome'] == 'Goal')])
    geo_goals = len(match_data[(match_data['team'] == 'Georgia') & (match_data['type'] == 'Shot') & (match_data['shot_outcome'] == 'Goal')])
    
    date_col = 'match_date'
    date_val = match_data[date_col].iloc[0] if date_col in df.columns else 'N/A'
    
    print(f'Match ID: {georgia_mid}, Date: {date_val}, Score: Spain {spain_goals} - {geo_goals} Georgia')
else:
    print('Match not found')
