with open('create_nb09b.py', 'r') as f:
    content = f.read()

bad_str = '"geo_x_aligned = 120 - geo_def[\'x\']\\n    geo_y_aligned = 80 - geo_def[\'y\']\\n    pitch.kdeplot(geo_x_aligned, geo_y_aligned, ax=axs[0], fill=True, cmap=cmap_def, alpha=0.8, levels=100)\\n",'
good_str = '    "geo_x_aligned = 120 - geo_def[\'x\']\\n",\n    "geo_y_aligned = 80 - geo_def[\'y\']\\n",\n    "pitch.kdeplot(geo_x_aligned, geo_y_aligned, ax=axs[0], fill=True, cmap=cmap_def, alpha=0.8, levels=100)\\n",'

content = content.replace(bad_str, good_str)

with open('create_nb09b.py', 'w') as f:
    f.write(content)
