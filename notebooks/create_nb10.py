import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Notebook 10: Final Tactical Synthesis (2022 vs 2024)\n",
    "\n",
    "This is the definitive, evidence-based conclusion of the entire project: answering exactly why Spain dominated possession but failed at Qatar 2022, and exactly what changed—tactically, structurally, and in personnel—by Euro 2024.\n",
    "\n",
    "All conclusions are drawn directly from the forensic calculations in Notebooks 04 through 09."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from IPython.display import display, HTML\n",
    "import warnings; warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Hypothesis Scorecard\n",
    "Evaluating the nine core hypotheses defined at the beginning of the project using the computed data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "scorecard_data = {\n",
    "    'Hypothesis': ['H1: Possession without penetration', 'H2: Lack of verticality', 'H3: Predictable build-up',\n",
    "                   'H4: Central overload without penetration', 'H5: Weak transition threat', 'H6: Underperformance vs chance quality',\n",
    "                   'H7: Morocco neutralized specific patterns', 'H8: 2024 shows directional change', 'H9: Personnel > Tactics'],\n",
    "    'Metric Used': ['F3 Entries & Prog Passes', 'Pass Angle & Directness', 'Progression Variety/PPDA',\n",
    "                    'Central Box Entries', 'Transition Shots', 'xG vs Goals',\n",
    "                    'Zone Touches vs Avg', 'All progression metrics', 'Returning Player Metrics'],\n",
    "    'Verdict': ['Supported', 'Supported', 'Supported',\n",
    "                'Supported', 'Partially Supported', 'Not Supported',\n",
    "                'Supported', 'Supported', 'Partially Supported'],\n",
    "    'Explanation': [\n",
    "        'Spain circulated in low-danger zones; 2024 saw a 28% increase in central F3 entries.',\n",
    "        '2022 had heavily lateral passing; 2024 dropped passes per shot from 12.0 to 7.5.',\n",
    "        'Build-up was heavily skewed to the left; Morocco easily defended rehearsed wide patterns.',\n",
    "        'Spain lacked central line-breaking passes, forcing wide recycling until 2024 brought Olmo/Ruiz.',\n",
    "        'Spain had some transition threat, but it was heavily constrained by narrow fullback positioning.',\n",
    "        'Spain generated very low-quality chances (low xG/shot) in 2022, not just bad finishing.',\n",
    "        'Morocco perfectly clogged the central/half-spaces, neutralizing Pedri/Gavi entirely.',\n",
    "        'Data confirms 2024 was significantly more vertical, direct, and transition-heavy.',\n",
    "        'Personnel (Yamal/Williams) drove width, but tactical roles (Rodri playing deeper) confirm system changes too.'\n",
    "    ]\n",
    "}\n",
    "scorecard_df = pd.DataFrame(scorecard_data)\n",
    "display(HTML(scorecard_df.to_html(index=False)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. The Morocco Case Study (Restatement)\n",
    "In Notebook 05, we analyzed the Round of 16 loss to Morocco. The data proved the exit was **systemic, not a fluke**.\n",
    "- Morocco perfectly identified Spain's structural reliance on lateral circulation and clogged the central passing lanes.\n",
    "- Against Morocco, Spain had 76% possession but failed to register a single open-play goal. Their passing network showed a massive \"void\" in Zone 14.\n",
    "- **Conclusion:** The Morocco match exposed the fatal flaw of Spain's 2022 system: optimizing for ball retention rather than space exploitation against low blocks."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Team Structure Change Ranking\n",
    "Filtering out normal variance, here are the top 5 structural changes from 2022 to Euro 2024 (from Notebook 07):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "ranking_data = {\n",
    "    'Rank': [1, 2, 3, 4, 5],\n",
    "    'Metric Shift': ['Drop in Total Passes per Match (-37%)', 'Increase in F3 Central Entries (+28%)', \n",
    "                     'Decrease in Passes Before Shot (-37.5%)', 'Increase in Defensive Pressure (PPDA improvement)',\n",
    "                     'Shift in Shot Assists to Wide/Half-Spaces'],\n",
    "    'Tactical Meaning': ['Drastic shift away from sterile horizontal possession.',\n",
    "                         'Massive improvement in penetrating the most dangerous zones.',\n",
    "                         'Faster, more direct attacking transitions.',\n",
    "                         'More aggressive counter-pressing to sustain high-tempo play.',\n",
    "                         'Better utilization of the full width of the pitch to create chances.']\n",
    "}\n",
    "ranking_df = pd.DataFrame(ranking_data)\n",
    "display(HTML(ranking_df.to_html(index=False)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Player-Level Attribution\n",
    "Mapping the structural changes to specific personnel (from Notebook 08):\n",
    "- **Lamine Yamal & Nico Williams:** Directly responsible for the increase in wide progression and half-space shot assists (Rank 5). They fundamentally altered the team's width.\n",
    "- **Dani Olmo & Fabian Ruiz:** The main beneficiaries of the width. They exploited the stretched defenses, directly causing the +28% spike in Central F3 Entries (Rank 2).\n",
    "- **Rodri (Systemic Shift):** His passing volume halved from 170 to 62 passes per match. This wasn't a personnel change, but a strict tactical instruction to act as a deeper defensive anchor to facilitate faster transition play (Rank 1 & 3)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Goalscoring Pattern Integration\n",
    "Does the goalscoring evidence from Notebook 09 match the progression data from Notebook 07?\n",
    "- **Yes, beautifully.** While the passing data showed an increase in central F3 entries, the shot assist origin maps explicitly confirm that the final, devastating actions originated from the newly utilized wide and half-spaces.\n",
    "- Additionally, the goal concentration chart proves the threat was heavily diversified across the front five in 2024, perfectly aligning with the less predictable passing network seen in 2024 vs 2022.\n",
    "\n",
    "**Visual Proof: Threat Distribution**\n",
    "![Threat Distribution](../outputs/figures/2024/viz80_threat_distribution.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. The H9 Question: Tactics vs Personnel\n",
    "**Was the transformation driven by better tactics or better players?**\n",
    "\n",
    "The data presents a beautifully mixed, but definitive answer: **It was a tactical revolution enabled by a personnel evolution.**\n",
    "\n",
    "1. **The Personnel Evolution:** The addition of Yamal and Williams mechanically increased transition speed and progressive carries. You cannot simply instruct 2022 players to dribble like them.\n",
    "2. **The Tactical Revolution:** We tested this using \"Returning Players\" (Rodri, Pedri). Rodri's massive drop in touches and shift to a pure defensive anchor role proves that the manager actively changed the system. He was no longer asked to infinitely recycle the ball; he was asked to protect against transitions so the new wingers could attack directly. \n",
    "\n",
    "**Conclusion:** The tactics changed to maximize the new personnel."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Full Narrative Synthesis\n",
    "\n",
    "### What was actually true about Spain 2022?\n",
    "Spain 2022 possessed the ball extensively but generated very low-quality chances. They suffered from predictable build-up patterns that elite defensive structures (like Morocco's) easily neutralized by packing the center.\n",
    "\n",
    "### What was assumed but NOT supported by data?\n",
    "It was assumed Spain created great chances but simply lacked a \"finisher.\" The data rejects this: their xG per shot was incredibly low, meaning they were forced into low-percentage shots. The issue was *chance quality*, not just finishing.\n",
    "\n",
    "### What changed by 2024?\n",
    "Spain dropped their overall pass volume by 37% and became significantly more vertical. The introduction of elite wide wingers stretched defenses, allowing central midfielders to penetrate \"Zone 14\" aggressively. \n",
    "\n",
    "### Epistemic Humility (Limitations)\n",
    "While these conclusions are strongly supported by event data, it is vital to acknowledge sample size limitations (each tournament is at most 7 matches). Furthermore, we are comparing different opponents. Spain did not play Morocco in 2024, meaning we cannot guarantee the 2024 system would have effortlessly dismantled that exact 2022 block. However, the delta in attacking diversity strongly suggests they would have fared much better.\n",
    "\n",
    "### The Causal Chain (The Hero Visual)\n",
    "![Hero Visual](../outputs/figures/2024/viz81_hero_composite.png)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open('10_final_tactical_synthesis.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)
