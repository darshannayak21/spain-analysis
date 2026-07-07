import pandas as pd
from mplsoccer import VerticalPitch
import matplotlib.pyplot as plt

df = pd.read_parquet('../outputs/data/master_events_cleaned.parquet')
spain_match = df[(df['match_id'] == 3941018) & (df['team'] == 'Spain')]
spain_f3 = spain_match[spain_match['x'] >= 80]

print("Spain F3 X min/max:", spain_f3['x'].min(), spain_f3['x'].max())
print("Spain F3 Y min/max:", spain_f3['y'].min(), spain_f3['y'].max())

geo_match = df[(df['match_id'] == 3941018) & (df['team'] == 'Georgia')]
geo_def = geo_match[geo_match['type'].isin(['Pressure', 'Tackle', 'Interception', 'Block', 'Foul Committed'])]

print("Geo Def X min/max:", geo_def['x'].min(), geo_def['x'].max())
print("Geo Def Y min/max:", geo_def['y'].min(), geo_def['y'].max())

# Try plotting a single vertical pitch with both pitch.kdeplot and pitch.scatter
fig, ax = plt.subplots(figsize=(8, 10))
pitch = VerticalPitch(pitch_type='statsbomb', half=True)
pitch.draw(ax=ax)
pitch.kdeplot(geo_def['x'], geo_def['y'], ax=ax, fill=True, cmap='YlGn', alpha=0.5)
pitch.scatter(spain_f3['x'], spain_f3['y'], ax=ax, color='red')
plt.savefig('test_pitch.png')
print("Test plot saved to test_pitch.png")
