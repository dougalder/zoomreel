# ZoomReel Design Notes

These notes record decisions made while building ZoomReel, and the reasons for them. They are written for anyone who will change the app later, and they avoid technical shorthand where possible.

## Objects and drawings (version 1.39)

- The **Images** tab became **Objects**. It lists pictures, drawings and text labels together. Guides are not listed.
- A **drawing** is a named group of everything drawn on the Artwork layer at one zoom level. Brush strokes, shapes and fills all join the current drawing.
- Changing zoom, even slightly, starts a new drawing ("Drawing N"). Separate sketches made at the same zoom stay in one drawing.
- Option-click selects a single item inside a drawing. Option-drag does the same for a box selection.
- The list can be sorted, filtered (All, Images, Drawings, Text) and reordered by dragging.
- Projects saved before 1.39 have their loose marks gathered into drawings by zoom level when opened.
- Known trade-off: the Draw and Objects panels sit below the fold (below the visible part of the screen) on small screens.

## Presenting and stepping through stops (versions 1.52 to 1.54)

- **Starting (1.54):** Present glides to the first stop and then plays straight away. Pausing during that glide stops the show on the first stop. Forward pressed during the glide goes to the next stop.
- **Player bar (1.52):** the bar is hidden while presenting. A click, a tap or Escape brings it back, and it fades after about 3.5 seconds of quiet. Moving the mouse keeps a visible bar on screen but does not bring a hidden one back.
- **Escape and full screen (1.52):** Escape shows the bar if hidden, or ends the presentation if it is showing. Leaving full-screen mode no longer ends the presentation.
- **Resume (1.53):** appears whenever a presentation is paused. Its label reads Play, Resume or Play again, depending on where you are.
- **Forward and back (1.53):** Forward skips the rest of the current stop's hold and flies on. Back plays the move in reverse at normal speed. At the last stop, Forward says "That was the last stop."
- **Phone layout (1.53):** on screens narrower than 600 pixels, the time readout is hidden and Present becomes an icon, so the timeline keeps enough room.

## Arranging several imported pictures (versions 1.50 to 1.51)

- Importing two or more pictures at once opens an Arrange dialog. The whole import, including arrangement, is one undo step.
- Four layouts: **Side by side** (a grid), **Zoom tunnel** (each picture sits in the quietest spot of the one before, found by measuring brightness edges on a small copy), **Straight down** (each picture centred at one-ninth size inside the one before), and **Cascade** (each picture half the size of the last, stepping diagonally).
- **Cascade → Random (1.51):** each picture steps off on a random diagonal with random spread, and its size is a random one to five halvings (1× to 1/16×). The first picture stays full size. Each Arrange gives a new pattern. This reading of the size rule is an interpretation that has not yet been confirmed by the project owner.
- Arrangement choices and the stops option are remembered in the project.

## PowerPoint import: tried and withdrawn

- A PowerPoint (.pptx) import with editable text was built in two releases, both numbered 1.50 and 1.51. The project owner decided the direction was wrong, and the app was rolled back to 1.49 exactly.
- The four layouts were then reused for multi-picture import, released as the new 1.50.
- Projects saved by the PowerPoint builds still open, but wrapped text from imported slides shows as single long lines.

## Toolbar tools

- **Shapes (1.45):** 21 drawing shapes, opened from the Shapes button or the letter U. Shapes are ordinary strokes and fills, so they join drawings and accept Fill, the Eraser and flips.
- **Guides (1.45):** one button opens a pop-out with Arrow, Circle, Square and Line. Guides never appear in exports or presentations.
- **Push (1.44, 1.45):** moves the selection through zoom levels in steps of 5×. (The first version used 10×.) Click goes deeper; Option-click goes shallower.

## Video export (versions 1.41 to 1.43)

- Safari only keeps a drawing surface up to date while it is on screen, so the export canvas is shown as a live preview inside the export window.
- In Safari, frames are sent to the video encoder as raw pixels.
- If the frame-by-frame encoder fails, the app falls back to real-time recording and saves the result in one piece.
- A finished video is checked against the expected length and is not saved if it is far too short or too long.
- A failure stays on screen with the step where it stopped, and a Copy details button.

## Conventions

- Every release raises `APP_VERSION` in the script section. The version shows in the top bar and in the File tab, and project files record the version that saved them.
- Export file names follow the pattern `YYYY-MM-DD ZoomReel-[Name]-[Resolution].[ext]`.
- Target browsers: Safari on Mac and iOS first; Chrome and Edge also supported.
- Every version includes a light and dark mode switch.
