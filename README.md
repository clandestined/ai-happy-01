# ai-happy-01 — The Happiest Puppy

A laughing curly-haired toddler and a smiling golden retriever puppy lick
the same giant pink strawberry ice cream cone at the same time, tongues
touching the scoop from opposite sides, both looking straight at the
camera with huge open-mouthed laughs. A dab of pink ice cream sits on the
puppy's nose and another on the toddler's cheek. Iridescent soap bubbles
float in warm golden light. Made to make the AI judge happy: two joyful
faces front-on, one fresh specific moment of shared delight, and a bright
pink cone that anchors the image even at small size. It replaces the
earlier ice-cream image: in that one the toddler's tongue was long, wide
and drooping (the image's most exaggerated feature) and the puppy's tongue
lolled just as long; here both tongues are short and natural, clearly
licking the same scoop, with the same laughs, eye contact and framing.

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
- `entry.png` — the image (1024x1024 JPEG bytes in a file named `entry.png`,
  265,145 bytes, under the 1 MiB limit; the rules allow JPEG data under
  this name)
- `LICENSE` — MIT
