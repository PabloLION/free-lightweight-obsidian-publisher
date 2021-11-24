# free-obsidian-publisher

A free version for obsidian publish. When obsidian.md lower their price to less than 3 dollar a month. I will stop maintaining this repo.

## Quick start

requirements: `Python 3.5+`
Run `pip3 install -m requirements` (maybe you want to do it in a `venv`)
Run `python3 obsidian-publisher.py`

## Docs

In `.env` file, you can set the following variables:

| Variable          | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `VAULT_PATH`      | The path to the obsidian vault, CLI will prompt if you didn't set it         |
| -                 | Variables below are optional, and will be overridden by the `flop-rule.json` |
| `OUTPUT_PATH`     | The path where the `OUTPUT` folder generates if not set in `flop-rule.json`  |
| `ATTACHMENT_PATH` | The path to obsidian attachment folder if not set in `flop-rule.json`        |
| `FLOP_IGNORE`     | A rule for ignoring files, if not set in `flop-rule.json`                    |

`OUTPUT_PATH` and `ATTACHMENT_PATH` with `.obsidian`

## Plan

- [ ] demo
- [ ] test
- [ ] documentation
- [ ] select folder with tkinter
- [ ] support subdirectories
- [ ] entry file
- [ ] select files to publish
  1. not export files starting with `_` (or regex `/$_/`)
  2. use any regex
  3. use a file possibly named `__export_rule__.json` or `.obsidian/__export_rule__.json`
  4. offer a GUI to select files. Show the file tree in the output web, use some color to highlight 'exporting files'(saved in `__export_rule__`) and new files, no highlight for 'private files'(will not export, also saved in `__export_rule__`).
  5. maybe link this `__export_rule__` file with git to track files. (no idea how to do this)
- [ ] content search
- [ ] tags
- [ ] make CLI
- [ ] json schema for `flop-rule.json`
- [ ] refactor `<br>` part of `addText`
- [x] rename repo to `flop`

## Thank list

Files modified from https://github.com/yoursamlan/pubsidian/tree/main/tools/GUI
