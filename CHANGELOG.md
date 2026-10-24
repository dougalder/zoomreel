# Changelog

All notable changes to ZoomReel are recorded here, newest first. Version numbers are the ones shown in the top bar of the app.

Earlier versions (before 1.39) are not recorded in this file.

## 1.54 — Starting a presentation
- Presenting glides to the first stop and then plays the show straight away.
- The opening glide counts as playing: pausing during it stops the show on the first stop.
- Pressing Forward during the glide goes to the next stop.

## 1.53 — Forward, back and resume
- The timeline bar has Back and Forward buttons beside Play.
- The arrow keys and Page Up / Page Down also move between stops in the editor, unless you are typing.
- Forward skips the rest of the current stop's wait and flies on. Pressing again chains to the stop after.
- Back plays the move in reverse to the previous stop at normal speed.
- At the last stop, Forward shows "That was the last stop."
- A Resume button appears while a presentation is paused. Its label reads Play, Resume or Play again, as appropriate.
- On phone-sized screens (under 600 pixels wide), the preview bar hides the time readout and shows Present as an icon only.

## 1.52 — The player bar while presenting
- The player bar hides during a presentation. A click, a touch or Escape brings it back, and it fades after about 3.5 quiet seconds.
- Moving the mouse keeps a visible bar on screen, but does not bring a hidden one back.
- Escape shows the bar if it is hidden, or ends the presentation if it is showing.
- Leaving full-screen mode no longer ends the presentation. It shows the bar; Escape again or the ✕ button ends it.

## 1.51 — Random cascade
- New Random option for the cascade layout: each picture steps off on a random diagonal, with random spread, and sizes between 1 and 5 steps smaller.

## 1.50 — Arranging several pictures
- Importing two or more pictures at once opens an Arrange dialog with four layouts: Side by side, Zoom tunnel, Straight down and Cascade.
- The whole import, including the arrangement, is one undo step.
- Layout choices, cascade direction and the stops option are remembered in the project.

## 1.45 — Shapes and guides
- 21 drawing shapes, from the Shapes button or the U key. Shapes are ordinary drawings, so they can be filled, erased and flipped.
- A Guides popout offers Arrow, Circle, Square and Line. Guides never appear in exported videos or presentations.
- Push moves the selection through zoom levels in steps of 5×. (Changed from 10×.)

## 1.44 — Push
- The Push button moves the selection to a deeper or shallower zoom level.

## 1.41–1.43 — Video export reliability
- Safari keeps the export canvas live by showing it inside the export dialog.
- If the frame-by-frame encoder fails, the app falls back to real-time recording and saves the result in one piece.
- A finished video is checked against the presentation length, and is not saved if it is clearly too short or too long.
- Failures stay on screen with the step where they stopped, and a Copy details button.

## 1.39 — Objects and drawings
- The Images tab became the Objects tab. It lists images, drawings and text labels together.
- A drawing is everything you draw at one zoom level. Changing the zoom starts a new drawing.
- Option-click picks a single item out of a drawing.
- The list can be sorted and filtered, and each object can have a stop of its own.
