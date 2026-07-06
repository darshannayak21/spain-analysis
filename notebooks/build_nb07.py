"""Generate and run NB07 Euro 2024 comprehensive analysis."""
import pandas as pd, numpy as np, os, sys, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patheffects as pe
from mplsoccer import Pitch, VerticalPitch
import warnings; warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
os.makedirs(os.path.join(ROOT, 'outputs', 'figures', '2024'), exist_ok=True)
sys.path.insert(0, ROOT)
from utils.config import OUTPUTS_DATA_DIR

os.chdir(BASE)
df = pd.read_parquet(os.path.join(OUTPUTS_DATA_DIR, 'master_events_cleaned.parquet'))
s24 = df[(df['tournament']=='EURO2024')&(df['team']=='Spain')].copy()
o24 = df[(df['tournament']=='EURO2024')&(df['team']!='Spain')].copy()
s22 = df[(df['tournament']=='WC2022')&(df['team']=='Spain')].copy()
o22 = df[(df['tournament']=='WC2022')&(df['team']!='Spain')].copy()
n22, n24 = s22['match_id'].nunique(), s24['match_id'].nunique()
print(f"WC2022: {n22} matches | EURO2024: {n24} matches")

# ── 1. TERRITORY HEATMAP ──
for tag, sdf, fname in [('Spain Euro 2024', s24, 'viz50_territory_2024'),
                         ('Spain WC 2022', s22, 'viz50_territory_2022')]:
    t = sdf[sdf['type'].isin(['Pass','Carry','Dribble'])].dropna(subset=['x','y'])
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
    fig, ax = pitch.draw(figsize=(12,8)); fig.set_facecolor('#0e1117')
    pitch.kdeplot(t['x'], t['y'], ax=ax, fill=True, levels=100, thresh=0, cut=4, cmap='magma', alpha=0.7)
    ax.set_title(f'{tag} — Territory Heatmap', color='white', fontsize=18, fontweight='bold', pad=15)
    plt.savefig(f'../outputs/figures/2024/{fname}.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
    plt.close(); print(f"  Saved {fname}")

# ── 2. PASSING NETWORK ──
def draw_pass_network(sdf, title, fname):
    starters = sdf['common_name'].fillna(sdf['player']).value_counts().head(11).index.tolist()
    passes = sdf[(sdf['type']=='Pass')&(sdf['pass_outcome'].isna())].copy()
    passes['p'] = passes['common_name'].fillna(passes['player'])
    passes['r'] = passes['pass_recipient'].map(lambda x: sdf[sdf['player']==x]['common_name'].iloc[0] if len(sdf[sdf['player']==x])>0 and pd.notna(sdf[sdf['player']==x]['common_name'].iloc[0]) else x)
    passes = passes[passes['p'].isin(starters)&passes['r'].isin(starters)]
    avg = passes.groupby('p').agg(x=('x','mean'),y=('y','mean'),cnt=('x','count'))
    combos = passes.groupby(['p','r']).size().reset_index(name='n')
    combos = combos[(combos['n']>3)&combos['p'].isin(avg.index)&combos['r'].isin(avg.index)]
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
    fig, ax = pitch.draw(figsize=(12,8)); fig.set_facecolor('#0e1117')
    for _, r in combos.iterrows():
        if r['p'] in avg.index and r['r'] in avg.index:
            pitch.lines(avg.loc[r['p'],'x'], avg.loc[r['p'],'y'], avg.loc[r['r'],'x'], avg.loc[r['r'],'y'], ax=ax, color='white', lw=r['n']/4, alpha=0.6, zorder=1)
    pitch.scatter(avg['x'], avg['y'], s=800, color='#ef3340', edgecolors='white', lw=2, ax=ax, zorder=2)
    for name, r in avg.iterrows():
        label = str(name).split()[-1] if len(str(name).split())>1 else str(name)
        ax.annotate(label, (r['x'], r['y']-3.5), color='white', ha='center', fontsize=11, fontweight='bold', zorder=3, path_effects=[pe.withStroke(linewidth=3, foreground='black')])
    ax.set_title(title, color='white', fontsize=18, fontweight='bold', pad=15)
    plt.savefig(f'../outputs/figures/2024/{fname}.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
    plt.close(); print(f"  Saved {fname}")

draw_pass_network(s24, 'Spain Euro 2024 — Passing Network', 'viz51_pass_network_2024')

# ── 3. SHOT MAP + GOAL LOCATIONS ──
shots24 = s24[s24['type']=='Shot'].dropna(subset=['x','y']).copy()
shots24['xg'] = pd.to_numeric(shots24['shot_statsbomb_xg'], errors='coerce')
goals24 = shots24[shots24['shot_outcome']=='Goal']

pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(12,8)); fig.set_facecolor('#0e1117')
sc = pitch.scatter(shots24['x'], shots24['y'], s=shots24['xg']*500+20, color='#636e72', alpha=0.5, edgecolors='white', ax=ax, zorder=1)
pitch.scatter(goals24['x'], goals24['y'], s=goals24['xg']*500+50, color='#ef3340', edgecolors='gold', lw=2, ax=ax, zorder=2, marker='*')
for _, g in goals24.iterrows():
    nm = g['common_name'] if pd.notna(g['common_name']) else str(g['player']).split()[-1]
    ax.annotate(f"{nm} {int(g['minute'])}'", (g['x'], g['y']+3), color='gold', ha='center', fontsize=9, fontweight='bold', path_effects=[pe.withStroke(linewidth=2, foreground='black')], zorder=3)
ax.set_title(f"Spain Euro 2024 — Shot Map ({len(shots24)} shots, {len(goals24)} goals, {shots24['xg'].sum():.1f} xG)", color='white', fontsize=18, fontweight='bold', pad=15)
plt.savefig('../outputs/figures/2024/viz52_shot_map_2024.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz52_shot_map_2024")

# ── 4. KEY PLAYER HEATMAPS ──
key_players = ['Lamine Yamal','Nico Williams','Rodri','Pedri','Dani Olmo','Fabian Ruiz','Morata','Cucurella']
# Map to common_name values in dataset
name_map = {'Fabian Ruiz': 'Fabián Ruiz'}
actual_names = s24['common_name'].dropna().unique().tolist()

rows, cols = 2, 4
fig, axes = plt.subplots(rows, cols, figsize=(22,11), facecolor='#0e1117')
for idx, player in enumerate(key_players):
    r, c = idx//cols, idx%cols; ax = axes[r][c]
    pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
    pitch.draw(ax=ax)
    # Find matching name
    matched = [n for n in actual_names if player.lower() in str(n).lower()]
    pname = matched[0] if matched else player
    pev = s24[s24['common_name']==pname]
    touches = pev[pev['type'].isin(['Pass','Carry','Ball Recovery','Dribble'])].dropna(subset=['x','y'])
    if len(touches)>5:
        pitch.kdeplot(touches['x'], touches['y'], ax=ax, fill=True, levels=50, thresh=0, cut=4, cmap='magma', alpha=0.7)
    # Stats
    pp = len(pev[pev['is_progressive_pass']==True])
    pc = len(pev[pev['is_progressive_carry']==True])
    pshots = pev[pev['type']=='Shot']
    xg = pd.to_numeric(pshots['shot_statsbomb_xg'], errors='coerce').sum()
    goals = len(pshots[pshots['shot_outcome']=='Goal']) if len(pshots)>0 else 0
    props = dict(boxstyle='round', facecolor='black', alpha=0.7, edgecolor='none')
    stat = f"Prog: {pp+pc} | xG: {xg:.1f} | G: {goals}"
    ax.text(0.05, 0.95, stat, transform=ax.transAxes, fontsize=9, color='white', va='top', bbox=props)
    ax.set_title(pname, color='white', fontsize=14, fontweight='bold', pad=8)

fig.suptitle('Spain Euro 2024 — Key Player Heatmaps', color='white', fontsize=22, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz53_player_heatmaps_2024.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz53_player_heatmaps_2024")

# ── 5. PROGRESSIVE PASSES MAP ──
pp24 = s24[s24['is_progressive_pass']==True].dropna(subset=['x','y','pass_end_x','pass_end_y'])
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(12,8)); fig.set_facecolor('#0e1117')
pitch.arrows(pp24['x'], pp24['y'], pp24['pass_end_x'], pp24['pass_end_y'], width=1.5, headwidth=5, headlength=5, color='#ef3340', ax=ax, alpha=0.4)
ax.set_title(f"Spain Euro 2024 — Progressive Passes (n={len(pp24)})", color='white', fontsize=18, fontweight='bold', pad=15)
plt.savefig('../outputs/figures/2024/viz54_progressive_passes_2024.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz54_progressive_passes_2024")

# ── 6. PROGRESSIVE CARRIES MAP ──
pc24 = s24[s24['is_progressive_carry']==True].dropna(subset=['x','y','carry_end_x','carry_end_y'])
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(12,8)); fig.set_facecolor('#0e1117')
pitch.arrows(pc24['x'], pc24['y'], pc24['carry_end_x'], pc24['carry_end_y'], width=2, headwidth=5, headlength=5, color='#fcca03', ax=ax, alpha=0.5)
ax.set_title(f"Spain Euro 2024 — Progressive Carries (n={len(pc24)})", color='white', fontsize=18, fontweight='bold', pad=15)
plt.savefig('../outputs/figures/2024/viz55_progressive_carries_2024.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz55_progressive_carries_2024")

# ── 7. PRESSURE HEATMAP ──
press24 = s24[s24['type']=='Pressure'].dropna(subset=['x','y'])
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(12,8)); fig.set_facecolor('#0e1117')
pitch.kdeplot(press24['x'], press24['y'], ax=ax, fill=True, levels=100, thresh=0, cut=4, cmap='hot', alpha=0.7)
ax.set_title(f"Spain Euro 2024 — Pressing Heatmap (n={len(press24)})", color='white', fontsize=18, fontweight='bold', pad=15)
plt.savefig('../outputs/figures/2024/viz56_pressure_2024.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz56_pressure_2024")

# ── 8. LAMINE YAMAL SPECIAL ──
yamal_name = [n for n in actual_names if 'yamal' in str(n).lower()][0]
yamal = s24[s24['common_name']==yamal_name]
yt = yamal[yamal['type'].isin(['Pass','Carry','Dribble'])].dropna(subset=['x','y'])
ypp = yamal[(yamal['is_progressive_pass']==True)].dropna(subset=['x','y','pass_end_x','pass_end_y'])
ypc = yamal[(yamal['is_progressive_carry']==True)].dropna(subset=['x','y','carry_end_x','carry_end_y'])

fig, axes = plt.subplots(1, 3, figsize=(20,7), facecolor='#0e1117')
# Heatmap
pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#c7d5cc')
pitch.draw(ax=axes[0])
pitch.kdeplot(yt['x'], yt['y'], ax=axes[0], fill=True, levels=50, thresh=0, cut=4, cmap='magma', alpha=0.7)
axes[0].set_title('Touch Heatmap', color='white', fontsize=14)
# Progressive passes
pitch.draw(ax=axes[1])
if len(ypp)>0:
    pitch.arrows(ypp['x'], ypp['y'], ypp['pass_end_x'], ypp['pass_end_y'], width=2, headwidth=5, headlength=5, color='#ef3340', ax=axes[1], alpha=0.7)
axes[1].set_title(f'Progressive Passes (n={len(ypp)})', color='white', fontsize=14)
# Progressive carries
pitch.draw(ax=axes[2])
if len(ypc)>0:
    pitch.arrows(ypc['x'], ypc['y'], ypc['carry_end_x'], ypc['carry_end_y'], width=2, headwidth=5, headlength=5, color='#fcca03', ax=axes[2], alpha=0.7)
axes[2].set_title(f'Progressive Carries (n={len(ypc)})', color='white', fontsize=14)

yshots = yamal[yamal['type']=='Shot']
yxg = pd.to_numeric(yshots['shot_statsbomb_xg'], errors='coerce').sum()
ygoals = len(yshots[yshots['shot_outcome']=='Goal'])
fig.suptitle(f'Lamine Yamal — Euro 2024 Deep Dive (xG: {yxg:.2f}, Goals: {ygoals})', color='white', fontsize=20, fontweight='bold', y=1.05)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz57_yamal_special.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz57_yamal_special")

# ── 9. xG CUMULATIVE RACE CHART ──
def xg_race(sdf):
    ms = sorted(sdf['match_id'].unique())
    cum, nums = [], []
    rx = 0
    for i, mid in enumerate(ms):
        sh = sdf[(sdf['match_id']==mid)&(sdf['type']=='Shot')]
        rx += pd.to_numeric(sh['shot_statsbomb_xg'], errors='coerce').sum()
        cum.append(rx); nums.append(i+1)
    return nums, cum

x22, y22 = xg_race(s22); x24, y24 = xg_race(s24)
fig, ax = plt.subplots(figsize=(10,6), facecolor='#0e1117'); ax.set_facecolor('#0e1117')
ax.plot(x22, y22, 'o-', color='#636e72', lw=3, label=f'WC 2022 ({n22} matches)')
ax.plot(x24, y24, 'o-', color='#ef3340', lw=3, label=f'EURO 2024 ({n24} matches)')
ax.set_title('Cumulative xG Generation', color='white', fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel('Match Number', color='white'); ax.set_ylabel('Cumulative xG', color='white')
ax.tick_params(colors='white')
for s in ax.spines.values(): s.set_color('white')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.legend(facecolor='#0e1117', labelcolor='white')
plt.savefig('../outputs/figures/2024/viz58_xg_race.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz58_xg_race")

# ── 10. MASTER COMPARISON TABLE ──
def metrics(sdf, odf, nm):
    m = {}
    tp = len(sdf[sdf['type']=='Pass']); op = len(odf[odf['type']=='Pass'])
    m['Possession %'] = tp/(tp+op)*100
    m['Passes/match'] = tp/nm
    m['Forward Pass %'] = sdf[sdf['type']=='Pass']['is_forward_pass'].mean()*100
    m['Prog Passes/match'] = len(sdf[sdf['is_progressive_pass']==True])/nm
    m['Prog Carries/match'] = len(sdf[sdf['is_progressive_carry']==True])/nm
    da = sdf[sdf['type'].isin(['Tackle','Interception','Foul Committed','Block'])]; hda = da[da['x']>=40]
    m['PPDA'] = op/max(1,len(hda))
    rec = sdf[sdf['type']=='Ball Recovery'].dropna(subset=['x']); m['High Recoveries/match'] = len(rec[rec['x']>=60])/nm
    ft = sdf[sdf['type'].isin(['Pass','Carry'])].dropna(subset=['x','pass_end_x','carry_end_x'], how='all').copy()
    ft['ex'] = ft['pass_end_x'].fillna(ft['carry_end_x']); ft['ey'] = ft['pass_end_y'].fillna(ft['carry_end_y'])
    f3 = ft[(ft['x']<80)&(ft['ex']>=80)]
    m['F3 Entries/match'] = len(f3)/nm
    m['F3 Wide %'] = len(f3[(f3['ey']<18)|(f3['ey']>62)])/max(1,len(f3))*100
    m['F3 Central %'] = len(f3[(f3['ey']>=30)&(f3['ey']<=50)])/max(1,len(f3))*100
    sh = sdf[sdf['type']=='Shot']; xg = pd.to_numeric(sh['shot_statsbomb_xg'], errors='coerce').sum()
    m['Shots/match'] = len(sh)/nm; m['xG/match'] = xg/nm; m['xG/shot'] = xg/max(1,len(sh))
    m['Goals/match'] = len(sh[sh['shot_outcome']=='Goal'])/nm
    return m

m22 = metrics(s22, o22, n22); m24 = metrics(s24, o24, n24)
comp = pd.DataFrame({'WC 2022': m22, 'EURO 2024': m24})
comp['% Change'] = ((comp['EURO 2024']-comp['WC 2022'])/comp['WC 2022'])*100
comp.to_csv('../outputs/figures/2024/master_comparison.csv')
print("\n" + "="*60)
print("MASTER COMPARISON TABLE"); print("="*60)
for idx, row in comp.iterrows():
    d = row['% Change']; arrow = "UP" if d>5 else "DOWN" if d<-5 else "--"
    print(f"  {idx:<25} 2022: {row['WC 2022']:>8.2f}  2024: {row['EURO 2024']:>8.2f}  {arrow} {d:>+.1f}%")
print("="*60)

# ── 11. GROUPED BAR COMPARISON ──
keys = ['Passes/match','Forward Pass %','Prog Carries/match','xG/match','Goals/match','F3 Wide %']
fig, axes = plt.subplots(2, 3, figsize=(18,10), facecolor='#0e1117')
for i, k in enumerate(keys):
    ax = axes[i//3][i%3]; ax.set_facecolor('#0e1117')
    v22, v24 = comp.loc[k,'WC 2022'], comp.loc[k,'EURO 2024']
    bars = ax.bar(['WC 2022','EURO 2024'], [v22, v24], color=['#636e72','#ef3340'], width=0.5)
    ax.set_title(k, color='white', fontsize=14, fontweight='bold')
    ax.tick_params(colors='white')
    for s in ax.spines.values(): s.set_color('gray')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    for bar, val in zip(bars, [v22, v24]):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()*0.5, f"{val:.1f}", ha='center', color='white', fontweight='bold', fontsize=14)
fig.suptitle('Spain Tactical Evolution — 2022 vs 2024', color='white', fontsize=22, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz59_master_comparison.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz59_master_comparison")

# ── 12. F3 ENTRY ZONE COMPARISON ──
fig, axes = plt.subplots(1, 2, figsize=(16,6), facecolor='#0e1117')
for i, (tag, sdf, ax) in enumerate([('WC 2022', s22, axes[0]), ('EURO 2024', s24, axes[1])]):
    ax.set_facecolor('#0e1117')
    ft = sdf[sdf['type'].isin(['Pass','Carry'])].dropna(subset=['x','pass_end_x','carry_end_x'], how='all').copy()
    ft['ex'] = ft['pass_end_x'].fillna(ft['carry_end_x']); ft['ey'] = ft['pass_end_y'].fillna(ft['carry_end_y'])
    f3 = ft[(ft['x']<80)&(ft['ex']>=80)]
    wide = len(f3[(f3['ey']<18)|(f3['ey']>62)]); central = len(f3[(f3['ey']>=30)&(f3['ey']<=50)])
    half = len(f3)-wide-central
    bars = ax.bar(['Wide','Half-space','Central'], [wide, half, central], color=['#ef3340','#fcca03','#00b894'])
    ax.set_title(f'{tag} F3 Entries', color='white', fontsize=16, fontweight='bold')
    ax.tick_params(colors='white')
    for s in ax.spines.values(): s.set_color('gray')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    for bar in bars:
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2, str(int(bar.get_height())), ha='center', color='white', fontsize=14, fontweight='bold')
fig.suptitle('Final Third Entry Zones — Where Did Spain Attack?', color='white', fontsize=20, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz60_f3_entry_zones.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close(); print("  Saved viz60_f3_entry_zones")

print("\n✅ ALL 12 VISUALIZATIONS GENERATED SUCCESSFULLY.")
