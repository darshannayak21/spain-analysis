import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch
import os
import sys

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Create outputs dir
os.makedirs('../outputs/figures/2024', exist_ok=True)

# Add utils to path
sys.path.insert(0, os.path.abspath('..'))
from utils.config import OUTPUTS_DATA_DIR

# Load Data
print("Loading data...")
df = pd.read_parquet(os.path.join(OUTPUTS_DATA_DIR, 'master_events_cleaned.parquet'))

s22 = df[(df['tournament'] == 'WC2022') & (df['team'] == 'Spain')].copy()
s24 = df[(df['tournament'] == 'EURO2024') & (df['team'] == 'Spain')].copy()

# Filter shots
shots_22 = s22[s22['type'] == 'Shot'].copy()
shots_24 = s24[s24['type'] == 'Shot'].copy()

goals_22 = shots_22[shots_22['shot_outcome'] == 'Goal'].copy()
goals_24 = shots_24[shots_24['shot_outcome'] == 'Goal'].copy()

# =========================================================
# VIZ 70: Team-Level Shot Maps
# =========================================================
print("Generating Viz 70: Team-Level Shot Maps...")
fig, axs = plt.subplots(1, 2, figsize=(20, 8))
fig.set_facecolor('#0e1117')
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)

for i, (shots, title) in enumerate([(shots_22, 'Spain WC 2022 - All Shots'), (shots_24, 'Spain Euro 2024 - All Shots')]):
    pitch.draw(ax=axs[i])
    axs[i].set_title(title, color='white', fontsize=18, fontweight='bold', pad=15)
    
    # Non-goals
    non_goals = shots[shots['shot_outcome'] != 'Goal']
    if len(non_goals) > 0:
        pitch.scatter(non_goals['x'], non_goals['y'], s=(non_goals['shot_statsbomb_xg'].fillna(0) * 500) + 20, 
                      c='#ff4b4b', alpha=0.5, ax=axs[i], edgecolors='white', lw=0.5, marker='o')
        
    # Goals
    goals = shots[shots['shot_outcome'] == 'Goal']
    if len(goals) > 0:
        pitch.scatter(goals['x'], goals['y'], s=(goals['shot_statsbomb_xg'].fillna(0) * 500) + 50, 
                      c='#00ff85', alpha=0.9, ax=axs[i], edgecolors='white', lw=1.5, marker='*')
        
    # Stats text
    stats_text = (f"Total Shots: {len(shots)}\n"
                  f"Total Goals: {len(goals)}\n"
                  f"Total xG: {shots['shot_statsbomb_xg'].sum():.2f}\n"
                  f"xG/Shot: {shots['shot_statsbomb_xg'].mean():.2f}")
    axs[i].text(40, 115, stats_text, color='white', fontsize=12, 
                bbox=dict(facecolor='#1e222b', edgecolor='none', boxstyle='round,pad=0.5', alpha=0.8))

plt.savefig('../outputs/figures/2024/viz70_team_shot_maps.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# =========================================================
# VIZ 71: Goal Location Analysis
# =========================================================
print("Generating Viz 71: Goal Location Maps...")
fig, axs = plt.subplots(1, 2, figsize=(20, 8))
fig.set_facecolor('#0e1117')
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)

color_map = {
    'Open Play': '#00ff85',
    'Set Piece': '#ffaa00',
    'Penalty': '#ff4b4b',
    'Corner': '#00aaff',
    'Free Kick': '#ff00aa',
    'Counter': '#aa00ff'
}

for i, (goals, title) in enumerate([(goals_22, 'Spain WC 2022 - Goal Locations'), (goals_24, 'Spain Euro 2024 - Goal Locations')]):
    pitch.draw(ax=axs[i])
    axs[i].set_title(title, color='white', fontsize=18, fontweight='bold', pad=15)
    
    if len(goals) > 0:
        for _, row in goals.iterrows():
            play_pattern = row.get('play_pattern', 'Open Play')
            # simplify set piece vs open play
            cat = 'Open Play'
            if 'Corner' in play_pattern: cat = 'Corner'
            elif 'Free Kick' in play_pattern: cat = 'Free Kick'
            elif 'Penalty' in play_pattern: cat = 'Penalty'
            elif 'Counter' in play_pattern: cat = 'Counter'
            elif 'Set Piece' in play_pattern or 'Throw-in' in play_pattern: cat = 'Set Piece'
            
            c = color_map.get(cat, '#ffffff')
            pitch.scatter(row['x'], row['y'], s=150, c=c, alpha=0.9, ax=axs[i], edgecolors='white', lw=1, marker='*')
            
            # Annotate player name
            pitch.annotate(row['player'].split()[-1], (row['x']-2, row['y']), ax=axs[i], color='white', fontsize=9, ha='center')

plt.savefig('../outputs/figures/2024/viz71_goal_locations.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# =========================================================
# VIZ 72 & 73: Shot Origin & Buildup Passes
# =========================================================
print("Generating Viz 72/73: Shot Origins & Buildup...")

# Helper to find assist origin and buildup passes
def get_shot_buildup_info(df_shots, df_all):
    origins = []
    buildup_lengths = []
    for _, shot in df_shots.iterrows():
        match_id = shot['match_id']
        possession = shot['possession']
        
        # Get all events in this possession
        poss_events = df_all[(df_all['match_id'] == match_id) & (df_all['possession'] == possession)].copy()
        
        # Number of passes in buildup
        passes = poss_events[poss_events['type'] == 'Pass']
        buildup_lengths.append(len(passes))
        
        # Assist origin
        if 'pass_shot_assist' in poss_events.columns and (poss_events['pass_shot_assist'] == True).any():
            assist = poss_events[poss_events['pass_shot_assist'] == True].iloc[0]
            origins.append({'x': assist['x'], 'y': assist['y']})
        elif 'pass_goal_assist' in poss_events.columns and (poss_events['pass_goal_assist'] == True).any():
            assist = poss_events[poss_events['pass_goal_assist'] == True].iloc[0]
            origins.append({'x': assist['x'], 'y': assist['y']})
        else:
            origins.append({'x': np.nan, 'y': np.nan})
            
    return pd.DataFrame(origins), buildup_lengths

origins_22, buildup_22 = get_shot_buildup_info(shots_22, s22)
origins_24, buildup_24 = get_shot_buildup_info(shots_24, s24)

# Plot Assist Origins
fig, axs = plt.subplots(1, 2, figsize=(20, 8))
fig.set_facecolor('#0e1117')
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)

for i, (orig, title) in enumerate([(origins_22.dropna(), 'WC 2022 - Assist Origins'), (origins_24.dropna(), 'Euro 2024 - Assist Origins')]):
    pitch.draw(ax=axs[i])
    axs[i].set_title(title, color='white', fontsize=18, fontweight='bold', pad=15)
    
    # Plot zones
    axs[i].axvline(18, color='gray', linestyle='--', alpha=0.3)
    axs[i].axvline(62, color='gray', linestyle='--', alpha=0.3)
    axs[i].axvline(30, color='gray', linestyle=':', alpha=0.3)
    axs[i].axvline(50, color='gray', linestyle=':', alpha=0.3)
    
    pitch.scatter(orig['x'], orig['y'], s=80, c='#00aaff', alpha=0.8, ax=axs[i], edgecolors='white', lw=0.5)
    
    # Determine zones
    # Y < 18 or Y > 62 = Wide
    # 18 <= Y < 30 or 50 < Y <= 62 = Half-Space
    # 30 <= Y <= 50 = Central
    orig['zone'] = 'Central'
    orig.loc[(orig['y'] < 18) | (orig['y'] > 62), 'zone'] = 'Wide'
    orig.loc[((orig['y'] >= 18) & (orig['y'] < 30)) | ((orig['y'] > 50) & (orig['y'] <= 62)), 'zone'] = 'Half-Space'
    
    zone_counts = orig['zone'].value_counts(normalize=True) * 100
    stats_text = (f"Wide: {zone_counts.get('Wide', 0):.1f}%\n"
                  f"Half-Space: {zone_counts.get('Half-Space', 0):.1f}%\n"
                  f"Central: {zone_counts.get('Central', 0):.1f}%")
    axs[i].text(40, 115, stats_text, color='white', fontsize=12, 
                bbox=dict(facecolor='#1e222b', edgecolor='none', boxstyle='round,pad=0.5', alpha=0.8))

plt.savefig('../outputs/figures/2024/viz72_assist_origins.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# Plot Buildup Passes Distribution
fig, ax = plt.subplots(figsize=(10, 6))
fig.set_facecolor('#0e1117')
ax.set_facecolor('#0e1117')

bins = np.arange(0, max(max(buildup_22), max(buildup_24)) + 5, 2)
ax.hist(buildup_22, bins=bins, alpha=0.5, label='WC 2022', color='#ff4b4b', edgecolor='white')
ax.hist(buildup_24, bins=bins, alpha=0.5, label='Euro 2024', color='#00ff85', edgecolor='white')

ax.set_title('Passes in Buildup Sequence Before Shot', color='white', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Number of Passes', color='white', fontsize=12)
ax.set_ylabel('Frequency', color='white', fontsize=12)
ax.tick_params(colors='white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.legend(facecolor='#1e222b', edgecolor='white', labelcolor='white')

# Add text for averages
ax.text(0.7, 0.5, f"Avg Passes (2022): {np.mean(buildup_22):.1f}\nAvg Passes (2024): {np.mean(buildup_24):.1f}", 
        transform=ax.transAxes, color='white', fontsize=12, bbox=dict(facecolor='#1e222b', edgecolor='none'))

plt.savefig('../outputs/figures/2024/viz73_buildup_passes.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# =========================================================
# VIZ 74: Individual Player Shot/Goal Profiles
# =========================================================
print("Generating Viz 74: Individual Shot Profiles...")
# Get top 3 scorers for each tournament
top_22 = goals_22['player'].value_counts().head(3).index.tolist()
top_24 = goals_24['player'].value_counts().head(3).index.tolist()

def plot_player_shots(players, shots_df, filename, title_prefix):
    n = len(players)
    if n == 0: return
    fig, axs = plt.subplots(1, n, figsize=(7*n, 8))
    if n == 1: axs = [axs]
    fig.set_facecolor('#0e1117')
    pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)
    
    for i, player in enumerate(players):
        pitch.draw(ax=axs[i])
        p_shots = shots_df[shots_df['player'] == player]
        
        non_goals = p_shots[p_shots['shot_outcome'] != 'Goal']
        goals = p_shots[p_shots['shot_outcome'] == 'Goal']
        
        if len(non_goals) > 0:
            pitch.scatter(non_goals['x'], non_goals['y'], s=(non_goals['shot_statsbomb_xg'].fillna(0) * 500) + 20, 
                          c='#ff4b4b', alpha=0.5, ax=axs[i], edgecolors='white', lw=0.5, marker='o')
        if len(goals) > 0:
            pitch.scatter(goals['x'], goals['y'], s=(goals['shot_statsbomb_xg'].fillna(0) * 500) + 50, 
                          c='#00ff85', alpha=0.9, ax=axs[i], edgecolors='white', lw=1.5, marker='*')
            
        axs[i].set_title(f"{title_prefix}: {player}", color='white', fontsize=16, fontweight='bold', pad=15)
        stats = (f"Shots: {len(p_shots)}\n"
                 f"Goals: {len(goals)}\n"
                 f"xG: {p_shots['shot_statsbomb_xg'].sum():.2f}")
        axs[i].text(40, 115, stats, color='white', fontsize=12, ha='center',
                    bbox=dict(facecolor='#1e222b', edgecolor='none', boxstyle='round,pad=0.5', alpha=0.8))
        
    plt.savefig(f'../outputs/figures/2024/{filename}', dpi=200, bbox_inches='tight', facecolor='#0e1117')
    plt.close()

plot_player_shots(top_22, shots_22, 'viz74_player_shots_2022.png', 'WC 2022')
plot_player_shots(top_24, shots_24, 'viz74_player_shots_2024.png', 'Euro 2024')

# =========================================================
# VIZ 75: Goal-Threat Concentration
# =========================================================
print("Generating Viz 75: Goal Threat Concentration...")
fig, axs = plt.subplots(1, 2, figsize=(14, 6))
fig.set_facecolor('#0e1117')

for i, (shots_df, goals_df, title) in enumerate([(shots_22, goals_22, 'WC 2022 - Goal Concentration'), 
                                                 (shots_24, goals_24, 'Euro 2024 - Goal Concentration')]):
    axs[i].set_facecolor('#0e1117')
    
    # Calculate goal share
    total_goals = len(goals_df)
    if total_goals > 0:
        scorer_shares = goals_df['player'].value_counts(normalize=True) * 100
        
        # Plot pie chart or bar chart
        labels = scorer_shares.index[:4].tolist() + ['Others'] if len(scorer_shares) > 4 else scorer_shares.index.tolist()
        sizes = scorer_shares.values[:4].tolist() + [scorer_shares.values[4:].sum()] if len(scorer_shares) > 4 else scorer_shares.values.tolist()
        
        axs[i].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'color': 'white'}, 
                   colors=['#00ff85', '#00aaff', '#ffaa00', '#ff00aa', '#ff4b4b'])
        axs[i].set_title(title, color='white', fontsize=16, fontweight='bold')

plt.savefig('../outputs/figures/2024/viz75_goal_concentration.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

print("Notebook 09 Visualization Build Complete!")
