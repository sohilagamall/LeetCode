#!/usr/bin/env python3
"""
sort_problems.py

Sorts freshly-pulled LeetPush solution files (sitting at the repo root)
into topic folders, based on a problem-number -> topic mapping in
topics.json. Uses `git mv` so git records these as renames, not
delete+add pairs.

Usage:
    git pull
    python3 sort_problems.py            # move + stage, but don't commit
    python3 sort_problems.py --commit   # move + stage + commit

Filename convention expected (LeetPush default):
    <problem-number>-<Problem-Title>.cpp
e.g. 1310-XOR-Queries-of-a-Subarray.cpp -> problem number = "1310"

Add new mappings to topics.json as you encounter new problems, e.g.:
    "217": "Arrays_and_Hashing"
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
TOPICS_FILE = REPO_ROOT / "topics.json"
FILENAME_RE = re.compile(r"^(\d+)-.+\.(cpp|py|java|js|ts)$")


def load_topics() -> dict:
    if not TOPICS_FILE.exists():
        print(f"No topics.json found at {TOPICS_FILE}. Creating an empty one.")
        TOPICS_FILE.write_text("{}\n")
        return {}
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def find_root_solution_files():
    """Find solution files sitting loose at the repo root (not already in a topic folder)."""
    files = []
    for entry in REPO_ROOT.iterdir():
        if entry.is_file() and FILENAME_RE.match(entry.name):
            files.append(entry)
    return files


def git_mv(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["git", "mv", str(src.name), str(dest.relative_to(REPO_ROOT))],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  ! git mv failed for {src.name}: {result.stderr.strip()}")
        return False
    return True


def main():
    commit = "--commit" in sys.argv
    topics = load_topics()

    files = find_root_solution_files()
    if not files:
        print("No loose solution files found at repo root. Nothing to sort.")
        return

    moved = []
    unmapped = []

    for f in files:
        match = FILENAME_RE.match(f.name)
        number = match.group(1)
        topic = topics.get(number)

        if not topic:
            unmapped.append(f.name)
            continue

        dest = REPO_ROOT / topic / f.name
        print(f"Moving {f.name} -> {topic}/")
        if git_mv(f, dest):
            moved.append(f.name)

    if unmapped:
        print("\nThese files have no topic mapping yet (left at root):")
        for name in unmapped:
            number = FILENAME_RE.match(name).group(1)
            print(f'  "{number}": "???",   # {name}')
        print("Add these to topics.json, then re-run this script.")

    if not moved:
        print("\nNothing moved.")
        return

    if commit:
        msg = f"Organize {len(moved)} problem(s) into topic folders"
        subprocess.run(["git", "commit", "-m", msg], cwd=REPO_ROOT)
        print(f"\nCommitted: {msg}")
    else:
        print(f"\n{len(moved)} file(s) staged via git mv. Review with 'git status', then commit.")


if __name__ == "__main__":
    main()