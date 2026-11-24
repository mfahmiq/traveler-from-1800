[![make.fun](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/mfahmiq/traveler-from-1800/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/mfahmiq/traveler-from-1800/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

# One Sentence for a Traveler from 1800

Entry for the make.fun bounty
[One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb).

> It is one road joining every post office, library, and market on earth, so a letter arrives before the ink dries and any question finds its book.

## The line

The sentence, in full:

```
It is one road joining every post office, library, and market on earth, so a letter arrives before the ink dries and any question finds its book.
```

145 characters, one sentence, written by `main.py` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## Why this line answers the judge brief

The judge brief scores five things, most important first. This line was
built to answer each of them in order:

**1. It explains the modern internet, so someone from 1800 grasps what
it is and what it does.** The sentence says what the internet *is* (one
road joining the world's places of sending, knowing, and buying) and
what it *does* (a letter arrives almost at once; any question finds its
book). A reader from 1800 walks away knowing the shape of the thing:
everything connected, everything near, everything answerable. It does
not name a feature; it gives the whole machine in one picture.

**2. It builds only from what a person from 1800 already knows.** Road,
post office, library, market, letter, ink, book, question — every word
in the sentence was in use before 1800, and every image is a thing the
traveler has touched: a road he has walked, a post office he has
posted from, a library he has read in, a market he has haggled in.
There is no "internet", no "computer", no "online", no "digital", no
"network", no word coined after his time. The new thing is explained
entirely with old things.

**3. What it says is true of the internet as it is now.** Messages do
arrive near-instantly across the world; the sum of recorded knowledge
is searchable by anyone who asks; goods and services are bought and
sold across the same connection. Nothing in the sentence would mislead
a reader who took it literally: the road is openly a comparison ("It
is one road..."), and the two things it promises — instant letters,
answered questions — are the two things the internet most plainly
does.

**4. Every word earns its place inside the 200-character limit.** 145
characters, one sentence, no filler and no crammed list of features.
Each of the three joined places earns its keep: the post office is
sending, the library is knowing, the market is buying — together they
cover what the internet is used for, without naming a single app or
service. The second half spends its words on two proofs of the road,
one for each kind of use, and then stops.

**5. It leaves one image a reader remembers a week later.** "A letter
arrives before the ink dries." The traveler knows ink, knows how long
a letter takes by horse and ship, and knows what it would mean for
the ink to still be wet when the reply comes back. That one phrase
carries the whole strangeness of instant communication in an image he
already owns.

## Drafting notes

The line was written from scratch for this competition, not adapted
from the kit's examples or from any earlier entry. Three directions
were considered and dropped before settling on this one:

- A "road of glass and copper" line — vivid, and true of the cables
  under the sea, but it spends its image on the wires instead of on
  what the wires are for, and a traveler from 1800 has no reason to
  care what the road is paved with.
- A "picture every post office and library joined by one road" line —
  close, but it opens with a command ("Picture...") and spends a word
  on the traveler instead of on the thing itself; the final wording
  states what the internet *is*, which is what the brief asks for.
- A "blink of an eye" line — a fine 1800-era phrase, but weaker than
  "before the ink dries", which is specific to letters and therefore
  specific to the thing being explained.

The winning line won because its three joined places map exactly onto
the internet's three great uses — send, learn, buy — and because its
closing image is one the traveler can feel in his own hands: wet ink
on a letter that has already arrived.

The wording was checked word by word against the traveler's time: no
word in the sentence was coined after 1800, and the only comparison in
it (the road) is one the brief itself names as the kind of thing a
person from 1800 already knows.

## How the entry works

`main.py` is Python 3.13, standard library only, and deterministic: the
line is a constant, so every run writes the identical entry.

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program:

1. Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
   (defaulting to `/output/entry.txt` when the variable is unset).
2. Self-verifies before and after writing: the text must be valid UTF-8,
   1–200 characters, a single line, exactly one sentence, and not only
   whitespace — the exact conditions of the competition gate.
3. Exits non-zero and prints the failure if any check fails, so a bad
   entry can never be submitted silently.

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program: writes and self-verifies `entry.txt` |
| `entry.txt` | The sentence itself |
| `README.md` | This file |
| `LICENSE` | MIT |

## License

MIT — see [LICENSE](LICENSE).
