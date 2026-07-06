"""NB08a: Euro 2024 Player Profiles + Returning Player Comparisons"""
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
n22, n24 = s22['match_id'].nunique(), s24['match_id'].nunique()

# ── 1. IDENTIFY KEY PLAYERS BY TOUCHES ──
touches24 = s24[s24['type'].isin(['Pass','Carry','Shot','Ball Recovery','Dribble'])]
touches24_names = touches24['common_name'].fillna(touches24['player'])
tc = touches24_names.value_counts()
print("="*60)
print("EURO 2024 - TOP PLAYERS BY TOUCHES")
print("="*60)
for name, cnt in tc.head(15).items():
    print(f"  {name:<30} {cnt:>5} touches")
# Exclude GK
top = [n for n in tc.index if 'Sim' not in str(n)][:10]
print(f"\nSelected cohort: {top}")

# ── 2. FULL PLAYER PROFILE CARDS (10 players, 2 rows of 5) ──
fig, axes = plt.subplots(2, 5, figsize=(28,12), facecolor='#0e1117')
for idx, player in enumerate(top):
    r, c = idx//5, idx%5; ax = axes[r][c]
    pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
    pitch.draw(ax=ax)
    pev = s24[s24['common_name']==player]
    t = pev[pev['type'].isin(['Pass','Carry','Ball Recovery','Dribble'])].dropna(subset=['x','y'])
    if len(t)>5:
        pitch.kdeplot(t['x'], t['y'], ax=ax, fill=True, levels=50, thresh=0, cut=4, cmap='magma', alpha=0.7)
    # Stats
    passes = pev[pev['type']=='Pass']
    cmp = (passes['pass_outcome'].isna().sum()/max(1,len(passes)))*100
    pp = len(pev[pev['is_progressive_pass']==True])
    pc = len(pev[pev['is_progressive_carry']==True])
    fwd = pev[pev['type']=='Pass']['is_forward_pass'].mean()*100 if len(passes)>0 else 0
    shots = pev[pev['type']=='Shot']
    xg = pd.to_numeric(shots['shot_statsbomb_xg'], errors='coerce').sum()
    goals = len(shots[shots['shot_outcome']=='Goal'])
    defs = len(pev[pev['type'].isin(['Ball Recovery','Interception','Tackle','Block','Pressure'])])
    dribbles = pev[pev['type']=='Dribble']
    drib_success = len(dribbles[dribbles['dribble_outcome']=='Complete']) if len(dribbles)>0 else 0

    props = dict(boxstyle='round', facecolor='black', alpha=0.75, edgecolor='none')
    stat = f"Pass: {cmp:.0f}% | Fwd: {fwd:.0f}%\nProg: {pp+pc} | Def: {defs}\nxG: {xg:.1f} | G: {goals} | Drib: {drib_success}"
    ax.text(0.03, 0.97, stat, transform=ax.transAxes, fontsize=8, color='white', va='top', bbox=props, family='monospace')
    short = str(player).split()[-1] if len(str(player).split())>2 else str(player)
    ax.set_title(short, color='white', fontsize=14, fontweight='bold', pad=8)

fig.suptitle('Spain Euro 2024 - Complete Player Profile Cards', color='white', fontsize=24, fontweight='bold', y=1.04)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz61_player_profiles_2024.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz61_player_profiles_2024")

# ── 3. RETURNING PLAYER COMPARISONS (Rodri, Pedri, Dani Olmo) ──
returning = ['Rodri', 'Pedri', 'Dani Olmo']
fig, axes = plt.subplots(3, 2, figsize=(16, 20), facecolor='#0e1117')
for i, player in enumerate(returning):
    for j, (tag, sdf) in enumerate([('WC 2022', s22), ('EURO 2024', s24)]):
        ax = axes[i][j]
        pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
        pitch.draw(ax=ax)
        pev = sdf[sdf['common_name']==player]
        t = pev[pev['type'].isin(['Pass','Carry','Ball Recovery','Dribble'])].dropna(subset=['x','y'])
        if len(t)>5:
            pitch.kdeplot(t['x'], t['y'], ax=ax, fill=True, levels=50, thresh=0, cut=4, cmap='magma', alpha=0.7)
        # Stats
        passes = pev[pev['type']=='Pass']
        cmp = (passes['pass_outcome'].isna().sum()/max(1,len(passes)))*100
        pp = len(pev[pev['is_progressive_pass']==True])
        pc = len(pev[pev['is_progressive_carry']==True])
        nm = sdf['match_id'].nunique()
        props = dict(boxstyle='round', facecolor='black', alpha=0.7, edgecolor='none')
        ax.text(0.03, 0.97, f"Pass: {cmp:.0f}% | Prog: {pp+pc}\n/match: {(pp+pc)/nm:.1f}", transform=ax.transAxes, fontsize=10, color='white', va='top', bbox=props)
        ax.set_title(f"{player} - {tag}", color='white', fontsize=14, fontweight='bold', pad=8)

fig.suptitle('Returning Players: 2022 vs 2024 Heatmap Comparison', color='white', fontsize=22, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz62_returning_players.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz62_returning_players")

# ── 4. PRINT DETAILED RETURNING PLAYER STATS ──
print("\n" + "="*60)
print("RETURNING PLAYER COMPARISON (Per Match)")
print("="*60)
for player in returning:
    print(f"\n--- {player} ---")
    for tag, sdf in [('2022', s22), ('2024', s24)]:
        pev = sdf[sdf['common_name']==player]
        nm = sdf['match_id'].nunique()
        passes = pev[pev['type']=='Pass']
        cmp = (passes['pass_outcome'].isna().sum()/max(1,len(passes)))*100
        pp = len(pev[pev['is_progressive_pass']==True])
        pc = len(pev[pev['is_progressive_carry']==True])
        fwd = pev[pev['type']=='Pass']['is_forward_pass'].mean()*100 if len(passes)>0 else 0
        defs = len(pev[pev['type'].isin(['Ball Recovery','Interception','Tackle','Block','Pressure'])])
        print(f"  {tag}: Passes={len(passes)/nm:.0f}/m  Cmp={cmp:.0f}%  Fwd={fwd:.0f}%  Prog={pp+pc} ({(pp+pc)/nm:.1f}/m)  Def={defs/nm:.1f}/m")

print("\n[DONE] NB08a complete.")
