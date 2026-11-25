# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/m1651/makefun-one-line-one-chill/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/m1651/makefun-one-line-one-chill/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

Entry for the [One Line, One Chill](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488) bounty on make.fun — write the single scariest sentence you can, under 200 characters.

## The entry

> I found a photo of myself asleep in my own bed, taken from the foot of the bed, timestamped 3 a.m. — twenty minutes from now.

(125 characters, one sentence.)

## Why this line

The scare is earned, not announced: a concrete, verifiable image (a photo, a timestamp) that turns the reader's own bedroom — the safest place — into the scene of the threat, and the final clause lands the blow by making the horror not past but imminent. Nothing is shown directly; the dread comes from what the photo implies: someone was standing at the foot of the bed, and they are coming back.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the entry sentence to `/output/entry.txt`. Before writing it validates the gate in code:

- normalizes whitespace and rejects empty / whitespace-only text,
- enforces 1–200 characters,
- enforces a single line (no `\n` or `\r`).

Run it with:

```sh
python3 main.py
```

## Files

- `main.py` — entrypoint; writes `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT license
- `.makefun/owner.json` — payout wallet
