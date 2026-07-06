# Research & Implementation Plan
## "When Possession Isn't Enough: A Tactical Analysis of Spain at Qatar 2022" (→ Euro 2024)

---

# PART 1 — UNDERSTANDING THE PROJECT

## The Story

Spain arrived at Qatar 2022 with the highest possession share of any team in the tournament and left in the Round of 16, eliminated by Morocco on penalties without scoring in open play across their final two knockout-adjacent matches. Two years later, a visibly younger, more direct Spain won Euro 2024 without ever needing to rely on the same suffocating possession identity.

The paper is not a "possession vs. directness" morality tale. It is a diagnostic: possession is a *means*, not an *end*. The 2022 squad optimized for control of the ball rather than control of space. The central narrative arc is:

**Control of the ball (2022) → Control of the ball without control of danger → Structural and personnel diagnosis of why → Deliberate tactical correction → Control of danger through the ball (2024).**

The emotional/analytical hook for readers: Spain had the ball 76% of the time against Morocco and generated almost nothing. That single fact is the entry point. Everything else in the paper exists to explain it and then show how it was fixed.

## Hypotheses to Test

These must be treated as hypotheses, not conclusions, and each needs a metric that can falsify it.

**H1 — Possession without penetration.** Spain circulated the ball extensively in low-danger zones (own half, wide areas) rather than progressing it into central/half-space attacking zones.
*Falsifiable via:* share of passes by pitch third, progressive pass counts into the final third vs. total pass volume, pass network centrality in wide vs. central zones.

**H2 — Lack of verticality/directness.** Spain's passing was lateral/backward-biased rather than forward-biased, slowing attacking tempo.
*Falsifiable via:* average pass direction angle, forward-pass ratio, pass speed/tempo (seconds per possession), directness index (net distance gained toward goal ÷ total distance passed).

**H3 — Predictable, low-variance build-up.** Spain's build-up shape and progression routes were repetitive enough that opponents (particularly Morocco) could set a low block and defend rehearsed patterns rather than react.
*Falsifiable via:* variety of progression corridors (entropy of final-third entry zones), frequency of specific buildup patterns (e.g., Busquets-drop, split centre-backs), opponent PPDA and block height against Spain.

**H4 — Central overload without central penetration.** Spain overloaded central zones for retention but lacked the passing lanes or player movement to break lines centrally, forcing reliance on wide recycling.
*Falsifiable via:* successful passes into the box by origin zone (central vs. wide), line-breaking pass counts, touches in the box by zone.

**H5 — Weak transition threat.** Spain's structure (high number of players committed to buildup, narrow full-back positioning) limited counter-attacking speed and numbers going forward after winning the ball.
*Falsifiable via:* counter-attack frequency, speed of possession after regain, number of players beyond the ball within 5 seconds of a turnover won.

**H6 — Underperformance relative to chance quality, not just chance quantity.** Spain generated a reasonable xG but did not convert; alternatively, they generated genuinely low-quality chances despite territorial dominance.
*Falsifiable via:* xG per shot (quality), xG total vs. goals (finishing), shot location map, big chances created.

**H7 — Morocco's defensive shape specifically neutralized Spain's patterns.** Morocco's mid/low block was set up to deny the exact central lanes and half-space combinations Spain relied on.
*Falsifiable via:* Spain's touches/passes by zone against Morocco specifically vs. Spain's tournament average; defensive action locations for Morocco.

**H8 — Euro 2024 shows measurable directional change**, not just narrative change: more verticality, more transition output, more individual carrying threat (Yamal/Nico Williams as inverted wingers), more variety in progression, and faster xG accumulation.
*Falsifiable via:* directly comparing the 2022 metrics above to the same metrics computed for Spain's Euro 2024 matches.

**H9 — Personnel change (not just tactical instruction) is the primary driver.** The presence of high-volume dribblers/carriers wide (Yamal, Nico Williams, Cucurella/Fabián overlaps) mechanically increases transition and penetration numbers independent of "philosophy."
*Falsifiable via:* player-level carry and dribble volumes 2022 vs. 2024, xG chain involvement by player, comparing Ferran Torres/Olmo-era wide play to Yamal/Williams-era wide play.

## Questions the Paper Must Answer

1. Did Spain actually lack penetration in 2022, or did they create enough danger and simply fail to finish?
2. Where specifically did Spain's attacks break down — buildup, progression, or final third?
3. Was Morocco's result a product of Spain's structural weakness, or elite opposition defending (i.e., is this generalizable or match-specific)?
4. What changed mechanically between 2022 and 2024 — formation, roles, personnel, or all three?
5. Which individual players are most responsible for the increase in attacking output, and can that be isolated from simple opponent-quality differences between the two tournaments?
6. Is Spain 2024 a genuinely different tactical model, or the same model executed by better dribblers?

## Evidence Standard

For every hypothesis, the paper should report:
- The metric(s) used
- The value for Spain 2022 (tournament-wide and Morocco match specifically)
- A benchmark for context (tournament average, or Euro 2024 equivalent)
- A one-line verdict: **Supported / Partially supported / Not supported**

This keeps the paper honest and avoids confirmation bias — several of these "obvious" narratives (e.g., "Spain lacked directness") are commonly asserted in football media but are not always borne out cleanly in the data, and the paper's credibility depends on showing that rigor.

---

# PART 2 — RESEARCH PLAN (GROUPS)

Each group answers exactly one tactical question and flows into the next.

### Group A — Territory & Possession Quality
**Question:** Did Spain control the ball, or control the pitch?
- Metrics: possession %, touches by pitch third, field tilt, deep progressions, PPDA (Spain's own, and opponent's PPDA against Spain)
- Visualizations: territory heatmap, zone-by-zone touch share
- Interpretation: distinguishes "possession volume" from "territorial dominance in dangerous zones"

### Group B — Buildup Structure
**Question:** How did Spain build attacks from the back, and how rigid was it?
- Metrics: average positions during buildup phase, pass network (centrality, edge weight), buildup pattern frequency (e.g., third-man combinations, Busquets drop-ins)
- Visualizations: average position maps, passing networks (buildup phase only), pass sonar from key buildup players
- Interpretation: tests H3 (predictability) and H4 (central overload)

### Group C — Progression (Passing & Carrying)
**Question:** How did Spain move the ball from buildup into the final third?
- Metrics: progressive passes, progressive carries, line-breaks (passes that bypass an opposition line), final-third entries by zone (wide vs. half-space vs. central)
- Visualizations: progressive pass maps, progressive carry maps, final-third entry zone map
- Interpretation: core test of H1 and H2 — directness and penetration

### Group D — Chance Creation
**Question:** When Spain reached the final third, what did they actually create?
- Metrics: shot count, xG total and xG/shot, big chances, key passes, xA, touches in the box, box-entry origin zone
- Visualizations: shot maps / xG maps, xG timeline (cumulative xG race chart), key-pass origin map
- Interpretation: separates "created enough, didn't finish" from "didn't create enough" — directly tests H6

### Group E — Pressing & Defensive Structure
**Question:** Was Spain's pressing an attacking weapon (winning the ball high to create instant chances) or purely defensive?
- Metrics: PPDA, high recoveries (in final/middle third), pressures and pressure success rate, time-to-shot after high recovery
- Visualizations: defensive action heatmap, pressure success map, recovery-to-shot sequences
- Interpretation: tests whether Spain's control extended to defensive/transitional moments or was purely a passing-phase phenomenon

### Group F — Transition Attack
**Question:** How dangerous was Spain immediately after winning the ball back?
- Metrics: counter-attack frequency, seconds from regain to shot, players ahead of the ball within 5 seconds of regain, progressive distance covered in first 3 actions after a turnover won
- Visualizations: transition sequence maps, "counter-attack speed" scatter (time vs. distance gained)
- Interpretation: tests H5 directly — structural cost of committing numbers to buildup

### Group G — The Morocco Case Study
**Question:** What specifically did Morocco do to nullify Spain's approach, and was it Spain's flaw or Morocco's plan?
- Metrics: Spain's Group A–F metrics recomputed for the Morocco match only, compared against Spain's group-stage average; Morocco's defensive block height, PPDA, and defensive action zones
- Visualizations: side-by-side "Spain vs. Group Stage average" radar or bar comparison; Morocco defensive shape map
- Interpretation: tests H7 — isolates whether the World Cup failure is systemic or opponent-specific (important for intellectual honesty)

### Group H — Personnel Roles (2022 lens)
**Question:** How did individual player profiles shape (or constrain) the system above?
- Feeds directly into Part 6 (Player Analysis)
- Metrics/visuals assigned per player

### Group I — The Euro 2024 Mirror
**Question:** Repeat Groups A–F for Euro 2024 and compare directly.
- Same metric set, same visualization types, applied to the 2024 dataset, presented side-by-side with 2022 equivalents
- This is what allows Part 9's "before/after" narrative to be data-driven rather than descriptive

### Group J — Personnel Roles (2024 lens) & Evolution
**Question:** Which players account for the measured change, and how?
- Feeds directly into Part 8 (Player Evolution)

### Group K — Synthesis
**Question:** Bringing it all together — what is the causal chain from 2022 to 2024?
- No new metrics; this is the narrative-construction group where the verdicts from A–J are assembled into the final argument and the hypothesis scorecard (Supported/Partial/Not supported) is presented.

---

# PART 3 — IMPLEMENTATION PLAN (NOTEBOOKS)

No code — structure and purpose only.

**01_setup_and_authentication.ipynb**
- Objective: install/verify `statsbombpy`, `mplsoccer`, and required libraries, then confirm access to StatsBomb Open Data (FIFA World Cup 2022 and UEFA Euro 2024).
- Inputs: none
- Outputs: verified environment, available competition and season IDs, ready-to-use project setup.

**02_load_and_prepare_data.ipynb**
- Objective: load all Spain matches from the 2022 FIFA World Cup and Euro 2024, including events, lineups and 360 data where available, then organize them into a consistent local dataset.
- Inputs: competition/season IDs
- Outputs: raw event data, lineup data, match inventory, combined datasets ready for cleaning.

**03_data_validation_and_cleaning.ipynb**
- Objective: validate, clean and standardize the datasets by checking event counts, handling missing values, standardizing player/team names and preparing a single analysis-ready dataset.
- Inputs: raw datasets from Notebook 02
- Outputs: cleaned, validated and tournament-tagged master dataset.

**04_spain_2022_tactical_analysis.ipynb** (Groups A–F)
- Objective: perform the complete tactical analysis of Spain's 2022 World Cup campaign, including territory, possession quality, build-up structure, progression, chance creation, pressing and transition play.
- Inputs: cleaned 2022 event dataset
- Outputs: all major team visualizations, tactical metrics, summary tables and key findings for Spain 2022.

**05_morocco_case_study.ipynb** (Group G)
- Objective: investigate why Morocco successfully stopped Spain by directly comparing the Round of 16 match with Spain's overall tournament performance.
- Inputs: Morocco match events and Spain 2022 tournament data
- Outputs: comparative visualizations, defensive structure analysis and evidence supporting or rejecting the Morocco-specific hypotheses.

**06_spain_2022_player_analysis.ipynb** (Group H)
- Objective: analyze the individual performances and tactical roles of Spain's key players, including Rodri, Pedri, Busquets, Dani Olmo, Gavi, Jordi Alba, Ferran Torres and Álvaro Morata.
- Inputs: cleaned 2022 player event data
- Outputs: player heatmaps, touch maps, passing maps, progressive actions, shot maps and individual performance summaries.

**07_euro2024_tactical_evolution.ipynb** (Groups I & J)
- Objective: analyze how Spain evolved at Euro 2024 by repeating the key tactical metrics from the 2022 analysis and highlighting the most important changes in playing style, player roles and attacking structure, with particular focus on Lamine Yamal, Nico Williams, Rodri, Pedri and Dani Olmo.
- Inputs: cleaned Euro 2024 event data
- Outputs: selected tactical comparisons, player visualizations, evolution of key metrics and evidence explaining Spain's transformation.

**08_final_comparison_and_conclusions.ipynb** (Group K)
- Objective: bring together all findings from the project to directly compare Spain 2022 with Euro 2024, evaluate each hypothesis and construct the final evidence-based narrative.
- Inputs: summary tables, metrics and visualizations from Notebooks 04–07
- Outputs: before-vs-after comparison figures, hypothesis scorecard, final conclusions and publication-ready visualizations for the research paper.

# PART 4 — VISUALIZATION PLAN

# Research & Implementation Plan
## "When Possession Isn't Enough: A Tactical Analysis of Spain at Qatar 2022" (→ Euro 2024)

---

# PART 1 — UNDERSTANDING THE PROJECT

## The Story

Spain arrived at Qatar 2022 with the highest possession share of any team in the tournament and left in the Round of 16, eliminated by Morocco on penalties without scoring in open play across their final two knockout-adjacent matches. Two years later, a visibly younger, more direct Spain won Euro 2024 without ever needing to rely on the same suffocating possession identity.

The paper is not a "possession vs. directness" morality tale. It is a diagnostic: possession is a *means*, not an *end*. The 2022 squad optimized for control of the ball rather than control of space. The central narrative arc is:

**Control of the ball (2022) → Control of the ball without control of danger → Structural and personnel diagnosis of why → Deliberate tactical correction → Control of danger through the ball (2024).**

The emotional/analytical hook for readers: Spain had the ball 76% of the time against Morocco and generated almost nothing. That single fact is the entry point. Everything else in the paper exists to explain it and then show how it was fixed.

## Hypotheses to Test

These must be treated as hypotheses, not conclusions, and each needs a metric that can falsify it.

**H1 — Possession without penetration.** Spain circulated the ball extensively in low-danger zones (own half, wide areas) rather than progressing it into central/half-space attacking zones.
*Falsifiable via:* share of passes by pitch third, progressive pass counts into the final third vs. total pass volume, pass network centrality in wide vs. central zones.

**H2 — Lack of verticality/directness.** Spain's passing was lateral/backward-biased rather than forward-biased, slowing attacking tempo.
*Falsifiable via:* average pass direction angle, forward-pass ratio, pass speed/tempo (seconds per possession), directness index (net distance gained toward goal ÷ total distance passed).

**H3 — Predictable, low-variance build-up.** Spain's build-up shape and progression routes were repetitive enough that opponents (particularly Morocco) could set a low block and defend rehearsed patterns rather than react.
*Falsifiable via:* variety of progression corridors (entropy of final-third entry zones), frequency of specific buildup patterns (e.g., Busquets-drop, split centre-backs), opponent PPDA and block height against Spain.

**H4 — Central overload without central penetration.** Spain overloaded central zones for retention but lacked the passing lanes or player movement to break lines centrally, forcing reliance on wide recycling.
*Falsifiable via:* successful passes into the box by origin zone (central vs. wide), line-breaking pass counts, touches in the box by zone.

**H5 — Weak transition threat.** Spain's structure (high number of players committed to buildup, narrow full-back positioning) limited counter-attacking speed and numbers going forward after winning the ball.
*Falsifiable via:* counter-attack frequency, speed of possession after regain, number of players beyond the ball within 5 seconds of a turnover won.

**H6 — Underperformance relative to chance quality, not just chance quantity.** Spain generated a reasonable xG but did not convert; alternatively, they generated genuinely low-quality chances despite territorial dominance.
*Falsifiable via:* xG per shot (quality), xG total vs. goals (finishing), shot location map, big chances created.

**H7 — Morocco's defensive shape specifically neutralized Spain's patterns.** Morocco's mid/low block was set up to deny the exact central lanes and half-space combinations Spain relied on.
*Falsifiable via:* Spain's touches/passes by zone against Morocco specifically vs. Spain's tournament average; defensive action locations for Morocco.

**H8 — Euro 2024 shows measurable directional change**, not just narrative change: more verticality, more transition output, more individual carrying threat (Yamal/Nico Williams as inverted wingers), more variety in progression, and faster xG accumulation.
*Falsifiable via:* directly comparing the 2022 metrics above to the same metrics computed for Spain's Euro 2024 matches.

**H9 — Personnel change (not just tactical instruction) is the primary driver.** The presence of high-volume dribblers/carriers wide (Yamal, Nico Williams, Cucurella/Fabián overlaps) mechanically increases transition and penetration numbers independent of "philosophy."
*Falsifiable via:* player-level carry and dribble volumes 2022 vs. 2024, xG chain involvement by player, comparing Ferran Torres/Olmo-era wide play to Yamal/Williams-era wide play.

## Questions the Paper Must Answer

1. Did Spain actually lack penetration in 2022, or did they create enough danger and simply fail to finish?
2. Where specifically did Spain's attacks break down — buildup, progression, or final third?
3. Was Morocco's result a product of Spain's structural weakness, or elite opposition defending (i.e., is this generalizable or match-specific)?
4. What changed mechanically between 2022 and 2024 — formation, roles, personnel, or all three?
5. Which individual players are most responsible for the increase in attacking output, and can that be isolated from simple opponent-quality differences between the two tournaments?
6. Is Spain 2024 a genuinely different tactical model, or the same model executed by better dribblers?

## Evidence Standard

For every hypothesis, the paper should report:
- The metric(s) used
- The value for Spain 2022 (tournament-wide and Morocco match specifically)
- A benchmark for context (tournament average, or Euro 2024 equivalent)
- A one-line verdict: **Supported / Partially supported / Not supported**

This keeps the paper honest and avoids confirmation bias — several of these "obvious" narratives (e.g., "Spain lacked directness") are commonly asserted in football media but are not always borne out cleanly in the data, and the paper's credibility depends on showing that rigor.

---

# PART 2 — RESEARCH PLAN (GROUPS)

Each group answers exactly one tactical question and flows into the next.

### Group A — Territory & Possession Quality
**Question:** Did Spain control the ball, or control the pitch?
- Metrics: possession %, touches by pitch third, field tilt, deep progressions, PPDA (Spain's own, and opponent's PPDA against Spain)
- Visualizations: territory heatmap, zone-by-zone touch share
- Interpretation: distinguishes "possession volume" from "territorial dominance in dangerous zones"

### Group B — Buildup Structure
**Question:** How did Spain build attacks from the back, and how rigid was it?
- Metrics: average positions during buildup phase, pass network (centrality, edge weight), buildup pattern frequency (e.g., third-man combinations, Busquets drop-ins)
- Visualizations: average position maps, passing networks (buildup phase only), pass sonar from key buildup players
- Interpretation: tests H3 (predictability) and H4 (central overload)

### Group C — Progression (Passing & Carrying)
**Question:** How did Spain move the ball from buildup into the final third?
- Metrics: progressive passes, progressive carries, line-breaks (passes that bypass an opposition line), final-third entries by zone (wide vs. half-space vs. central)
- Visualizations: progressive pass maps, progressive carry maps, final-third entry zone map
- Interpretation: core test of H1 and H2 — directness and penetration

### Group D — Chance Creation
**Question:** When Spain reached the final third, what did they actually create?
- Metrics: shot count, xG total and xG/shot, big chances, key passes, xA, touches in the box, box-entry origin zone
- Visualizations: shot maps / xG maps, xG timeline (cumulative xG race chart), key-pass origin map
- Interpretation: separates "created enough, didn't finish" from "didn't create enough" — directly tests H6

### Group E — Pressing & Defensive Structure
**Question:** Was Spain's pressing an attacking weapon (winning the ball high to create instant chances) or purely defensive?
- Metrics: PPDA, high recoveries (in final/middle third), pressures and pressure success rate, time-to-shot after high recovery
- Visualizations: defensive action heatmap, pressure success map, recovery-to-shot sequences
- Interpretation: tests whether Spain's control extended to defensive/transitional moments or was purely a passing-phase phenomenon

### Group F — Transition Attack
**Question:** How dangerous was Spain immediately after winning the ball back?
- Metrics: counter-attack frequency, seconds from regain to shot, players ahead of the ball within 5 seconds of regain, progressive distance covered in first 3 actions after a turnover won
- Visualizations: transition sequence maps, "counter-attack speed" scatter (time vs. distance gained)
- Interpretation: tests H5 directly — structural cost of committing numbers to buildup

### Group G — The Morocco Case Study
**Question:** What specifically did Morocco do to nullify Spain's approach, and was it Spain's flaw or Morocco's plan?
- Metrics: Spain's Group A–F metrics recomputed for the Morocco match only, compared against Spain's group-stage average; Morocco's defensive block height, PPDA, and defensive action zones
- Visualizations: side-by-side "Spain vs. Group Stage average" radar or bar comparison; Morocco defensive shape map
- Interpretation: tests H7 — isolates whether the World Cup failure is systemic or opponent-specific (important for intellectual honesty)

### Group H — Personnel Roles (2022 lens)
**Question:** How did individual player profiles shape (or constrain) the system above?
- Feeds directly into Part 6 (Player Analysis)
- Metrics/visuals assigned per player

### Group I — The Euro 2024 Mirror
**Question:** Repeat Groups A–F for Euro 2024 and compare directly.
- Same metric set, same visualization types, applied to the 2024 dataset, presented side-by-side with 2022 equivalents
- This is what allows Part 9's "before/after" narrative to be data-driven rather than descriptive

### Group J — Personnel Roles (2024 lens) & Evolution
**Question:** Which players account for the measured change, and how?
- Feeds directly into Part 8 (Player Evolution)

### Group K — Synthesis
**Question:** Bringing it all together — what is the causal chain from 2022 to 2024?
- No new metrics; this is the narrative-construction group where the verdicts from A–J are assembled into the final argument and the hypothesis scorecard (Supported/Partial/Not supported) is presented.

---

# PART 3 — IMPLEMENTATION PLAN (NOTEBOOKS)

No code — structure and purpose only.

**01_setup_and_authentication.ipynb**
- Objective: install/verify `statsbombpy`, `mplsoccer`, and required libraries, then confirm access to StatsBomb Open Data (FIFA World Cup 2022 and UEFA Euro 2024).
- Inputs: none
- Outputs: verified environment, available competition and season IDs, ready-to-use project setup.

**02_load_and_prepare_data.ipynb**
- Objective: load all Spain matches from the 2022 FIFA World Cup and Euro 2024, including events, lineups and 360 data where available, then organize them into a consistent local dataset.
- Inputs: competition/season IDs
- Outputs: raw event data, lineup data, match inventory, combined datasets ready for cleaning.

**03_data_validation_and_cleaning.ipynb**
- Objective: validate, clean and standardize the datasets by checking event counts, handling missing values, standardizing player/team names and preparing a single analysis-ready dataset.
- Inputs: raw datasets from Notebook 02
- Outputs: cleaned, validated and tournament-tagged master dataset.

**04_spain_2022_tactical_analysis.ipynb** (Groups A–F)
- Objective: perform the complete tactical analysis of Spain's 2022 World Cup campaign, including territory, possession quality, build-up structure, progression, chance creation, pressing and transition play.
- Inputs: cleaned 2022 event dataset
- Outputs: all major team visualizations, tactical metrics, summary tables and key findings for Spain 2022.

**05_morocco_case_study.ipynb** (Group G)
- Objective: investigate why Morocco successfully stopped Spain by directly comparing the Round of 16 match with Spain's overall tournament performance.
- Inputs: Morocco match events and Spain 2022 tournament data
- Outputs: comparative visualizations, defensive structure analysis and evidence supporting or rejecting the Morocco-specific hypotheses.

**05b_wing_play_and_substitute_impact.ipynb** (extends Group G)
- Objective: establish, with data, that Morocco's low block specifically denied Spain's
  central progression, that Spain's resulting attack was left-side-heavy and predictable
  due to a lack of a genuine right-sided winger (Ferran Torres nominally started wide
  right but profiles more as an inverted/central forward), and that this contributed
  directly to Spain failing to score. The notebook then isolates the Nico Williams
  substitution as the clearest single data point of what a genuine winger changed —
  comparing his output directly against Ferran Torres's in the same match, and comparing
  Spain's attacking output in the minutes before vs after he entered.
- Inputs: Spain vs Morocco match event data (from Notebook 05), lineup/substitution data
- Outputs: side-by-side wing analysis (left vs right flank output), a verified
  substitution timeline, a full Nico Williams impact profile (heatmap, xG, touches in
  box, dribbles, carries, minutes played), a direct Ferran Torres vs Nico Williams
  comparison on the right flank, and a before/after team-output comparison split at the
  substitution minute.

**06_spain_2022_player_analysis.ipynb** (Group H)
- Objective: analyze the individual performances and tactical roles of Spain's key players, including Rodri, Pedri, Busquets, Dani Olmo, Gavi, Jordi Alba, Ferran Torres and Álvaro Morata.
- Inputs: cleaned 2022 player event data
- Outputs: player heatmaps, touch maps, passing maps, progressive actions, shot maps and individual performance summaries.

**07_euro2024_team_tactical_analysis.ipynb** (Group I)
- Objective: perform the complete team-level tactical analysis of Spain's Euro 2024
  campaign, mirroring Notebook 04 exactly — territory, possession quality, buildup
  structure and shape, passing network structure, progression, chance creation,
  pressing and transition play — so every metric is directly comparable to 2022.
- Inputs: cleaned Euro 2024 event dataset (build in Notebook 02/03 if not already done)
- Outputs: full Euro 2024 team-level metrics and visualizations, formatted identically
  to Notebook 04's outputs, ready for direct side-by-side comparison.

**08_euro2024_player_analysis.ipynb** (Group J)
- Objective: perform a complete individual player analysis for Spain's Euro 2024 squad,
  mirroring Notebook 06 — heatmaps, passing networks, possession involvement, progressive
  actions, defensive contributions — with particular depth on Lamine Yamal, Nico
  Williams, Rodri, Pedri and Dani Olmo, while remaining open to any other player who
  proves tactically significant in the data. For returning players (Rodri, Pedri,
  Olmo), directly overlay/compare their 2022 profile against their 2024 profile.
- Inputs: cleaned Euro 2024 event dataset, plus Notebook 06 outputs for returning-player
  comparisons.
- Outputs: full player profile cards (heatmap + passing network + stat panel) for all
  key Euro 2024 players, and 2022-vs-2024 comparison visuals for returning players.

**09_shots_goals_comparative_analysis.ipynb** (supports Groups D, I, J, K)
- Objective: build a dedicated, detailed comparison of where and how Spain created
  and scored goals in 2022 vs 2024 — shot locations, goal locations, shot situation
  (open play/set piece/counter), body part, assist origin zones, and xG quality —
  at both team level and for the most involved individual shooters/creators in each
  tournament.
- Inputs: cleaned event datasets for both tournaments (shots, goals, key passes/assists)
- Outputs: team and player-level shot maps and goal maps for both tournaments, a
  side-by-side shot-quality and shot-origin comparison, and a summary of exactly how
  Spain's goalscoring patterns changed.

**10_final_comparison_and_conclusions.ipynb** (Group K)
- Objective: bring together all findings from Notebooks 04–09 to directly compare
  Spain 2022 with Euro 2024, evaluate each hypothesis and construct the final
  evidence-based narrative.
- Inputs: summary tables, metrics and visualizations from Notebooks 04–09
- Outputs: before-vs-after comparison figures, hypothesis scorecard, final conclusions
  and publication-ready visualizations for the research paper.

# PART 4 — VISUALIZATION PLAN

Only visualizations that answer a specific question are included.

| # | Title | Question Answered | Why It Matters | Data Required | Library | Difficulty | Expected Insight |
|---|-------|-------------------|------------------|----------------|---------|------------|-------------------|
| 1 | Territory Heatmap (Spain vs. tournament avg) | Did Spain control dangerous zones or just possession? | Separates raw possession % from territorial danger | Location data, all events | mplsoccer | Easy | Likely heavy concentration in own half/wide areas rather than central final third |
| 2 | Average Position Map (buildup phase) | What shape did Spain build in? | Reveals rigidity/width of buildup structure | Passing events, player locations | mplsoccer | Medium | Tests predictability (H3) |
| 3 | Passing Network (buildup only) | Who dominated ball circulation and where? | Identifies over-reliance on specific central nodes (e.g., Busquets) | Pass events, player IDs | mplsoccer/networkx | Medium | Tests H4 — central overload without penetration |
| 4 | Progressive Pass Map | Where did Spain progress the ball into danger? | Direct test of penetration vs. mere circulation | Pass events with progressive-pass calculation | mplsoccer | Medium | Tests H1 directly |
| 5 | Progressive Carry Map | Did players carry the ball forward, or rely only on passing? | Distinguishes passing-only teams from dual-threat teams | Carry events | mplsoccer | Medium | Useful baseline for 2024 comparison (carry volume likely rises sharply) |
| 6 | Final-Third Entry Zone Breakdown | Did Spain enter dangerous zones centrally or only wide? | Tests reliance on wide recycling (H1/H4) | Pass/carry end-locations | mplsoccer/pandas | Easy | Likely wide-heavy in 2022 |
| 7 | Shot Map / xG Map | Was the finishing problem shot quality or shot conversion? | Core test of H6 | Shot events, xG | mplsoccer | Easy | Distinguishes "bad chances" from "missed good chances" |
| 8 | xG Timeline (cumulative race chart) | When and how quickly did Spain generate danger across matches? | Shows tempo of threat generation, not just totals | Shot events with timestamps | matplotlib | Easy | May reveal slow accumulation vs. bursts |
| 9 | Pass Sonar (key buildup players) | What passing options/directions did key players actually use? | Tests directness/verticality (H2) at player level | Pass angle/distance per player | mplsoccer | Medium | Tests whether central players passed forward or sideways/back |
| 10 | Pressure Heatmap | Where did Spain press, and how aggressively? | Establishes whether control extended off the ball | Pressure events | mplsoccer | Easy | Context for Group E |
| 11 | PPDA Comparison (Spain vs. opponents, 2022) | Was pressing intensity actually high, or reputation-driven? | Quantifies a commonly-assumed strength | Pass/defensive-action counts | pandas/matplotlib | Easy | Baseline for 2024 comparison |
| 12 | Transition Speed Scatter (time vs. distance after regain) | How dangerous was Spain in transition? | Direct test of H5 | Possession-chain event sequencing | matplotlib | Hard | Likely shows slow, low-distance transitions in 2022 |
| 13 | Morocco Comparative Radar (Spain vs. Morocco match vs. Spain group-stage avg) | Was the Morocco loss systemic or opponent-specific? | Tests H7; adds intellectual honesty to the narrative | Aggregated metrics from Groups A–F | matplotlib | Medium | Clarifies whether Morocco "solved" Spain or Spain simply underperformed |
| 14 | Morocco Defensive Shape Map | What structure stopped Spain specifically? | Shows the mechanism of the defensive success | Morocco defensive event locations | mplsoccer | Medium | Confirms/refutes H7 with opponent-side evidence |
| 15 | Player Touch/Heatmap Panels (Rodri, Pedri, Busquets, etc.) | What role did each key player actually occupy on the pitch? | Grounds Part 6 in data, not reputation | Touch locations per player | mplsoccer | Easy | Identifies role rigidity or overlap |
| 16 | 2022 vs. 2024 Side-by-Side Metric Comparison (small multiples) | What quantitatively changed between tournaments? | The paper's central evidentiary payoff | All Group A–F metrics computed for both tournaments | matplotlib | Medium | This is the visual proof of the paper's thesis |
| 17 | Yamal/Nico Williams Carry & Dribble Map (2024) | Did wide personnel change explain the increase in threat? | Direct test of H9 | Carry/dribble events, 2024 | mplsoccer | Medium | Likely shows high-volume, high-success wide carrying absent in 2022 wide play |
| 18 | Player xG Chain Involvement Comparison (Pedri/Rodri/Olmo, 2022 vs. 2024) | Did returning players change their own output, or did new players around them change the system? | Isolates personnel vs. tactical-instruction effects (H9 vs. H8) | Possession-chain data, xG buildup | pandas/matplotlib | Hard | Key to answering "was it the plan or the players?" |
| 19 | Width Utilization Comparison (touch distribution across pitch width, 2022 vs. 2024) | Did Spain actually become "wider" as commonly claimed? | Tests a frequently-asserted but rarely-verified claim | Touch x/y coordinates | mplsoccer | Easy | May confirm or complicate the "greater width" narrative |
| 20 | Final Hypothesis Scorecard (table/infographic) | Which hypotheses held up? | Closes the paper with a transparent, evidence-based summary | All prior results | matplotlib/table | Easy | Delivers the paper's core credibility statement |

Note: visualizations 1–15 are 2022-focused (Parts 5–6); 16–20 are comparative/2024-focused (Parts 7–9). This keeps the visual budget disciplined — roughly 20 total, each tied to a specific question, rather than an unstructured gallery.

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 5 — SPAIN 2022 ANALYSIS: THEMES TO INVESTIGATE

Treat every item below as a question, not a fact, and resolve it using Groups A–G:

- **Possession without penetration** → Groups A, C, D
- **Lack of verticality / directness** → Groups B, C (pass sonar, forward-pass ratio)
- **Slow circulation / predictable buildup** → Group B (network centrality, pattern repetition)
- **Limited threat in transition** → Group F
- **Poor chance creation vs. poor finishing** → Group D (xG/shot is the deciding metric)
- **Reliance on wide recycling** → Group C (final-third entry zones)
- **Limited through balls / poor central progression** → Groups C, D (central vs. wide box entries)
- **Defensive strengths / pressing effectiveness** → Group E
- **Why Morocco succeeded** → Group G specifically; do not generalize this to "Spain's system failed" until the comparative radar (Viz 13) is checked — it's possible Morocco's specific low block was simply well-executed against a team that was otherwise performing close to its season norms.

Recommend structuring this section of the paper as a sequence of "claim → test → verdict" mini-sections, mirroring the hypothesis structure in Part 1. This is what will make the paper feel like real analysis rather than a narrative built to fit a preconceived story.

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 6 — PLAYER ANALYSIS (2022)

| Player | Best Visualizations | Key Metrics | Role in System | Contribution to Success/Failure |
|---|---|---|---|---|
| **Rodri** | Touch heatmap, pass network centrality | Pass completion %, progressive passes, defensive actions | Deep-lying pivot, primary distributor alongside Busquets | Test whether he was used as a progressor or a safe recycler |
| **Pedri** | Progressive carry map, heatmap | Progressive carries, dribbles, line-breaking passes | Central connector between lines | Likely Spain's clearest individual penetration threat — worth checking if he was underused positionally |
| **Busquets** | Pass sonar, average position | Pass distribution angle, pressure resistance (passes under pressure) | Deepest buildup anchor | Central to testing H3/H4 — is the system built around his (declining) mobility? |
| **Dani Olmo** | Touch map, xG chain involvement | Key passes, xA, touches in box | Free role / secondary striker-winger hybrid | Check if he was Spain's main creative outlet given limited orthodox winger threat |
| **Gavi** | Heatmap, defensive actions + progressive carries | Ball recoveries, progressive carries, duels won | Box-to-box dynamism | Assess whether his energy compensated for structural rigidity elsewhere |
| **Jordi Alba** | Overlap/underlap map, crosses | Progressive passes/carries from LB, cross accuracy | Primary width provider on the left | Central to "reliance on wide recycling" — test his end product, not just volume |
| **Ferran Torres** | Touch map, shot map | Shots, xG, touches in box | Nominal right-wing threat | Likely a key data point for "limited wide threat" preceding Yamal's emergence |
| **Álvaro Morata** | Shot map, movement/reception map | xG, shots, aerial duels, hold-up passes received | Focal point striker | Test whether service quality or finishing was the bigger issue (feeds Group D directly) |

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 7 — EURO 2024: WHAT CHANGED?

Apply the exact Group A–F metric set from Part 2 to the 2024 dataset (Notebook 11) and test each claim below — do not assume:

- **Greater verticality / directness** → compare forward-pass ratio and directness index, 2022 vs. 2024
- **Greater transition threat** → compare Group F metrics directly
- **Improved wing play** → compare final-third entry zones and wide carry/dribble volumes
- **Higher attacking threat / more dangerous chances** → compare xG/shot and xG timelines
- **Improved pressing** → compare PPDA and high-recovery-to-shot times
- **Greater width** → compare touch-distribution-by-width (Viz 19) — this is one of the more commonly overstated claims in media coverage and deserves genuine scrutiny
- **More dynamic movement / more effective full-backs** → compare full-back progressive actions and overlap frequency
- **Better central progression** → compare central vs. wide progressive pass/carry share

Present every one of these as a paired before/after chart (Viz 16), not just prose description.

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 8 — PLAYER EVOLUTION (2022 → 2024)

This is the most important analytical section — it's where the paper answers "was it the tactics or the players?"

| Player | Analyses to Run | What It Should Reveal |
|---|---|---|
| **Lamine Yamal** | Touch map, carry/dribble map, xG chain involvement, reception locations | New profile entirely (didn't exist in 2022) — quantify his direct-carrying threat as a structural addition, not a replacement of like-for-like |
| **Nico Williams** | Same as above | Same purpose — the "inverted winger who carries" archetype largely absent in 2022's wide options |
| **Rodri** | 2022 vs. 2024 pass network position, progressive passes, defensive actions | Did his individual role change, or did the players around him change what his passes led to? Critical for isolating H8 vs. H9 |
| **Pedri** | 2022 vs. 2024 progressive carries, xG chain involvement | Test whether he became more central to progression or was simply healthier/more available |
| **Dani Olmo** | 2022 vs. 2024 touch map, xA, positional heatmap | Did his role shift from primary creator to secondary option as Yamal/Williams took over the creative burden? |

Recommended framing: build a single composite visualization (small multiples) showing each returning player's heatmap/output side-by-side, 2022 vs. 2024, directly above the new-personnel (Yamal/Williams) visualizations. This makes the "personnel vs. tactics" argument visually self-evident before a word of text explains it.

---

# PART 9 — FINAL STORY ARC (MAPPED TO GROUPS & VISUALS)

1. **Spain dominated possession** — Group A / Viz 1
2. **The possession lacked attacking threat** — Groups C & D / Viz 4, 6, 7, 8
3. **Data reveals exactly why** — Groups B, E, F, G / Viz 2, 3, 9–14
4. **Spain changed key tactical principles** — Group I / Viz 16
5. **New player profiles transformed the attack** — Group J / Viz 17, 18
6. **Euro 2024 demonstrates those tactical improvements** — Group I / Viz 16, 19
7. **Conclude with an evidence-based explanation** — Group K / Viz 20 (hypothesis scorecard)

This mapping is the paper's skeleton: every claim in the narrative has a named group, notebook, and visualization behind it, so nothing in the final draft will be asserted without a traceable data source.

---

## Practical Notes Before You Start

- **Data availability check first:** confirm StatsBomb Open Data actually includes 360 (freeze-frame) data for the Spain matches you need — it's not uniformly available across all matches/competitions, and several of the harder visualizations (pressure success, transition numbers-behind-the-ball) depend on it. If it's missing for some matches, note this as a limitation rather than skipping the analysis silently.
- **Match selection:** decide up front whether "Spain 2022" means all group + knockout matches or a curated subset (e.g., excluding the Costa Rica blowout, which will skew several metrics). Recommend analyzing all matches but flagging outliers explicitly.
- **Consistent zone/metric definitions across tournaments** are essential — define "progressive pass," "final third," and "half-space" once in Notebook 03 and reuse those exact functions everywhere, so 2022 and 2024 numbers are genuinely comparable.
- **Keep the hypothesis scorecard visible from the start** — update it as you complete each notebook rather than writing it retroactively; this is what will keep the paper's tone analytical rather than narrative-driven.

| # | Title | Question Answered | Why It Matters | Data Required | Library | Difficulty | Expected Insight |
|---|-------|-------------------|------------------|----------------|---------|------------|-------------------|
| 1 | Territory Heatmap (Spain vs. tournament avg) | Did Spain control dangerous zones or just possession? | Separates raw possession % from territorial danger | Location data, all events | mplsoccer | Easy | Likely heavy concentration in own half/wide areas rather than central final third |
| 2 | Average Position Map (buildup phase) | What shape did Spain build in? | Reveals rigidity/width of buildup structure | Passing events, player locations | mplsoccer | Medium | Tests predictability (H3) |
| 3 | Passing Network (buildup only) | Who dominated ball circulation and where? | Identifies over-reliance on specific central nodes (e.g., Busquets) | Pass events, player IDs | mplsoccer/networkx | Medium | Tests H4 — central overload without penetration |
| 4 | Progressive Pass Map | Where did Spain progress the ball into danger? | Direct test of penetration vs. mere circulation | Pass events with progressive-pass calculation | mplsoccer | Medium | Tests H1 directly |
| 5 | Progressive Carry Map | Did players carry the ball forward, or rely only on passing? | Distinguishes passing-only teams from dual-threat teams | Carry events | mplsoccer | Medium | Useful baseline for 2024 comparison (carry volume likely rises sharply) |
| 6 | Final-Third Entry Zone Breakdown | Did Spain enter dangerous zones centrally or only wide? | Tests reliance on wide recycling (H1/H4) | Pass/carry end-locations | mplsoccer/pandas | Easy | Likely wide-heavy in 2022 |
| 7 | Shot Map / xG Map | Was the finishing problem shot quality or shot conversion? | Core test of H6 | Shot events, xG | mplsoccer | Easy | Distinguishes "bad chances" from "missed good chances" |
| 8 | xG Timeline (cumulative race chart) | When and how quickly did Spain generate danger across matches? | Shows tempo of threat generation, not just totals | Shot events with timestamps | matplotlib | Easy | May reveal slow accumulation vs. bursts |
| 9 | Pass Sonar (key buildup players) | What passing options/directions did key players actually use? | Tests directness/verticality (H2) at player level | Pass angle/distance per player | mplsoccer | Medium | Tests whether central players passed forward or sideways/back |
| 10 | Pressure Heatmap | Where did Spain press, and how aggressively? | Establishes whether control extended off the ball | Pressure events | mplsoccer | Easy | Context for Group E |
| 11 | PPDA Comparison (Spain vs. opponents, 2022) | Was pressing intensity actually high, or reputation-driven? | Quantifies a commonly-assumed strength | Pass/defensive-action counts | pandas/matplotlib | Easy | Baseline for 2024 comparison |
| 12 | Transition Speed Scatter (time vs. distance after regain) | How dangerous was Spain in transition? | Direct test of H5 | Possession-chain event sequencing | matplotlib | Hard | Likely shows slow, low-distance transitions in 2022 |
| 13 | Morocco Comparative Radar (Spain vs. Morocco match vs. Spain group-stage avg) | Was the Morocco loss systemic or opponent-specific? | Tests H7; adds intellectual honesty to the narrative | Aggregated metrics from Groups A–F | matplotlib | Medium | Clarifies whether Morocco "solved" Spain or Spain simply underperformed |
| 14 | Morocco Defensive Shape Map | What structure stopped Spain specifically? | Shows the mechanism of the defensive success | Morocco defensive event locations | mplsoccer | Medium | Confirms/refutes H7 with opponent-side evidence |
| 15 | Player Touch/Heatmap Panels (Rodri, Pedri, Busquets, etc.) | What role did each key player actually occupy on the pitch? | Grounds Part 6 in data, not reputation | Touch locations per player | mplsoccer | Easy | Identifies role rigidity or overlap |
| 16 | 2022 vs. 2024 Side-by-Side Metric Comparison (small multiples) | What quantitatively changed between tournaments? | The paper's central evidentiary payoff | All Group A–F metrics computed for both tournaments | matplotlib | Medium | This is the visual proof of the paper's thesis |
| 17 | Yamal/Nico Williams Carry & Dribble Map (2024) | Did wide personnel change explain the increase in threat? | Direct test of H9 | Carry/dribble events, 2024 | mplsoccer | Medium | Likely shows high-volume, high-success wide carrying absent in 2022 wide play |
| 18 | Player xG Chain Involvement Comparison (Pedri/Rodri/Olmo, 2022 vs. 2024) | Did returning players change their own output, or did new players around them change the system? | Isolates personnel vs. tactical-instruction effects (H9 vs. H8) | Possession-chain data, xG buildup | pandas/matplotlib | Hard | Key to answering "was it the plan or the players?" |
| 19 | Width Utilization Comparison (touch distribution across pitch width, 2022 vs. 2024) | Did Spain actually become "wider" as commonly claimed? | Tests a frequently-asserted but rarely-verified claim | Touch x/y coordinates | mplsoccer | Easy | May confirm or complicate the "greater width" narrative |
| 20 | Final Hypothesis Scorecard (table/infographic) | Which hypotheses held up? | Closes the paper with a transparent, evidence-based summary | All prior results | matplotlib/table | Easy | Delivers the paper's core credibility statement |

Note: visualizations 1–15 are 2022-focused (Parts 5–6); 16–20 are comparative/2024-focused (Parts 7–9). This keeps the visual budget disciplined — roughly 20 total, each tied to a specific question, rather than an unstructured gallery.

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 5 — SPAIN 2022 ANALYSIS: THEMES TO INVESTIGATE

Treat every item below as a question, not a fact, and resolve it using Groups A–G:

- **Possession without penetration** → Groups A, C, D
- **Lack of verticality / directness** → Groups B, C (pass sonar, forward-pass ratio)
- **Slow circulation / predictable buildup** → Group B (network centrality, pattern repetition)
- **Limited threat in transition** → Group F
- **Poor chance creation vs. poor finishing** → Group D (xG/shot is the deciding metric)
- **Reliance on wide recycling** → Group C (final-third entry zones)
- **Limited through balls / poor central progression** → Groups C, D (central vs. wide box entries)
- **Defensive strengths / pressing effectiveness** → Group E
- **Why Morocco succeeded** → Group G specifically; do not generalize this to "Spain's system failed" until the comparative radar (Viz 13) is checked — it's possible Morocco's specific low block was simply well-executed against a team that was otherwise performing close to its season norms.

Recommend structuring this section of the paper as a sequence of "claim → test → verdict" mini-sections, mirroring the hypothesis structure in Part 1. This is what will make the paper feel like real analysis rather than a narrative built to fit a preconceived story.

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 6 — PLAYER ANALYSIS (2022)

| Player | Best Visualizations | Key Metrics | Role in System | Contribution to Success/Failure |
|---|---|---|---|---|
| **Rodri** | Touch heatmap, pass network centrality | Pass completion %, progressive passes, defensive actions | Deep-lying pivot, primary distributor alongside Busquets | Test whether he was used as a progressor or a safe recycler |
| **Pedri** | Progressive carry map, heatmap | Progressive carries, dribbles, line-breaking passes | Central connector between lines | Likely Spain's clearest individual penetration threat — worth checking if he was underused positionally |
| **Busquets** | Pass sonar, average position | Pass distribution angle, pressure resistance (passes under pressure) | Deepest buildup anchor | Central to testing H3/H4 — is the system built around his (declining) mobility? |
| **Dani Olmo** | Touch map, xG chain involvement | Key passes, xA, touches in box | Free role / secondary striker-winger hybrid | Check if he was Spain's main creative outlet given limited orthodox winger threat |
| **Gavi** | Heatmap, defensive actions + progressive carries | Ball recoveries, progressive carries, duels won | Box-to-box dynamism | Assess whether his energy compensated for structural rigidity elsewhere |
| **Jordi Alba** | Overlap/underlap map, crosses | Progressive passes/carries from LB, cross accuracy | Primary width provider on the left | Central to "reliance on wide recycling" — test his end product, not just volume |
| **Ferran Torres** | Touch map, shot map | Shots, xG, touches in box | Nominal right-wing threat | Likely a key data point for "limited wide threat" preceding Yamal's emergence |
| **Álvaro Morata** | Shot map, movement/reception map | xG, shots, aerial duels, hold-up passes received | Focal point striker | Test whether service quality or finishing was the bigger issue (feeds Group D directly) |

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 7 — EURO 2024: WHAT CHANGED?

Apply the exact Group A–F metric set from Part 2 to the 2024 dataset (Notebook 11) and test each claim below — do not assume:

- **Greater verticality / directness** → compare forward-pass ratio and directness index, 2022 vs. 2024
- **Greater transition threat** → compare Group F metrics directly
- **Improved wing play** → compare final-third entry zones and wide carry/dribble volumes
- **Higher attacking threat / more dangerous chances** → compare xG/shot and xG timelines
- **Improved pressing** → compare PPDA and high-recovery-to-shot times
- **Greater width** → compare touch-distribution-by-width (Viz 19) — this is one of the more commonly overstated claims in media coverage and deserves genuine scrutiny
- **More dynamic movement / more effective full-backs** → compare full-back progressive actions and overlap frequency
- **Better central progression** → compare central vs. wide progressive pass/carry share

Present every one of these as a paired before/after chart (Viz 16), not just prose description.

---
below whatever is mentioned is just my understanding i want more through investigation and more visualizations so dont limit yourself whatever i am mentioning below about the players and stuff is just my understanding dont limit ursef to what i say the data should speak and give answers not what i said 
# PART 8 — PLAYER EVOLUTION (2022 → 2024)

This is the most important analytical section — it's where the paper answers "was it the tactics or the players?"

| Player | Analyses to Run | What It Should Reveal |
|---|---|---|
| **Lamine Yamal** | Touch map, carry/dribble map, xG chain involvement, reception locations | New profile entirely (didn't exist in 2022) — quantify his direct-carrying threat as a structural addition, not a replacement of like-for-like |
| **Nico Williams** | Same as above | Same purpose — the "inverted winger who carries" archetype largely absent in 2022's wide options |
| **Rodri** | 2022 vs. 2024 pass network position, progressive passes, defensive actions | Did his individual role change, or did the players around him change what his passes led to? Critical for isolating H8 vs. H9 |
| **Pedri** | 2022 vs. 2024 progressive carries, xG chain involvement | Test whether he became more central to progression or was simply healthier/more available |
| **Dani Olmo** | 2022 vs. 2024 touch map, xA, positional heatmap | Did his role shift from primary creator to secondary option as Yamal/Williams took over the creative burden? |

Recommended framing: build a single composite visualization (small multiples) showing each returning player's heatmap/output side-by-side, 2022 vs. 2024, directly above the new-personnel (Yamal/Williams) visualizations. This makes the "personnel vs. tactics" argument visually self-evident before a word of text explains it.

---

# PART 9 — FINAL STORY ARC (MAPPED TO GROUPS & VISUALS)

1. **Spain dominated possession** — Group A / Viz 1
2. **The possession lacked attacking threat** — Groups C & D / Viz 4, 6, 7, 8
3. **Data reveals exactly why** — Groups B, E, F, G / Viz 2, 3, 9–14
4. **Spain changed key tactical principles** — Group I / Viz 16
5. **New player profiles transformed the attack** — Group J / Viz 17, 18
6. **Euro 2024 demonstrates those tactical improvements** — Group I / Viz 16, 19
7. **Conclude with an evidence-based explanation** — Group K / Viz 20 (hypothesis scorecard)

This mapping is the paper's skeleton: every claim in the narrative has a named group, notebook, and visualization behind it, so nothing in the final draft will be asserted without a traceable data source.

---

## Practical Notes Before You Start

- **Data availability check first:** confirm StatsBomb Open Data actually includes 360 (freeze-frame) data for the Spain matches you need — it's not uniformly available across all matches/competitions, and several of the harder visualizations (pressure success, transition numbers-behind-the-ball) depend on it. If it's missing for some matches, note this as a limitation rather than skipping the analysis silently.
- **Match selection:** decide up front whether "Spain 2022" means all group + knockout matches or a curated subset (e.g., excluding the Costa Rica blowout, which will skew several metrics). Recommend analyzing all matches but flagging outliers explicitly.
- **Consistent zone/metric definitions across tournaments** are essential — define "progressive pass," "final third," and "half-space" once in Notebook 03 and reuse those exact functions everywhere, so 2022 and 2024 numbers are genuinely comparable.
- **Keep the hypothesis scorecard visible from the start** — update it as you complete each notebook rather than writing it retroactively; this is what will keep the paper's tone analytical rather than narrative-driven.

Throughout the project, prioritize clarity over complexity.

If a simpler metric or visualization explains the tactical idea better than a more advanced one, prefer the simpler approach.

The final paper should be understandable to football fans while remaining rigorous enough for football analytics readers.