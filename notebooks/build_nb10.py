import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Create outputs dir
os.makedirs('../outputs/figures/2024', exist_ok=True)

def load_img(path):
    try:
        return mpimg.imread(path)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None

# ==========================================
# Composite 1: Threat Distribution (Network vs Goals)
# ==========================================
print("Generating Composite 2: Threat Distribution...")
fig, axs = plt.subplots(2, 2, figsize=(20, 16))
fig.patch.set_facecolor('#0e1117')

img_net_22 = load_img('../outputs/figures/2022/viz03_pass_network_all.png')
img_net_24 = load_img('../outputs/figures/2024/viz51_pass_network_2024.png')
img_goals = load_img('../outputs/figures/2024/viz75_goal_concentration.png')

if img_net_22 is not None:
    axs[0, 0].imshow(img_net_22)
if img_net_24 is not None:
    axs[0, 1].imshow(img_net_24)
if img_goals is not None:
    # img_goals is already a 1x2 side-by-side.
    axs[1, 0].imshow(img_goals)
    # Hide the second axis on the bottom row since the goal image spans both conceptually,
    # or just plot it spanning both columns
    pass

for ax in axs.flatten():
    ax.axis('off')

# Make the bottom row a single subplot for the wide goal image
axs[1, 0].remove()
axs[1, 1].remove()
ax_bottom = fig.add_subplot(2, 1, 2)
if img_goals is not None:
    ax_bottom.imshow(img_goals)
ax_bottom.axis('off')
ax_bottom.set_title("Goal Threat Concentration Comparison", color='white', fontsize=20, pad=10, fontweight='bold')

plt.tight_layout()
plt.savefig('../outputs/figures/2024/viz80_threat_distribution.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

# ==========================================
# Composite 2: Hero Causal Chart
# ==========================================
print("Generating Composite 1: Hero Visualization...")

fig = plt.figure(figsize=(20, 24))
fig.patch.set_facecolor('#0e1117')

img_ter = load_img('../outputs/figures/2024/viz50_territory_comparison.png')
img_pen = load_img('../outputs/figures/2024/viz66_penetration_comparison.png')
img_shift = load_img('../outputs/figures/2024/viz41_metric_shifts.png') # Or master comparison

# 3 rows, 1 col
ax1 = fig.add_subplot(3, 1, 1)
if img_ter is not None: ax1.imshow(img_ter)
ax1.axis('off')
ax1.set_title("1. Territory Shift (Less Sterile Possession, More Danger)", color='white', fontsize=24, fontweight='bold', pad=15)

ax2 = fig.add_subplot(3, 1, 2)
if img_pen is not None: ax2.imshow(img_pen)
ax2.axis('off')
ax2.set_title("2. Penetration Shift (Wider, Faster, More Direct)", color='white', fontsize=24, fontweight='bold', pad=15)

ax3 = fig.add_subplot(3, 1, 3)
if img_shift is not None: ax3.imshow(img_shift)
ax3.axis('off')
ax3.set_title("3. The Statistical Confirmation", color='white', fontsize=24, fontweight='bold', pad=15)

plt.tight_layout(pad=3.0)
plt.savefig('../outputs/figures/2024/viz81_hero_composite.png', dpi=200, bbox_inches='tight', facecolor='#0e1117')
plt.close()

print("Build complete.")
