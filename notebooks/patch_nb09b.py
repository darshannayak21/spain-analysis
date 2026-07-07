import json

def format_source(text):
    lines = text.split('\n')
    return [line + '\n' for line in lines[:-1]] + [lines[-1]]

with open('09b_georgia_case_study.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_part_2_code = """defensive_actions = ['Pressure', 'Tackle', 'Interception', 'Block', 'Foul Committed', 'Clearance']

# GEORGIA CALCULATIONS
geo_def = georgia_match[georgia_match['type'].isin(defensive_actions)]
geo_avg_height = geo_def['x'].mean()

# FIX 1: Correct PPDA (All Spain passes / Georgia high defensive actions)
spain_passes = spain_match[spain_match['type'] == 'Pass']
geo_def_high = geo_def[geo_def['x'] >= 40]
ppda_geo = len(spain_passes) / len(geo_def_high) if len(geo_def_high) > 0 else 0

# FIX 3: Low block %
geo_def_low = geo_def[geo_def['x'] < 40]
geo_low_block_pct = (len(geo_def_low) / len(geo_def)) * 100 if len(geo_def) > 0 else 0

# MOROCCO CALCULATIONS (Match ID 3869220)
morocco_match = df[(df['match_id'] == 3869220) & (df['team'] == 'Morocco')]
spain_vs_mor_match = df[(df['match_id'] == 3869220) & (df['team'] == 'Spain')]

mor_def = morocco_match[morocco_match['type'].isin(defensive_actions)]
mor_avg_height = mor_def['x'].mean()
spain_vs_mor_passes = spain_vs_mor_match[spain_vs_mor_match['type'] == 'Pass']
mor_def_high = mor_def[mor_def['x'] >= 40]
ppda_mor = len(spain_vs_mor_passes) / len(mor_def_high) if len(mor_def_high) > 0 else 0

mor_def_low = mor_def[mor_def['x'] < 40]
mor_low_block_pct = (len(mor_def_low) / len(mor_def)) * 100 if len(mor_def) > 0 else 0

print("=== DEFENSIVE SETUP COMPARISON ===")
print(f"{str('Opponent').ljust(15)} | {str('Avg Def Height').ljust(15)} | {str('PPDA').ljust(10)} | {str('Def Actions <40').ljust(15)}")
print("-" * 65)
print(f"{str('Morocco (2022)').ljust(15)} | {f'{mor_avg_height:.1f} yards'.ljust(15)} | {f'{ppda_mor:.1f}'.ljust(10)} | {f'{mor_low_block_pct:.1f}%'.ljust(15)}")
print(f"{str('Georgia (2024)').ljust(15)} | {f'{geo_avg_height:.1f} yards'.ljust(15)} | {f'{ppda_geo:.1f}'.ljust(10)} | {f'{geo_low_block_pct:.1f}%'.ljust(15)}")"""

markdown_2b = """## Part 2b: Team Territorial Dominance
Comparing the overall spatial footprint of both teams. The heatmaps below show ALL events/touches for both sides, revealing the height and compactness of the defensive and offensive lines."""

code_2b = """fig, axs = plt.subplots(1, 2, figsize=(16, 10), facecolor=bg_color)
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color=bg_color, line_color='white', half=False)

# Left: Georgia full team touches
pitch.draw(ax=axs[0])
pitch.kdeplot(georgia_match['x'], georgia_match['y'], ax=axs[0], fill=True, cmap=cmap_def, alpha=0.8, levels=100)
axs[0].set_title("Georgia Team Touch Heatmap (Attacking Up)", color=text_color, fontsize=14)

# Right: Spain full team touches
pitch.draw(ax=axs[1])
pitch.kdeplot(spain_match['x'], spain_match['y'], ax=axs[1], fill=True, cmap=cmap_def, alpha=0.8, levels=100)
axs[1].set_title("Spain Team Touch Heatmap (Attacking Up)", color=text_color, fontsize=14)

viz_path = get_viz_filename('georgia_vs_spain_team_heatmaps')
plt.savefig(viz_path, dpi=300, bbox_inches='tight', facecolor=bg_color)
plt.show()"""

markdown_insight_2b = """**Insight:** Just like Morocco, Georgia exhibits a classic low block vs high line scenario. Georgia's entire spatial footprint is condensed deep in their own half, while Spain's touches push extremely high up the pitch, confirming that Georgia conceded territory entirely by design to deny space behind."""

part_2_code_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'geo_avg_height = geo_def' in ''.join(cell['source']):
        part_2_code_idx = i
        break

if part_2_code_idx != -1:
    nb['cells'][part_2_code_idx]['source'] = format_source(new_part_2_code)

    new_cells = [
        {"cell_type": "markdown", "metadata": {}, "source": format_source(markdown_2b)},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": format_source(code_2b)},
        {"cell_type": "markdown", "metadata": {}, "source": format_source(markdown_insight_2b)}
    ]
    
    for j, c in enumerate(new_cells):
        nb['cells'].insert(part_2_code_idx + 1 + j, c)

with open('09b_georgia_case_study.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
