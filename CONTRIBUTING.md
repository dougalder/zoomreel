# Contributing to ZoomReel

Thank you for helping. ZoomReel is written to be understood by people who are not programmers, so please keep explanations plain as well.

## Reporting a problem

1. Use the **Bug report** template in *Issues*.
2. Say which browser and version you used (Safari, Chrome or Edge, and the version number). The easiest way to find it is the browser's About menu.
3. Describe what you did, what you expected, and what happened instead.
4. If a video export failed, press **Copy details** in the error box and paste the text into the report. It contains the app version and the step where things stopped.
5. If you can, attach a small project file (saved from the File tab). Remove any private pictures first.

## Suggesting a change

Open an issue describing the problem you want solved, in everyday words, before writing code. It is easier to agree on the approach first.

## Making a change

1. Fork the repository and create a branch with a short descriptive name.
2. Edit `ZoomReel.html`. Keep everything in that one file.
3. Raise `APP_VERSION` in the script section (for example from `'1.54'` to `'1.55'`) and set `APP_BUILD` to today's date.
4. Add a short entry to the top of `CHANGELOG.md`.
5. If the change alters how something looks, run `python3 tools/make_screenshots.py` and commit the new images.
6. Test in Safari and Chrome at least. Check light mode, dark mode, and a narrow window.
7. Open a pull request using the template.

## Style

- Use plain English in the interface, the manual and the comments. Spell out any technical abbreviation the first time it appears (for example, MP4 is "MPEG-4 video file").
- Keep the app working offline apart from the two external resources listed in the README.
