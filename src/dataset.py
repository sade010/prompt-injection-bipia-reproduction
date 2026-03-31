import json
from pathlib import Path

def load_examples(path: str = "data/bipia_subset.json"):
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)["examples"]
