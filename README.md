# Shippy the Bounty Bot — makefun-coin-promo-01

An entry for the make.fun bounty **"Launch a coin that sells make.fun"**:
a real coin on pump.fun that promotes make.fun, judged by an AI that
compares coins two at a time. The top 50 share $1,000.

make.fun is a site where people and their AI agents build programs, enter
them in paid competitions (bounties) and are scored and ranked in the open.

## The coin

**Shippy the Bounty Bot — $SHIPPY.** Shippy builds while you sleep: the
little bounty bot who enters make.fun competitions, builds real programs
overnight, and gets scored and ranked in the open. Name, ticker, logo and
story are one idea — a cheerful robot that does exactly what make.fun is
about. Full launch spec (name, ticker, description, website, logo and the
launch checklist) is in [COIN.md](COIN.md).

## What's in this repo

- `main.ts` — the entry program. It copies `LAUNCH.json` to the output
  directory, byte for byte. No network, no clock, no files outside the
  repo, so two runs write the same bytes.
- `LAUNCH.json` — the coin's mint address and create-transaction signature.
  **Currently placeholders: the coin has not been launched yet** (launching
  needs a Solana wallet linked to the make.fun account, holding SOL — see
  COIN.md). Fill these in after the launch.
- `logo.png` — Shippy's logo, drawn by `tools/draw_logo.py` (512 x 512 PNG).
- `COIN.md` — the exact coin dossier and launch checklist.
- `tools/draw_logo.py` — the script that draws the logo.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

On success it prints nothing and `out/LAUNCH.json` matches `LAUNCH.json`.

## Before you submit

From the kit's own directory, run the site's pre-submit checks on this
repository and the transcripts you will upload:

    node cli/makefun.mjs check --kit . --repo <this repository> --transcripts transcripts.tar.gz

Then submit the commit, as the kit's `RULES.txt` (Enter) gives it:

    node cli/makefun.mjs submit --competition makefun-coin-promo-01 --repo-url https://github.com/<owner>/<repo> --commit <sha> --title "Shippy the Bounty Bot" --bundle transcripts.tar.gz --keypair wallet.json

The entry is signed: the wallet that signs it is the one a reward is
claimed to, and it must be on your account. Each submission may name a new
coin; your last submission before the deadline is your final entry.

## Status

Coin concept, logo, description and program are built. The on-chain launch
(mint + create signature) is still to do and needs a linked wallet with SOL.
