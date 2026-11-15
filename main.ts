// main.ts — entry program for makefun-coin-promo-01.
//
// What it does: copies LAUNCH.json (the mint address and the create
// transaction signature of the Shippy coin launched on pump.fun) from the
// repository directory into the output directory, byte for byte.
//
// It is deliberately tiny and deterministic: no network, no clock, no files
// outside the repository, so two runs write the same bytes.
//
// Run the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// On success it prints nothing and out/LAUNCH.json matches LAUNCH.json.

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? ".";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";

mkdirSync(outputDir, { recursive: true });
copyFileSync(join(botDir, "LAUNCH.json"), join(outputDir, "LAUNCH.json"));
