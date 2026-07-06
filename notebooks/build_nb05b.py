import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch
import os
import sys

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

os.makedirs('../outputs/figures/2022', exist_ok=True)
sys.path.insert(0, os.path.abspath('..'))
from utils.config import OUTPUTS_DATA_DIR

print("Loading data...")
df = pd.read_parquet(os.path.join(OUTPUTS_DATA_DIR, 'master_events_cleaned.parquet'))

match_id = 3869220
spain = df[(df['match_id'] == match_id) & (df['team'] == 'Spain')].copy()

# Isolate players
ferran = spain[spain['player'].str.contains('Ferr', na=False) & spain['player'].str.contains('Torres', na=False)].copy()
nico = spain[spain['player'] == 'Nicholas Williams Arthuer'].copy()

# Filter out nan coordinates for plotting
ferran_actions = ferran.dropna(subset=['x', 'y'])
nico_actions = nico.dropna(subset=['x', 'y'])

# ========================================================
# 1. Head-to-Head Heatmap
# ========================================================
print("Generating Heatmap Comparison...")
fig, axs = plt.subplots(1, 2, figsize=(20, 8))
fig.set_facecolor('#0e1117')
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)

for i, (p_df, title) in enumerate([(ferran_actions, 'Ferran Torres (Starts, 75 mins)'), 
                                   (nico_actions, 'Nico Williams (Sub, 43 mins)')]):
    pitch.draw(ax=axs[i])
    if len(p_df) > 0:
        pitch.kdeplot(p_df['x'], p_df['y'], ax=axs[i], fill=True, levels=100, thresh=0, cut=4, cmap='plasma', alpha=0.7)
    axs[i].set_title(title, color='white', fontsize=18, fontweight='bold', pad=15)

plt.suptitle("Right Wing Heatmap Comparison vs Morocco", color='white', fontsize=24, fontweight='bold', y=1.05)
plt.savefig('../outputs/figures/2022/viz05b_rw_heatmaps.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ========================================================
# 2. Action Map (Dribbles & Carries)
# ========================================================
print("Generating Action Map (Dribbles & Carries)...")
fig, axs = plt.subplots(1, 2, figsize=(20, 8))
fig.set_facecolor('#0e1117')
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)

for i, (p_df, title) in enumerate([(ferran, 'Ferran Torres: Dribbles & Carries'), 
                                   (nico, 'Nico Williams: Dribbles & Carries')]):
    pitch.draw(ax=axs[i])
    
    # Dribbles
    dribbles = p_df[p_df['type'] == 'Dribble'].dropna(subset=['x', 'y'])
    succ_dribbles = dribbles[dribbles['dribble_outcome'] == 'Complete']
    fail_dribbles = dribbles[dribbles['dribble_outcome'] == 'Incomplete']
    
    pitch.scatter(succ_dribbles['x'], succ_dribbles['y'], ax=axs[i], s=150, c='#00ff85', edgecolors='white', marker='*', label='Succ. Dribble')
    pitch.scatter(fail_dribbles['x'], fail_dribbles['y'], ax=axs[i], s=100, c='#ff4b4b', edgecolors='white', marker='X', label='Fail. Dribble')
    
    # Progressive Carries
    def is_prog_carry(row):
        if row['type'] != 'Carry': return False
        if not isinstance(row.get('carry_end_location'), list): return False
        x_start, y_start = row['x'], row['y']
        x_end, y_end = row['carry_end_location']
        if x_start < 40: return False
        dist_start = np.sqrt((120 - x_start)**2 + (40 - y_start)**2)
        dist_end = np.sqrt((120 - x_end)**2 + (40 - y_end)**2)
        return dist_start - dist_end >= 10
        
    p_df['prog_carry'] = p_df.apply(is_prog_carry, axis=1)
    prog_carries = p_df[p_df['prog_carry'] == True]
    
    for _, row in prog_carries.iterrows():
        x_s, y_s = row['x'], row['y']
        x_e, y_e = row['carry_end_location']
        pitch.arrows(x_s, y_s, x_e, y_e, ax=axs[i], color='#00aaff', width=2, headwidth=4, headlength=4, alpha=0.8, label='Prog Carry')
    
    axs[i].set_title(title, color='white', fontsize=18, fontweight='bold', pad=15)
    
    # Handle legends to avoid duplicates
    handles, labels = axs[i].get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    if len(by_label) > 0:
        axs[i].legend(by_label.values(), by_label.keys(), loc='upper left', facecolor='#1e222b', edgecolor='white', labelcolor='white')

plt.savefig('../outputs/figures/2022/viz05b_rw_actions.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ========================================================
# 3. Touches in Box
# ========================================================
print("Generating Box Touches Map...")
fig, axs = plt.subplots(1, 2, figsize=(20, 8))
fig.set_facecolor('#0e1117')
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)

for i, (p_df, title) in enumerate([(ferran_actions, 'Ferran Torres: Box Touches'), 
                                   (nico_actions, 'Nico Williams: Box Touches')]):
    pitch.draw(ax=axs[i])
    
    touches = p_df[(p_df['x'] >= 102) & (p_df['y'] >= 18) & (p_df['y'] <= 62)]
    pitch.scatter(touches['x'], touches['y'], ax=axs[i], s=200, c='#ff00aa', alpha=0.9, edgecolors='white', lw=1.5, marker='o')
    
    axs[i].set_title(f"{title} ({len(touches)})", color='white', fontsize=18, fontweight='bold', pad=15)

plt.savefig('../outputs/figures/2022/viz05b_rw_box_touches.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

print("Notebook 05b visualizations built successfully!")
