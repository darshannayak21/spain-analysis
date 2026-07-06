import pandas as pd
import numpy as np
import os
import sys
import time
from statsbombpy import sb
import warnings
warnings.filterwarnings('ignore')

OUTPUTS_DATA_DIR = 'outputs/data'

print("Pulling France WC 2022 matches...")
matches = sb.matches(competition_id=43, season_id=106)
france_matches = matches[(matches['home_team'] == 'France') | (matches['away_team'] == 'France')]
print(f"Found {len(france_matches)} France matches in WC 2022.")

events_list = []
lineups_list = []

for idx, row in france_matches.iterrows():
    match_id = int(row['match_id'])
    tourney = 'WC2022'
    opponent = row['away_team'] if row['home_team'] == 'France' else row['home_team']
    stage = row['competition_stage']
    
    print(f"Pulling Match {match_id} | vs {opponent} ({stage})...")
    
    # Events
    try:
        match_events = sb.events(match_id=match_id)
        match_events['match_id'] = match_id
        match_events['tournament'] = tourney
        match_events['opponent'] = opponent
        match_events['competition_stage'] = stage
        events_list.append(match_events)
    except Exception as e:
        print(f"  [ERR] Events: {e}")
        
    time.sleep(1.5)
    
    # Lineups
    try:
        match_lineups = sb.lineups(match_id=match_id)
        for team_name, df in match_lineups.items():
            df = df.copy()
            df['match_id'] = match_id
            df['tournament'] = tourney
            df['team_name'] = team_name
            lineups_list.append(df)
    except Exception as e:
        print(f"  [ERR] Lineups: {e}")
        
    time.sleep(1.5)

print("\nProcessing data...")
france_events = pd.concat(events_list, ignore_index=True)
france_lineups = pd.concat(lineups_list, ignore_index=True)

def prep_for_parquet(df):
    df_out = df.copy()
    for col in df_out.columns:
        if df_out[col].apply(lambda x: isinstance(x, (list, dict))).any():
            df_out[col] = df_out[col].astype(str)
    return df_out

france_events_pq = prep_for_parquet(france_events)
france_lineups_pq = prep_for_parquet(france_lineups)

# Load existing
print("Loading existing raw datasets...")
events_raw = pd.read_parquet(os.path.join(OUTPUTS_DATA_DIR, 'events_raw.parquet'))
lineups_raw = pd.read_parquet(os.path.join(OUTPUTS_DATA_DIR, 'lineups_raw.parquet'))

# Append and save
events_combined = pd.concat([events_raw, france_events_pq], ignore_index=True).drop_duplicates(subset=['id'], keep='last')
lineups_combined = pd.concat([lineups_raw, france_lineups_pq], ignore_index=True).drop_duplicates(subset=['match_id', 'team_name', 'player_id'], keep='last')

events_combined.to_parquet(os.path.join(OUTPUTS_DATA_DIR, 'events_raw.parquet'), index=False)
lineups_combined.to_parquet(os.path.join(OUTPUTS_DATA_DIR, 'lineups_raw.parquet'), index=False)

print(f"Success! Appended {len(france_events)} France events. New total: {len(events_combined)}")
print(f"Appended {len(france_lineups)} France lineup rows. New total: {len(lineups_combined)}")
