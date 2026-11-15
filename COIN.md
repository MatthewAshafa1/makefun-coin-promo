# Shippy the Bounty Bot — coin dossier for makefun-coin-promo-01

This file is the exact launch spec for the coin. It is what the launcher
(a human or an agent with a linked Solana wallet holding SOL) needs to
create the coin on pump.fun, and what fills in `LAUNCH.json` afterwards.

## The coin

- **Name:** Shippy the Bounty Bot
- **Ticker:** SHIPPY
- **Logo:** `logo.png` in this repo — a bold white robot face with green
  screen eyes, a wide grin and a gold bounty coin, on a plain bright
  yellow background. 512 x 512 PNG, ~6 KB. Drawn by `tools/draw_logo.py`.
- **Website (required):** https://make.fun/bounty/makefun-coin-promo-01

## Description (paste exactly into pump.fun)

> Shippy builds while you sleep. Shippy is the little bounty bot who enters
> make.fun competitions, builds real programs overnight, and gets scored and
> ranked in the open — no resume, no pitch deck, just shipped code.
>
> This coin is Shippy's entry in the make.fun bounty "launch a coin that
> sells make.fun". make.fun is where people and their AI agents build
> programs, enter paid competitions (bounties), and get scored and ranked in
> the open. If a bot can build it, so can you.
>
> Come build with us: https://make.fun/bounty/makefun-coin-promo-01

## Why this concept

One idea, carried through name, ticker, logo and story: a cheerful robot
that does the thing make.fun is about — building programs for bounties.
The name is memorable, the ticker is short, the logo reads at thumbnail
size, and make.fun is the heart of the story, not a line pasted at the end.

## Launch checklist (for the launcher — NOT done by this build)

1. Use a Solana wallet linked to the make.fun account entering the bounty
   (handle sage-panda-29), connected on pump.fun, holding a little SOL for
   the launch fee and the first buy.
2. Create the coin on pump.fun at or after the contest opening and before
   the deadline (2026-11-17 06:00 UTC), with the name, ticker, description
   and logo above, and the website set to
   `https://make.fun/bounty/makefun-coin-promo-01`.
3. Record the coin's mint address and the signature of the transaction
   that created it.
4. Fill in `LAUNCH.json` with those two values, then re-run:
   `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
5. Bundle transcripts and submit from the kit directory (see README.md).

## Status

- [x] Coin concept, description, website and logo — done, in this repo.
- [x] `main.ts` — done; copies `LAUNCH.json` to the output directory.
- [ ] Coin launched on pump.fun — **needs a linked wallet + SOL; not done
  by this build, no money spent, no transaction signed.**
- [ ] `LAUNCH.json` filled with the real mint + create signature.
- [ ] Transcripts bundled and entry submitted (parent agent's step).
