#!/usr/bin/env python3

import re
import sys
from pathlib import Path

def fix_colon_spacing_and_remove_bom(file_path: Path):
    # Read raw bytes first, to detect BOM
    raw = file_path.read_bytes()
    BOM = b"\xef\xbb\xbf"
    if raw.startswith(BOM):
        print(f"Removing BOM from {file_path}")
        raw = raw[len(BOM):]
        file_path.write_bytes(raw)

    # Now open as UTF-8 text
    with file_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    with file_path.open("w", encoding="utf-8") as f:
        for line in lines:
            # Skip comments
            if line.strip().startswith("//") or line.strip().startswith("/*"):
                f.write(line)
                continue
            # Replace "key": value with "key" : value
            line = re.sub(r'(".*?")\s*:\s*', r'\1 : ', line)
            f.write(line)

def process_all_json_files():
    for path in Path(".").rglob("*.json"):
        if str(path).startswith("./.git") or not path.is_file():
            continue
        print(f"Postprocessing: {path}")
        fix_colon_spacing_and_remove_bom(path)

if __name__ == "__main__":
    process_all_json_files()
