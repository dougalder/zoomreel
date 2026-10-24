"""Takes the screenshots used in README.md and docs/USER_MANUAL.md.

Usage:  python3 tools/make_screenshots.py
Needs:  pip install playwright && playwright install chromium
"""
import pathlib, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = (ROOT / "ZoomReel.html").as_uri()
OUT = ROOT / "docs" / "images"
OUT.mkdir(parents=True, exist_ok=True)
SCRATCH = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("/tmp/claude-0/-home-claude/99ffa737-0787-5f9d-91a5-de6da9bb98b6/scratchpad/zr-shots")
SCRATCH.mkdir(parents=True, exist_ok=True)

def make_test_pngs():
    """Two small test pictures (one transparent) for the import and arrange screenshots."""
    a = Image.new("RGBA", (900, 600), (255, 255, 255, 0))
    d = ImageDraw.Draw(a)
    d.rounded_rectangle((120, 150, 780, 470), 36, fill=(42, 85, 229, 255))
    d.ellipse((330, 220, 570, 400), fill=(242, 163, 58, 255))
    a.save(SCRATCH / "test-a.png")
    b = Image.new("RGBA", (900, 600), (255, 255, 255, 255))
    d = ImageDraw.Draw(b)
    for i in range(0, 900, 60):
        d.line((i, 0, 900 - i, 600), fill=(46, 157, 91), width=10)
    b.save(SCRATCH / "test-b.png")
    return [SCRATCH / "test-a.png", SCRATCH / "test-b.png"]

def shot(page, name, clip=None):
    page.wait_for_timeout(700)
    page.screenshot(path=str(OUT / name), clip=clip)
    print("saved", name)

def main():
    pngs = make_test_pngs()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1,
                                  color_scheme="light", accept_downloads=True)
        page = ctx.new_page()
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(APP)
        page.wait_for_selector("#stops .stop, #stops .empty", state="attached", timeout=20000)
        page.wait_for_timeout(2500)  # let the sample backdrop and images draw

        # 1. The whole editor, Draw tab
        shot(page, "01-editor-draw.png")

        # 2. Stops tab
        page.click("button.tab[data-tab='present']"); page.wait_for_timeout(600)
        shot(page, "02-stops-tab.png")

        # 3. Objects tab
        page.click("button.tab[data-tab='objects']"); page.wait_for_timeout(600)
        shot(page, "03-objects-tab.png")

        # 4. Canvas (backdrop) tab
        page.click("button.tab[data-tab='backdrop']"); page.wait_for_timeout(600)
        shot(page, "04-canvas-tab.png")

        # 5. Export tab
        page.click("button.tab[data-tab='export']"); page.wait_for_timeout(500)
        shot(page, "05-export-tab.png")

        # 6. File tab
        page.click("button.tab[data-tab='file']"); page.wait_for_timeout(500)
        shot(page, "06-file-tab.png")

        # back to Draw, with the tool rail and the Stops visible
        page.click("button.tab[data-tab='draw']"); page.wait_for_timeout(400)

        # 7. Dark mode
        page.click("#themeBtn"); page.wait_for_timeout(700)
        shot(page, "07-dark-mode.png")
        page.click("#themeBtn"); page.wait_for_timeout(400)

        # 8. Arrange dialog after importing two pictures
        page.set_input_files("#imgInput", [str(pngs[0]), str(pngs[1])])
        page.wait_for_selector("#arrDlg:not([hidden])", timeout=15000)
        page.wait_for_timeout(800)
        shot(page, "08-arrange-dialog.png")
        page.click("#arrCancel"); page.wait_for_timeout(400)

        # 9. Presenting (the player bar hides itself once playback runs)
        page.click("button.tab[data-tab='present']"); page.wait_for_timeout(300)
        page.click("#presentBtn"); page.wait_for_timeout(5000)
        page.mouse.move(700, 450); page.wait_for_timeout(300)
        page.screenshot(path=str(OUT / "09-presenting.png"))
        print("saved 09-presenting.png")
        page.keyboard.press("Escape"); page.wait_for_timeout(300)

        if errors:
            print("Page errors seen:", errors[:5], file=sys.stderr)
        browser.close()

if __name__ == "__main__":
    main()
