# ai-happy-01 — The Happiest Puppy

A golden retriever puppy laughing with its eyes squeezed shut in delight,
a tiny orange butterfly landing on its nose, in a sunlit wildflower meadow
at golden hour. Made to make the AI judge happy: warm light, a joyful
subject, and one small surprising moment of delight.

## How it works

`main.py` (Python 3, standard library only, no network) copies the image
`entry.png` in this repository to `/output/entry.png`. The output is
byte-identical on every run because it is a plain file copy.

Run locally (or with `/output` as the destination in the grader):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `entry.png` — the image (1024x683 PNG, under 1 MiB)
- `LICENSE` — MIT
