import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch
import os
import sys
import warnings
warnings.filterwarnings('ignore')

os.makedirs('../outputs/figures/2022', exist_ok=True)
sys.path.insert(0, os.path.abspath('..'))
from utils.config import OUTPUTS_DATA_DIR

print("Loading data...")
df = pd.read_parquet(os.path.join(OUTPUTS_DATA_DIR, 'master_events_cleaned.parquet'))
match_id = 3869220

spain_all = df[(df['team'] == 'Spain') & (df['tournament'] == 'WC2022')].copy()
morocco = df[(df['match_id'] == match_id) & (df['team'] == 'Morocco')].copy()
spain_mor = spain_all[spain_all['match_id'] == match_id].copy()
spain_other = spain_all[spain_all['match_id'] != match_id].copy()

# ==============================================================================
# 1. Lane-Split Analysis (Match vs Avg)
# ==============================================================================
print("Generating Lane-Split Chart...")
def get_lane_split(event_df):
    f3 = event_df[event_df['x'] >= 80].dropna(subset=['y'])
    if len(f3) == 0: return 0, 0, 0
    l = len(f3[f3['y'] < 30])
    c = len(f3[(f3['y'] >= 30) & (f3['y'] <= 50)])
    r = len(f3[f3['y'] > 50])
    t = l + c + r
    return (l/t*100), (c/t*100), (r/t*100)

m_l, m_c, m_r = get_lane_split(spain_mor)
o_l, o_c, o_r = get_lane_split(spain_other)

fig, ax = plt.subplots(figsize=(10, 6))
fig.set_facecolor('#0e1117')
ax.set_facecolor('#0e1117')
x = np.arange(3)
width = 0.35
ax.bar(x - width/2, [m_l, m_c, m_r], width, label='vs Morocco', color='#ff4b4b')
ax.bar(x + width/2, [o_l, o_c, o_r], width, label='Tournament Avg (Other 3)', color='#00aaff')

ax.set_ylabel('% of Final Third Entries', color='white', fontsize=12)
ax.set_title('Spain Attack Lane Distribution', color='white', fontsize=16, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(['Left (y < 30)', 'Central (30 <= y <= 50)', 'Right (y > 50)'], color='white')
ax.tick_params(colors='white')
for spine in ax.spines.values(): spine.set_color('white')
ax.legend(facecolor='#1e222b', edgecolor='white', labelcolor='white')
plt.savefig('../outputs/figures/2022/viz05b_lane_split.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ==============================================================================
# 2. Morocco Defensive Heatmap
# ==============================================================================
print("Generating Morocco Defensive Heatmap...")
fig, ax = plt.subplots(figsize=(12, 8))
fig.set_facecolor('#0e1117')
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
pitch.draw(ax=ax)

# Def actions: Pressure, Block, Clearance, Interception, Duel, Ball Recovery, Foul Committed
def_actions = ['Pressure', 'Block', 'Clearance', 'Interception', 'Duel', 'Ball Recovery', 'Foul Committed']
mor_def = morocco[morocco['type'].isin(def_actions)].dropna(subset=['x', 'y'])

pitch.kdeplot(mor_def['x'], mor_def['y'], ax=ax, fill=True, levels=100, thresh=0, cut=4, cmap='Greens', alpha=0.7)
# Draw lanes
ax.axhline(30, color='gray', linestyle='--', alpha=0.5)
ax.axhline(50, color='gray', linestyle='--', alpha=0.5)

ax.set_title('Morocco Defensive Actions (Proving Central Denial)', color='white', fontsize=18, fontweight='bold', pad=15)
plt.savefig('../outputs/figures/2022/viz05b_morocco_def_heatmap.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ==============================================================================
# 3. Match Timeline
# ==============================================================================
print("Generating Match Timeline...")
subs = spain_mor[spain_mor['type'] == 'Substitution'].copy()
morata_sub = subs[subs['substitution_replacement'] == 'lvaro Borja Morata Martn']
if len(morata_sub) == 0: morata_sub = subs[subs['substitution_replacement'].str.contains('Morata', na=False)]
nico_sub = subs[subs['substitution_replacement'].str.contains('Williams', na=False)]

fig, ax = plt.subplots(figsize=(15, 3))
fig.set_facecolor('#0e1117')
ax.set_facecolor('#0e1117')

ax.plot([0, 120], [0, 0], color='white', lw=3)
ax.scatter([0, 45, 90, 120], [0, 0, 0, 0], color='white', s=100, zorder=5)
ax.text(0, 0.1, 'Kickoff', color='white', ha='center', fontsize=12)
ax.text(45, 0.1, 'HT', color='white', ha='center', fontsize=12)
ax.text(90, 0.1, 'FT', color='white', ha='center', fontsize=12)
ax.text(120, 0.1, 'Penalties', color='white', ha='center', fontsize=12)

if len(morata_sub) > 0:
    m_min = morata_sub['minute'].values[0]
    ax.scatter([m_min], [0], color='#00ff85', s=150, zorder=5)
    ax.text(m_min, -0.2, f'Morata IN ({m_min}\')', color='#00ff85', ha='center', fontsize=12, rotation=45)

if len(nico_sub) > 0:
    n_min = nico_sub['minute'].values[0]
    ax.scatter([n_min], [0], color='#00aaff', s=150, zorder=5)
    ax.text(n_min, 0.2, f'Nico IN ({n_min}\')', color='#00aaff', ha='center', fontsize=12, rotation=45)
    
    # Did Nico leave?
    nico_off = subs[subs['player'].str.contains('Williams', na=False)]
    if len(nico_off) > 0:
        noff_min = nico_off['minute'].values[0]
        ax.scatter([noff_min], [0], color='#ff4b4b', s=150, zorder=5)
        ax.text(noff_min, -0.2, f'Nico OUT ({noff_min}\')', color='#ff4b4b', ha='center', fontsize=12, rotation=45)

ax.set_xlim(-5, 125)
ax.set_ylim(-0.5, 0.5)
ax.axis('off')
ax.set_title('Match Substitution Timeline', color='white', fontsize=16, fontweight='bold')
plt.savefig('../outputs/figures/2022/viz05b_timeline.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# The before/after and specific player stats will be computed natively inside the notebook for transparency.
print("Extended visual assets built.")
