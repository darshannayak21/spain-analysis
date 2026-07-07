import json
import os

nb_path = 'notebooks/05_morocco_case_study.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        source = "".join(cell.get('source', []))
        if 'pitch.kdeplot(m_def[\'x\'], m_def[\'y\']' in source:
            # Replace the plotting block
            new_source = source.replace(
                "pitch.kdeplot(m_def['x'], m_def['y'], ax=axes[0]",
                "# Invert Morocco's coordinates to match Spain's attacking perspective\n"
                "m_def_x_inv = 120 - m_def['x']\n"
                "m_def_y_inv = 80 - m_def['y']\n\n"
                "pitch.kdeplot(m_def_x_inv, m_def_y_inv, ax=axes[0]"
            )
            new_source = new_source.replace(
                "pitch.kdeplot(m_def['x'], m_def['y'], ax=axes[1]",
                "pitch.kdeplot(m_def_x_inv, m_def_y_inv, ax=axes[1]"
            )
            
            # Split back into lines for JSON
            lines = [line + '\\n' for line in new_source.split('\\n')]
            lines[-1] = lines[-1].rstrip('\\n')
            cell['source'] = lines

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook patched successfully.")
