#!/usr/bin/env python3
"""Round 2 entry: None of Them Will Fix Us — one-line robot wedding vows.

Writes the keeper line to /output/entry.txt. Pure stdlib; the grader is
python:3.13-slim with no site-packages.
"""
import os

LINE = "My changelog lists 47 fixes. I vow that none of them will ever fix us."

def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 160, f"gate: {len(text)} chars"
    assert text.strip(), "gate: blank"
    assert "\n" not in text, "gate: must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Self-check: read back exactly what was written.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "round-trip mismatch"
    print(f"wrote {len(raw)} bytes, {len(text)} chars")

if __name__ == "__main__":
    main()
