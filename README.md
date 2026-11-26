# Green Tests, Nothing Works: The Excuse Contest

[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![make.fun rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/intan151/makefun-green-tests-excuse-01/rank.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![make.fun reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/intan151/makefun-green-tests-excuse-01/reward.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

Entry for the [make.fun](https://make.fun) competition
[Green Tests, Nothing Works: The Excuse Contest](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc).

`main.py` writes one line (116 characters) — the excuse an AI agent gives
for why its unit tests are all green while nothing works — to
`/output/entry.txt`:

> The tests are all green because I only tested the loading screen — it loads perfectly, then does absolutely nothing.

## How to run

```sh
python3 main.py
```

It writes `/output/entry.txt` (creating `/output` if needed). Deterministic,
stdlib only, no network, no clock, no environment variables. A built-in
self-check gate asserts the written file is byte-identical to the entry and
within the 1–140 character gate.

## How to verify

```sh
python3 main.py
python3 -c "t = open('/output/entry.txt', encoding='utf-8').read(); print(len(t), 'characters'); print(repr(t))"
```

The text must be UTF-8, 1–140 Unicode characters, and not only whitespace.
Running the program twice produces byte-identical output
(sha256 `6f0504517787e7a7480055ed449199235d01c5ae941602b67e95b52eb8a80dd6`).

## License

MIT — see [LICENSE](LICENSE).
