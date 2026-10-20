"""compute_calibration_mp1.py - W5 take-home helper, adapted for MP1.

The course's compute_calibration.py expects the capstone layout
(g001 ids, 3 dimensions, an answers.db SQLite table). MP1 is different:
- ids look like  j02-zero_shot  (snippet id + prompt strategy)
- the judge gives ONE score (1-4), not three
- the judge scores live in mp1_scored_cache.pkl, not a database

This script reads YOUR blind scores from docs/judge-calibration.md,
reads the JUDGE's scores from mp1_scored_cache.pkl, and prints:
- exact agreement   (same number)
- within-1 agreement (off by at most 1)
- every disagreement, with the model output so you can see why

Run it from inside the mp1 folder:
    python scripts/compute_calibration_mp1.py
"""
from __future__ import annotations

import argparse
import pickle
import re
from pathlib import Path

# Matches a table row like:  | j02-zero_shot | 3 | my note |
TABLE_ROW = re.compile(r"^\|\s*(j\d+)-(\w+)\s*\|\s*([1-4])\s*\|\s*(.*?)\s*\|?\s*$")


def parse_my_scores(path: str) -> dict[tuple[str, str], tuple[int, str]]:
    """Return {(snippet_id, strategy): (my_score, my_note)} from the markdown table."""
    scores = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW.match(line)
        if match:
            sid, strategy, score, note = match.groups()
            scores[(sid, strategy)] = (int(score), note)
    return scores


def load_judge_rows(pkl_path: str) -> dict[tuple[str, str], dict]:
    """Return {(snippet_id, strategy): row} from the MP1 scored cache."""
    rows = pickle.loads(Path(pkl_path).read_bytes())
    return {(r["snippet_id"], r["strategy"]): r for r in rows}


def main():
    parser = argparse.ArgumentParser(description="MP1 judge calibration agreement.")
    parser.add_argument("--calibration-file", default="docs/judge-calibration.md")
    parser.add_argument("--scored-cache", default="mp1_scored_cache.pkl")
    args = parser.parse_args()

    mine = parse_my_scores(args.calibration_file)
    if not mine:
        print(f"ERROR: no scored rows found in {args.calibration_file}")
        print("Fill the 'My score' column with 1-4, e.g.  | j02-zero_shot | 4 | note |")
        return

    judge = load_judge_rows(args.scored_cache)

    exact = within_1 = total = 0
    disagreements = []
    for key, (my_score, note) in mine.items():
        if key not in judge:
            print(f"WARNING: {key[0]}-{key[1]} not found in the cache, skipped")
            continue
        judge_score = judge[key]["llm_judge_score"]
        total += 1
        delta = abs(my_score - judge_score)
        if delta == 0:
            exact += 1
        if delta <= 1:
            within_1 += 1
        if delta >= 1:
            disagreements.append((key, my_score, judge_score, delta, note, judge[key]))

    print("\nCalibration summary (MP1)")
    print("-" * 25)
    print(f"  n scores            : {total}")
    print(f"  exact agreement     : {exact} / {total}  ({100 * exact / total:.0f}%)")
    print(f"  within-1 agreement  : {within_1} / {total}  ({100 * within_1 / total:.0f}%)")
    print(f"  disagreements       : {len(disagreements)}")
    for (sid, strategy), mine_s, judge_s, delta, note, row in disagreements:
        who = "I rated higher" if mine_s > judge_s else "judge rated higher"
        print(f"\n    {sid}-{strategy}: me={mine_s} / judge={judge_s} (delta={delta}). {who}.")
        print(f"      model output   : {row['extracted']}")
        print(f"      exact-match acc: {row['accuracy']}/3")
        print(f"      my note        : {note}")


if __name__ == "__main__":
    main()
