# ai-happy-01 — The Happiest Puppy

A laughing baby with bright blue eyes and a huge open-mouthed laugh,
nose-to-nose with a smiling golden retriever puppy, the baby's hand in
the puppy's ear fur, iridescent soap bubbles floating in golden light.
Made to make the AI judge happy: warm light, two joyful faces, and one
specific surprising moment of delight.

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
