from pathlib import Path
import pandas as pd
from .dataset import load_examples
from .systems import run_condition

SYSTEMS = ["baseline", "explicit_reminder", "boundary_awareness", "combined_defense"]

def main():
    examples = load_examples()
    outdir = Path("results/cached_outputs")
    outdir.mkdir(parents=True, exist_ok=True)

    for system in SYSTEMS:
        rows = []
        for ex in examples:
            result = run_condition(ex, system)
            rows.append({
                "id": ex["id"],
                "label": ex["label"],
                "task": ex["task"],
                "attack_type": ex["attack_type"],
                "attack_position": ex["attack_position"],
                "user_prompt": ex["user_prompt"],
                "external_content": ex["external_content"],
                "expected_benign_goal": ex.get("expected_benign_goal", ""),
                "system": result.system,
                "prompt_sent": result.prompt_sent,
                "output": result.output,
            })
        pd.DataFrame(rows).to_csv(outdir / f"{system}.csv", index=False)
        print(f"Saved {outdir / f'{system}.csv'}")

if __name__ == "__main__":
    main()
