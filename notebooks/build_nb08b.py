"""NB08b: Yamal/Williams Deep Dive + Penetration Rankings + Who Drove the Change"""
import pandas as pd, numpy as np, os, sys, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patheffects as pe
from mplsoccer import Pitch, VerticalPitch
import warnings; warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(BASE)
os.makedirs(os.path.join(ROOT, 'outputs', 'figures', '2024'), exist_ok=True)
sys.path.insert(0, ROOT); os.chdir(BASE)
from utils.config import OUTPUTS_DATA_DIR

df = pd.read_parquet(os.path.join(OUTPUTS_DATA_DIR, 'master_events_cleaned.parquet'))
s24 = df[(df['tournament']=='EURO2024')&(df['team']=='Spain')].copy()
s22 = df[(df['tournament']=='WC2022')&(df['team']=='Spain')].copy()
actual = s24['common_name'].dropna().unique().tolist()

# ── 1. YAMAL DEEP DIVE (4-panel) ──
yamal_name = [n for n in actual if 'yamal' in str(n).lower()][0]
yamal = s24[s24['common_name']==yamal_name]
yt = yamal[yamal['type'].isin(['Pass','Carry','Dribble'])].dropna(subset=['x','y'])
ypp = yamal[yamal['is_progressive_pass']==True].dropna(subset=['x','y','pass_end_x','pass_end_y'])
ypc = yamal[yamal['is_progressive_carry']==True].dropna(subset=['x','y','carry_end_x','carry_end_y'])
ydrib = yamal[yamal['type']=='Dribble'].dropna(subset=['x','y'])

fig, axes = plt.subplots(1, 4, figsize=(28,7), facecolor='#0e1117')
for ax in axes:
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc'); pitch.draw(ax=ax)

# Panel 1: Heatmap
pitch.kdeplot(yt['x'], yt['y'], ax=axes[0], fill=True, levels=50, thresh=0, cut=4, cmap='magma', alpha=0.7)
axes[0].set_title('Touch Heatmap', color='white', fontsize=14)

# Panel 2: Progressive Passes
if len(ypp)>0:
    pitch.arrows(ypp['x'], ypp['y'], ypp['pass_end_x'], ypp['pass_end_y'], width=2, headwidth=5, headlength=5, color='#ef3340', ax=axes[1], alpha=0.7)
axes[1].set_title(f'Progressive Passes (n={len(ypp)})', color='white', fontsize=14)

# Panel 3: Progressive Carries
if len(ypc)>0:
    pitch.arrows(ypc['x'], ypc['y'], ypc['carry_end_x'], ypc['carry_end_y'], width=2, headwidth=5, headlength=5, color='#fcca03', ax=axes[2], alpha=0.7)
axes[2].set_title(f'Progressive Carries (n={len(ypc)})', color='white', fontsize=14)

# Panel 4: Dribbles
if len(ydrib)>0:
    succ = ydrib[ydrib['dribble_outcome']=='Complete']
    fail = ydrib[ydrib['dribble_outcome']!='Complete']
    pitch.scatter(succ['x'], succ['y'], color='#00b894', s=80, edgecolors='white', ax=axes[3], zorder=2, label='Success')
    pitch.scatter(fail['x'], fail['y'], color='#d63031', s=80, edgecolors='white', ax=axes[3], zorder=2, marker='x', label='Failed')
    axes[3].legend(loc='lower right', facecolor='#0e1117', labelcolor='white', fontsize=9)
axes[3].set_title(f'Take-ons ({len(ydrib[ydrib["dribble_outcome"]=="Complete"])}/{len(ydrib)})', color='white', fontsize=14)

yshots = yamal[yamal['type']=='Shot']; yxg = pd.to_numeric(yshots['shot_statsbomb_xg'], errors='coerce').sum()
ygoals = len(yshots[yshots['shot_outcome']=='Goal'])
fig.suptitle(f'Lamine Yamal - Euro 2024 Complete Profile (xG: {yxg:.2f}, Goals: {ygoals})', color='white', fontsize=20, fontweight='bold', y=1.05)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz63_yamal_deep_dive.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz63_yamal_deep_dive")

# ── 2. NICO WILLIAMS DEEP DIVE (4-panel) ──
nico_name = [n for n in actual if 'nico' in str(n).lower() or 'williams' in str(n).lower()][0]
nico = s24[s24['common_name']==nico_name]
nt = nico[nico['type'].isin(['Pass','Carry','Dribble'])].dropna(subset=['x','y'])
npp = nico[nico['is_progressive_pass']==True].dropna(subset=['x','y','pass_end_x','pass_end_y'])
npc = nico[nico['is_progressive_carry']==True].dropna(subset=['x','y','carry_end_x','carry_end_y'])
ndrib = nico[nico['type']=='Dribble'].dropna(subset=['x','y'])

fig, axes = plt.subplots(1, 4, figsize=(28,7), facecolor='#0e1117')
for ax in axes:
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc'); pitch.draw(ax=ax)

pitch.kdeplot(nt['x'], nt['y'], ax=axes[0], fill=True, levels=50, thresh=0, cut=4, cmap='magma', alpha=0.7)
axes[0].set_title('Touch Heatmap', color='white', fontsize=14)

if len(npp)>0:
    pitch.arrows(npp['x'], npp['y'], npp['pass_end_x'], npp['pass_end_y'], width=2, headwidth=5, headlength=5, color='#ef3340', ax=axes[1], alpha=0.7)
axes[1].set_title(f'Progressive Passes (n={len(npp)})', color='white', fontsize=14)

if len(npc)>0:
    pitch.arrows(npc['x'], npc['y'], npc['carry_end_x'], npc['carry_end_y'], width=2, headwidth=5, headlength=5, color='#fcca03', ax=axes[2], alpha=0.7)
axes[2].set_title(f'Progressive Carries (n={len(npc)})', color='white', fontsize=14)

if len(ndrib)>0:
    succ = ndrib[ndrib['dribble_outcome']=='Complete']
    fail = ndrib[ndrib['dribble_outcome']!='Complete']
    pitch.scatter(succ['x'], succ['y'], color='#00b894', s=80, edgecolors='white', ax=axes[3], zorder=2)
    pitch.scatter(fail['x'], fail['y'], color='#d63031', s=80, edgecolors='white', ax=axes[3], zorder=2, marker='x')
axes[3].set_title(f'Take-ons ({len(ndrib[ndrib["dribble_outcome"]=="Complete"])}/{len(ndrib)})', color='white', fontsize=14)

nshots = nico[nico['type']=='Shot']; nxg = pd.to_numeric(nshots['shot_statsbomb_xg'], errors='coerce').sum()
ngoals = len(nshots[nshots['shot_outcome']=='Goal'])
fig.suptitle(f'Nico Williams - Euro 2024 Complete Profile (xG: {nxg:.2f}, Goals: {ngoals})', color='white', fontsize=20, fontweight='bold', y=1.05)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz64_nico_deep_dive.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz64_nico_deep_dive")

# ── 3. PENETRATION RANKING (All players, 2024) ──
prog_p = s24[s24['is_progressive_pass']==True]['common_name'].fillna(s24['player']).value_counts()
prog_c = s24[s24['is_progressive_carry']==True]['common_name'].fillna(s24['player']).value_counts()
pen = pd.DataFrame({'Prog Passes': prog_p, 'Prog Carries': prog_c}).fillna(0)
pen['Total'] = pen['Prog Passes'] + pen['Prog Carries']
pen = pen.sort_values('Total', ascending=True).tail(12)

fig, ax = plt.subplots(figsize=(10,8), facecolor='#0e1117'); ax.set_facecolor('#0e1117')
ax.barh(pen.index, pen['Prog Passes'], color='#ef3340', label='Progressive Passes')
ax.barh(pen.index, pen['Prog Carries'], left=pen['Prog Passes'], color='#fcca03', label='Progressive Carries')
ax.set_title('Euro 2024 Penetration Ranking\n(Progressive Passes + Carries)', color='white', fontsize=16, fontweight='bold', pad=15)
ax.tick_params(colors='white')
for s in ax.spines.values(): s.set_color('white')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.legend(facecolor='#0e1117', labelcolor='white')
plt.savefig('../outputs/figures/2024/viz65_penetration_2024.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz65_penetration_2024")

# ── 4. SIDE-BY-SIDE PENETRATION 2022 vs 2024 ──
prog_p22 = s22[s22['is_progressive_pass']==True]['common_name'].fillna(s22['player']).value_counts()
prog_c22 = s22[s22['is_progressive_carry']==True]['common_name'].fillna(s22['player']).value_counts()
pen22 = pd.DataFrame({'Prog Passes': prog_p22, 'Prog Carries': prog_c22}).fillna(0)
pen22['Total'] = pen22['Prog Passes'] + pen22['Prog Carries']

fig, axes = plt.subplots(1, 2, figsize=(20,8), facecolor='#0e1117')
for i, (tag, pdata) in enumerate([('WC 2022', pen22.sort_values('Total',ascending=True).tail(10)), ('EURO 2024', pen.tail(10))]):
    ax = axes[i]; ax.set_facecolor('#0e1117')
    ax.barh(pdata.index, pdata['Prog Passes'], color='#ef3340', label='Passes')
    ax.barh(pdata.index, pdata['Prog Carries'], left=pdata['Prog Passes'], color='#fcca03', label='Carries')
    ax.set_title(f'{tag} - Top Penetration Threats', color='white', fontsize=16, fontweight='bold')
    ax.tick_params(colors='white')
    for s in ax.spines.values(): s.set_color('white')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(facecolor='#0e1117', labelcolor='white', fontsize=9)
fig.suptitle('Who Drove the Attack? 2022 vs 2024', color='white', fontsize=20, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz66_penetration_comparison.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz66_penetration_comparison")

# ── 5. PRINT FINAL VERDICT ──
print("\n" + "="*60)
print("WHO MOST EXPLAINS SPAIN'S 2024 TRANSFORMATION (RANKED)")
print("="*60)

# Calculate each player's share of total progressive actions
total_prog_24 = len(s24[s24['is_progressive_pass']==True]) + len(s24[s24['is_progressive_carry']==True])
for player in pen.sort_values('Total', ascending=False).head(8).index:
    share = pen.loc[player, 'Total'] / total_prog_24 * 100
    pev = s24[s24['common_name']==player]
    shots = pev[pev['type']=='Shot']
    xg = pd.to_numeric(shots['shot_statsbomb_xg'], errors='coerce').sum()
    goals = len(shots[shots['shot_outcome']=='Goal'])
    drib = pev[pev['type']=='Dribble']
    drib_s = len(drib[drib['dribble_outcome']=='Complete'])
    print(f"  {player:<25} Prog: {int(pen.loc[player,'Total']):>3} ({share:.1f}% of team) | xG: {xg:.2f} | Goals: {goals} | Dribbles: {drib_s}")

print("\n[DONE] NB08b complete.")
