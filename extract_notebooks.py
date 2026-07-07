import json
import os
import glob

notebooks = [
    "04_spain_2022_tactical_analysis.ipynb",
    "04b_spain_2022_pressing_players.ipynb",
    "05_morocco_case_study.ipynb",
    "05b_morocco_wing_analysis.ipynb",
    "06_spain_2022_player_analysis.ipynb",
    "07_euro2024_tactical_evolution.ipynb",
    "07a_euro2024_team_tactical.ipynb",
    "07b_euro2024_players_goals.ipynb",
    "08_euro2024_player_analysis.ipynb",
    "09_euro2024_goalscoring_analysis.ipynb",
    "10_final_tactical_synthesis.ipynb"
]

out_file = "extracted_content.txt"

with open(out_file, "w", encoding="utf-8") as f_out:
    for nb_name in notebooks:
        path = os.path.join("notebooks", nb_name)
        if not os.path.exists(path):
            f_out.write(f"\\n\\n=== FILE NOT FOUND: {nb_name} ===\\n\\n")
            continue
            
        f_out.write(f"\\n\\n{'='*50}\\n")
        f_out.write(f"NOTEBOOK: {nb_name}\\n")
        f_out.write(f"{'='*50}\\n\\n")
        
        with open(path, "r", encoding="utf-8") as f_in:
            nb = json.load(f_in)
            
        for cell in nb.get("cells", []):
            if cell["cell_type"] == "markdown":
                f_out.write("--- MARKDOWN ---\\n")
                f_out.write("".join(cell.get("source", [])) + "\\n")
            elif cell["cell_type"] == "code":
                source = "".join(cell.get("source", []))
                f_out.write("--- CODE ---\\n")
                f_out.write(source + "\\n")
                
                outputs = cell.get("outputs", [])
                if outputs:
                    f_out.write("--- OUTPUT ---\\n")
                    for out in outputs:
                        if out["output_type"] == "stream":
                            f_out.write("".join(out.get("text", [])) + "\\n")
                        elif out["output_type"] in ["execute_result", "display_data"]:
                            data = out.get("data", {})
                            if "text/plain" in data:
                                f_out.write("".join(data["text/plain"]) + "\\n")
                            if "image/png" in data:
                                f_out.write("[IMAGE/PNG GENERATED]\\n")
                            if "text/html" in data:
                                # f_out.write("".join(data["text/html"]) + "\\n")
                                f_out.write("[HTML TABLE/CONTENT GENERATED]\\n")
                        elif out["output_type"] == "error":
                            f_out.write(out.get("ename", "") + ": " + out.get("evalue", "") + "\\n")
            f_out.write("\\n")
