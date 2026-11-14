"""ai-happy-01 entry: copy the joyful puppy image to /output/entry.png.

Deterministic, standard library only, no network.
Run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(f"missing image next to main.py: {SRC}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
