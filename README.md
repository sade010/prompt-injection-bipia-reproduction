# A Small-Scale Reproduction of Indirect Prompt Injection Defenses on a BIPIA-Inspired Subset

This repository contains the final seminar project submission. It is a small-scale, literature-based reproduction study on indirect prompt injection.

## Project scope

The project compares four conditions on a curated BIPIA-inspired subset:

- `baseline`
- `explicit_reminder`
- `boundary_awareness`
- `combined_defense`

The goal is to evaluate whether black-box defenses reduce malicious instruction following while preserving the benign user task.

## Repository contents

- `data/bipia_subset.json`: curated benchmark subset
- `data/sampling_protocol.md`: subset construction protocol
- `src/`: execution and evaluation code
- `results/cached_outputs/*.csv`: cached model outputs for all conditions
- `results/metrics.csv`: final summary metrics
- `results/figures/*.png`: generated plots
- `report/main.tex`: paper source for Overleaf

## Important

The repository already includes final cached outputs, metrics, and figures.  
The project can therefore be inspected without rerunning any API calls.

## Setup

```bash
py -3.11 -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt