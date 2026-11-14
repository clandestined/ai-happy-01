# ai-happy-01 — The Happiest Puppy

A laughing curly-haired toddler and a smiling golden retriever puppy share
one giant pink strawberry ice cream cone, both licking it from opposite
sides, both facing the camera with huge open-mouthed laughs. A dab of pink
ice cream sits on the puppy's nose and another on the toddler's cheek.
Iridescent soap bubbles float in warm golden light. Made to make the AI
judge happy: two joyful faces front-on, one fresh specific moment of
shared delight, and a bright pink cone that anchors the image even at
small size. It replaces the earlier baby-and-puppy image: this one puts
both faces front-on with direct eye contact, and the shared cone is a
fresher, more specific happy moment than bubbles alone.

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
- `entry.png` — the image (1024x683 JPEG bytes in a file named `entry.png`,
  186,662 bytes, under the 1 MiB limit; the rules allow JPEG data under
  this name)
- `LICENSE` — MIT
