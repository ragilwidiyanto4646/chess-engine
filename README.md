# chess-engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ragilwidiyanto4646/chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ragilwidiyanto4646/chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A single-file chess engine in 4,068 bytes of Python 3.13 stdlib: alpha-beta
with quiescence, MVV-LVA ordering, material + piece-square eval, iterative
deepening to depth 6 under a fixed 60,000-node budget per move. Full rules:
castling, en passant, promotion, checkmate/stalemate. Perft-verified 17/17.

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:8080 python3 main.py
```

It plays the gauntlet through the env: `POST /game {}` serves the game in
play, `POST /move {"game": n, "move": "<uci>"}` plays a move, and the loop
ends when the env answers status `"done"`. No clock in the search and no
randomness, so a replay plays the same moves. The driver tolerates a faulty
env answer (bad JSON, bad FEN, missing field, refused move) by resigning
that game or retrying, instead of crashing the trial. No model calls, no
other files, no dependencies.

---

<sub>Entered on [make.fun](https://make.fun/?ref=ztnjpsw2&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
