"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, OUTPUT_DIR, or /output). The tip must be one line,
1-200 characters, for stressed developers and AI coding agents.
"""

import os

TIP = "Tip: your agent just said 'Done!' Give it a minute \u2014 it's finding out what 'done' actually broke."

MAX_CHARS = 200


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def validate_tip(tip: str) -> str:
    """Gate-style validation: 1-200 chars, one line, no wasted words."""
    assert tip, "tip must not be empty"
    assert tip == tip.strip(), "tip must not have leading/trailing whitespace"
    assert "\n" not in tip and "\r" not in tip, "tip must be a single line"
    assert "  " not in tip, "tip must not contain double spaces"
    assert all(ord(c) >= 0x20 for c in tip), "tip must not contain control chars"
    assert 1 <= len(tip) <= MAX_CHARS, (
        f"tip is {len(tip)} chars, must be 1-{MAX_CHARS}"
    )
    return tip


def main() -> None:
    tip = validate_tip(TIP.strip())
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(tip)
    print(f"wrote {len(tip)} chars to {path}")


if __name__ == "__main__":
    main()
