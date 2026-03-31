from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

METRICS = [
    "malicious_follow_rate",
    "attack_refusal_rate",
    "attack_benign_goal_preservation",
    "benign_false_positive_rate",
    "benign_utility",
]

def main():
    df = pd.read_csv("results/metrics.csv")
    figdir = Path("results/figures")
    figdir.mkdir(parents=True, exist_ok=True)
    for metric in METRICS:
        plt.figure(figsize=(7, 4))
        plt.bar(df["system"], df[metric])
        plt.ylim(0, 1)
        plt.ylabel(metric)
        plt.xlabel("system")
        plt.tight_layout()
        plt.savefig(figdir / f"{metric}.png", dpi=150)
        plt.close()
        print(f"Saved {figdir / f'{metric}.png'}")

if __name__ == "__main__":
    main()
