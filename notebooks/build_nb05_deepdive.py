import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch
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
match_events = df[df['match_id'] == match_id].copy()

spain = match_events[match_events['team'] == 'Spain'].copy()
morocco = match_events[match_events['team'] == 'Morocco'].copy()

# ========================================================
# 1. Team Heatmap Comparison
# ========================================================
print("Generating Team Heatmaps...")
fig, axs = plt.subplots(1, 2, figsize=(20, 8))
fig.set_facecolor('#0e1117')
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')

for i, (team_df, title, cmap) in enumerate([(spain, 'Spain Territory vs Morocco', 'Reds'), (morocco, 'Morocco Territory vs Spain', 'Greens')]):
    pitch.draw(ax=axs[i])
    actions = team_df.dropna(subset=['x', 'y'])
    pitch.kdeplot(actions['x'], actions['y'], ax=axs[i], fill=True, levels=100, thresh=0, cut=4, cmap=cmap, alpha=0.7)
    axs[i].set_title(title, color='white', fontsize=18, fontweight='bold', pad=15)

plt.savefig('../outputs/figures/2022/viz05a_morocco_team_heatmaps.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ========================================================
# 2. Touch Map in Opponent Box
# ========================================================
print("Generating Box Touches...")
fig, ax = plt.subplots(figsize=(10, 6))
fig.set_facecolor('#0e1117')
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc', half=True)
pitch.draw(ax=ax)

# Filter touches in box (x >= 102, 18 <= y <= 62)
touches = spain[(spain['x'] >= 102) & (spain['y'] >= 18) & (spain['y'] <= 62)].dropna(subset=['x', 'y'])
# exclude passes out of the box? We just plot all actions.
pitch.scatter(touches['x'], touches['y'], ax=ax, s=150, c='#ff4b4b', alpha=0.8, edgecolors='white', lw=1, marker='o')

ax.set_title(f'Spain Touches in Morocco Box (Total: {len(touches)})', color='white', fontsize=18, fontweight='bold', pad=15)
plt.savefig('../outputs/figures/2022/viz05b_spain_box_touches.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ========================================================
# 3. Flank Attack Analysis
# ========================================================
print("Generating Flank Analysis...")
fig, ax = plt.subplots(figsize=(12, 8))
fig.set_facecolor('#0e1117')
pitch.draw(ax=ax)

# We define lanes: Left (y < 30), Central (30 <= y <= 50), Right (y > 50)
spain_f3 = spain[spain['x'] >= 80].dropna(subset=['x', 'y'])

left_count = len(spain_f3[spain_f3['y'] < 30])
center_count = len(spain_f3[(spain_f3['y'] >= 30) & (spain_f3['y'] <= 50)])
right_count = len(spain_f3[spain_f3['y'] > 50])
total = left_count + center_count + right_count

# Draw lanes
ax.axhline(30, color='gray', linestyle='--', alpha=0.5)
ax.axhline(50, color='gray', linestyle='--', alpha=0.5)

pitch.kdeplot(spain_f3['x'], spain_f3['y'], ax=ax, fill=True, levels=50, thresh=0, cut=4, cmap='Blues', alpha=0.6)

stats_text = (f"Final Third Actions by Lane\n"
              f"Left: {left_count/total*100:.1f}%\n"
              f"Center: {center_count/total*100:.1f}%\n"
              f"Right: {right_count/total*100:.1f}%")
ax.text(60, 40, stats_text, color='white', fontsize=14, 
        bbox=dict(facecolor='#1e222b', edgecolor='white', boxstyle='round,pad=0.5', alpha=0.8))

ax.set_title('Spain Final Third Entry Density vs Morocco', color='white', fontsize=18, fontweight='bold', pad=15)
plt.savefig('../outputs/figures/2022/viz05c_spain_flanks.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ========================================================
# 4. Starting XI Player Heatmaps
# ========================================================
print("Generating Starting 11 Heatmaps...")

# Get all players who played in the first 45 mins. Since there were no first half subs, this is exactly 11.
first_half = spain[spain['minute'] < 45]
starting_11 = first_half['player'].dropna().unique()

# If somehow > 11, we limit it
starting_11 = list(starting_11)[:11]

# Plot 3x4 grid for the 11 players
fig, axs = plt.subplots(3, 4, figsize=(24, 15))
fig.set_facecolor('#0e1117')
axs = axs.flatten()
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')

for i, player in enumerate(starting_11):
    pitch.draw(ax=axs[i])
    p_events = spain[spain['player'] == player].dropna(subset=['x', 'y'])
    if len(p_events) > 0:
        pitch.kdeplot(p_events['x'], p_events['y'], ax=axs[i], fill=True, levels=100, thresh=0, cut=4, cmap='plasma', alpha=0.7)
    axs[i].set_title(player, color='white', fontsize=14, fontweight='bold')

# Hide the 12th subplot
axs[11].axis('off')

plt.suptitle("Spain Starting XI Heatmaps vs Morocco", color='white', fontsize=24, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('../outputs/figures/2022/viz05d_starting11_heatmaps.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

print("Morocco Deep Dive visualizations built successfully!")
