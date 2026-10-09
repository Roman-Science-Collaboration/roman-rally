#!/usr/bin/env python3
"""Build the Roman Rally invitation graphic.

Edit the text and URL constants below, then from the repository root:

    python3 -m pip install pillow segno opencv-python-headless fonttools brotli pyzbar
    python3 tools/make_invitation.py

pyzbar also needs the system library zbar (Debian/Ubuntu: libzbar0).

The script reads assets/images/roman-rally-banner.png, writes a WebP
next to it for the website, and writes:

    assets/images/roman-rally-invitation.jpg
    assets/images/roman-rally-invitation.png

It then checks that both QR codes in the JPG decode to RALLY_URL and HOST_URL.
HOST_URL must stay in step with the handbook heading id
`what-it-means-to-host-a-rally-room`.
Fonts are the site's Source Serif 4 and Source Sans 3 files in assets/fonts/.
"""

from __future__ import annotations

import io
import sys
import tempfile
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import segno

ROOT = Path(__file__).resolve().parents[1]
BANNER_PNG = ROOT / "assets" / "images" / "roman-rally-banner.png"
BANNER_WEBP = ROOT / "assets" / "images" / "roman-rally-banner.webp"
OUT_JPG = ROOT / "assets" / "images" / "roman-rally-invitation.jpg"
OUT_PNG = ROOT / "assets" / "images" / "roman-rally-invitation.png"
FONT_DIR = ROOT / "assets" / "fonts"

# Edit these when the date or the public URL changes.
RALLY_URL = "https://roman-science-collaboration.github.io/roman-rally/"
# Stable anchor on handbook.md. The heading id is set in HTML, not left to auto-ids.
HOST_URL = (
    "https://roman-science-collaboration.github.io/roman-rally/"
    "handbook/#what-it-means-to-host-a-rally-room"
)
TITLE = "Roman Rally"
DATES = "December 14-18, 2026"
PLACE = "Online and at in-person Rally Rooms at participating institutions"
# Separate paragraphs with a blank line. Each paragraph is wrapped on its own.
BODY = (
    "Spend a few days of hands-on, hackathon-style work together on early "
    "Nancy Grace Roman Space Telescope commissioning and first-look data.\n\n"
    "Bring a question, an idea, or a curiosity.\n\n"
    "The Rally is open to the Roman Science Collaboration and the Roman Forum community."
)
ORGANIZER = "Organized by the Roman Science Collaboration"
QR_CAPTION = "Scan to join the Rally"
HOST_TITLE = "Seeking Rally Hosts"
HOST_LINE = "Want to host a local Rally Room? Scan to learn what it takes."
CREDIT = "Illustration by Robyn"

W, H = 1200, 1500
MAX_JPG_BYTES = 400 * 1024

# Deep violet, pale lavender, and the banner sky (navy).
VIOLET = (79, 39, 116)       # #4f2774
LAVENDER = (228, 218, 242)   # #e4daf2
NAVY = (31, 42, 74)          # #1f2a4a
WHITE = (255, 255, 255)


def load_font(woff2_name: str, size: int, cache: dict[str, Path]) -> ImageFont.FreeTypeFont:
    src = FONT_DIR / woff2_name
    if src not in cache:
        tt = TTFont(src)
        tt.flavor = None
        dest = Path(tempfile.mkdtemp(prefix="rally-font-")) / (src.stem + ".ttf")
        tt.save(dest)
        cache[src] = dest
    return ImageFont.truetype(str(cache[src]), size=size)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if not current:
                raise SystemExit(f"Word does not fit: {word}")
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def text_height(font: ImageFont.FreeTypeFont, lines: int, leading: float) -> int:
    return int(round(lines * font.size * leading))


def draw_centered(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    y: int,
    leading: float,
) -> int:
    step = font.size * leading
    for line in lines:
        draw.text((W / 2, y), line, font=font, fill=fill, anchor="mt")
        y += step
    return int(round(y))


def draw_left(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    x: int,
    y: int,
    leading: float,
) -> int:
    step = font.size * leading
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill, anchor="lt")
        y += step
    return int(round(y))


def make_qr(url: str, dark: tuple[int, int, int], scale: int) -> Image.Image:
    code = segno.make(url, error="h", micro=False)
    # border=4 is the quiet zone, in modules.
    buf = io.BytesIO()
    code.save(
        buf,
        kind="png",
        scale=scale,
        border=4,
        dark="#%02x%02x%02x" % dark,
        light="#ffffff",
    )
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def wrap_url(draw: ImageDraw.ImageDraw, url: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    """Wrap a URL on slashes and the fragment, then hard-break a token if needed."""
    if draw.textlength(url, font=font) <= max_width:
        return [url]
    tokens: list[str] = []
    buf = ""
    for ch in url:
        # Keep "#" with the fragment so the anchor is not split off the hash.
        if ch == "#" and buf:
            tokens.append(buf)
            buf = ch
            continue
        buf += ch
        if ch == "/":
            tokens.append(buf)
            buf = ""
    if buf:
        tokens.append(buf)
    lines: list[str] = []
    current = ""

    def hard_break(token: str) -> list[str]:
        pieces: list[str] = []
        piece = ""
        for ch in token:
            trial = piece + ch
            if draw.textlength(trial, font=font) <= max_width:
                piece = trial
            else:
                if piece:
                    pieces.append(piece)
                piece = ch
        if piece:
            pieces.append(piece)
        return pieces

    for token in tokens:
        trial = current + token
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
            continue
        if current:
            lines.append(current)
            current = ""
        if draw.textlength(token, font=font) <= max_width:
            current = token
        else:
            broken = hard_break(token)
            lines.extend(broken[:-1])
            current = broken[-1]
    if current:
        lines.append(current)
    return lines


def matched_qr_scales(url_a: str, url_b: str, max_side: int = 292) -> tuple[int, int]:
    """Integer scales so the two codes are nearly the same size and still sharp."""
    count_a = segno.make(url_a, error="h").symbol_size(scale=1, border=4)[0]
    count_b = segno.make(url_b, error="h").symbol_size(scale=1, border=4)[0]
    best: tuple[tuple[int, int], int, int] | None = None
    for scale_a in range(4, 11):
        for scale_b in range(4, 11):
            side_a = count_a * scale_a
            side_b = count_b * scale_b
            if max(side_a, side_b) > max_side or min(side_a, side_b) < 200:
                continue
            # Prefer equal sizes, then larger codes.
            score = (abs(side_a - side_b), -min(side_a, side_b))
            if best is None or score < best[0]:
                best = (score, scale_a, scale_b)
    if best is None:
        raise SystemExit("Could not fit two QR codes at a scannable size.")
    return best[1], best[2]


def draw_centered_at(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    center_x: float,
    y: int,
    leading: float,
) -> int:
    step = font.size * leading
    for line in lines:
        draw.text((center_x, y), line, font=font, fill=fill, anchor="mt")
        y += step
    return int(round(y))


def write_webp(banner: Image.Image) -> None:
    banner.save(BANNER_WEBP, format="WEBP", quality=80, method=6)


def compose(fonts: dict[str, ImageFont.FreeTypeFont]) -> Image.Image:
    banner = Image.open(BANNER_PNG).convert("RGB")
    if banner.size != (973, 314):
        print(f"Note: banner is {banner.size}, expected 973x314. Scaling to full width anyway.")
    banner_h = round(banner.height * W / banner.width)
    banner = banner.resize((W, banner_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (W, H), WHITE)
    canvas.paste(banner, (0, 0))
    draw = ImageDraw.Draw(canvas)

    bar = 8
    draw.rectangle((0, banner_h, W, banner_h + bar), fill=VIOLET)
    draw.rectangle((0, H - bar, W, H), fill=NAVY)

    side = 96
    body_width = W - side * 2
    place_width = W - 160

    place_lines = wrap_text(draw, PLACE, fonts["place"], place_width)
    paragraphs = [wrap_text(draw, part, fonts["body"], body_width) for part in BODY.split("\n\n")]

    credit_h = text_height(fonts["credit"], 1, 1.3)
    title_h = text_height(fonts["title"], 1, 1.02)
    date_h = text_height(fonts["date"], 1, 1.2)
    place_h = text_height(fonts["place"], len(place_lines), 1.3)
    para_gap = 14
    body_h = sum(text_height(fonts["body"], len(lines), 1.38) for lines in paragraphs)
    body_h += para_gap * (len(paragraphs) - 1)
    org_h = text_height(fonts["org"], 1, 1.25)
    band_pad = 16

    margin = 44
    col_gap = 22
    col_w = (W - margin * 2 - col_gap) // 2
    inner_w = col_w - 36
    scale_join, scale_host = matched_qr_scales(RALLY_URL, HOST_URL, max_side=min(288, inner_w - 8))
    qr_join = make_qr(RALLY_URL, VIOLET, scale_join)
    qr_host = make_qr(HOST_URL, NAVY, scale_host)
    qr_side = max(qr_join.width, qr_join.height, qr_host.width, qr_host.height)

    join_title = wrap_text(draw, QR_CAPTION, fonts["caption"], inner_w)
    host_title = wrap_text(draw, HOST_TITLE, fonts["caption"], inner_w)
    host_sub = wrap_text(draw, HOST_LINE, fonts["qr_sub"], inner_w)
    join_url = wrap_url(draw, RALLY_URL, fonts["url"], inner_w)
    host_url = wrap_url(draw, HOST_URL, fonts["url"], inner_w)
    header_h = max(
        text_height(fonts["caption"], len(join_title), 1.15),
        text_height(fonts["caption"], len(host_title), 1.15)
        + 6
        + text_height(fonts["qr_sub"], len(host_sub), 1.25),
    )
    url_h = max(
        text_height(fonts["url"], len(join_url), 1.25),
        text_height(fonts["url"], len(host_url), 1.25),
    )
    card_pad = 14
    qr_block_h = card_pad + header_h + 10 + qr_side + 8 + url_h + card_pad

    # These base gaps are the same numbers added into `fixed` below.
    top_gap = 18
    gap_after_credit = 12
    gap_after_title = 12
    gap_after_rule = 14
    gap_after_band = 16
    gap_before_org = 12
    gap_before_qr = 14
    gap_after_url = 14
    rule_h = 4
    fixed = (
        top_gap
        + credit_h
        + gap_after_credit
        + title_h
        + gap_after_title
        + rule_h
        + gap_after_rule
        + band_pad
        + date_h
        + 8
        + place_h
        + band_pad
        + gap_after_band
        + body_h
        + gap_before_org
        + org_h
        + gap_before_qr
        + qr_block_h
        + gap_after_url
    )
    content_top = banner_h + bar
    content_bottom = H - bar
    extra = (content_bottom - content_top) - fixed
    if extra < 0:
        raise SystemExit(f"Invitation text overflows the canvas by {-extra} px. Shorten the copy or the type.")

    # Share leftover space across the stack so one gap does not open into a hole.
    share = extra // 4
    gap_after_credit += share
    gap_after_band += share
    gap_before_qr += share
    gap_after_url += share + (extra - share * 4)

    y = content_top + top_gap
    y = draw_centered(draw, [CREDIT], fonts["credit"], VIOLET, y, 1.3)
    y += gap_after_credit
    y = draw_centered(draw, [TITLE], fonts["title"], VIOLET, y, 1.02)
    y += gap_after_title
    rule_w = 112
    draw.rectangle(((W - rule_w) / 2, y, (W + rule_w) / 2, y + rule_h), fill=VIOLET)
    y += rule_h + gap_after_rule

    band_top = y
    text_y = y + band_pad
    text_y = draw_centered(draw, [DATES], fonts["date"], VIOLET, text_y, 1.2)
    text_y += 8
    text_y = draw_centered(draw, place_lines, fonts["place"], NAVY, text_y, 1.3)
    band_bottom = text_y + band_pad
    # Paint the band first, then the type, so the fill does not cover the words.
    draw.rectangle((0, band_top, W, band_bottom), fill=LAVENDER)
    text_y = band_top + band_pad
    text_y = draw_centered(draw, [DATES], fonts["date"], VIOLET, text_y, 1.2)
    text_y += 8
    text_y = draw_centered(draw, place_lines, fonts["place"], NAVY, text_y, 1.3)
    y = band_bottom + gap_after_band

    for i, lines in enumerate(paragraphs):
        y = draw_left(draw, lines, fonts["body"], NAVY, side, y, 1.38)
        if i != len(paragraphs) - 1:
            y += para_gap
    y += gap_before_org
    y = draw_centered(draw, [ORGANIZER], fonts["org"], VIOLET, y, 1.25)
    y += gap_before_qr

    def paste_qr(qr: Image.Image, box: tuple[int, int, int, int]) -> None:
        framed = Image.new("RGB", (qr_side, qr_side), WHITE)
        framed.paste(qr, ((qr_side - qr.width) // 2, (qr_side - qr.height) // 2))
        left = box[0] + (col_w - qr_side) // 2
        canvas.paste(framed, (left, box[1]))

    cards = (
        (margin, VIOLET, join_title, [], join_url, qr_join),
        (margin + col_w + col_gap, NAVY, host_title, host_sub, host_url, qr_host),
    )
    card_bottom = y + qr_block_h
    for left, accent, title_lines, sub_lines, url_lines, qr in cards:
        box = (left, y, left + col_w, card_bottom)
        draw.rounded_rectangle(box, radius=16, outline=accent, width=3)
        center = left + col_w / 2
        text_y = y + card_pad
        title_bottom = draw_centered_at(draw, title_lines, fonts["caption"], accent, center, text_y, 1.15)
        if sub_lines:
            draw_centered_at(draw, sub_lines, fonts["qr_sub"], NAVY, center, title_bottom + 6, 1.25)
        qr_top = y + card_pad + header_h + 10
        paste_qr(qr, (left, qr_top, left + col_w, qr_top + qr_side))
        url_top = qr_top + qr_side + 8
        draw_centered_at(draw, url_lines, fonts["url"], NAVY, center, url_top, 1.25)
    y = card_bottom + gap_after_url
    if y > content_bottom + 1:
        raise SystemExit(f"Layout ran past the bottom rule (y={y}, limit={content_bottom}).")
    return canvas


def save_outputs(canvas: Image.Image) -> None:
    canvas.save(OUT_PNG, format="PNG", optimize=True)
    # 4:4:4 subsampling keeps the QR modules from being smeared.
    chosen = None
    for quality in (90, 86, 82, 78, 74, 70):
        buf = io.BytesIO()
        canvas.save(buf, format="JPEG", quality=quality, subsampling=0, optimize=True)
        size = buf.tell()
        if size <= MAX_JPG_BYTES:
            OUT_JPG.write_bytes(buf.getvalue())
            chosen = (quality, size)
            break
    if chosen is None:
        raise SystemExit(f"Could not fit the invitation under {MAX_JPG_BYTES} bytes.")
    print(f"Wrote {OUT_JPG.relative_to(ROOT)} ({chosen[1]} bytes, quality {chosen[0]})")
    print(f"Wrote {OUT_PNG.relative_to(ROOT)} ({OUT_PNG.stat().st_size} bytes)")


def decode_qr(path: Path) -> list[str]:
    import cv2
    from pyzbar.pyzbar import decode

    pil = Image.open(path).convert("RGB")
    pyzbar_vals = [item.data.decode("utf-8") for item in decode(pil)]

    bgr = cv2.imread(str(path))
    detector = cv2.QRCodeDetector()
    opencv_vals: list[str] = []
    ok, decoded, _points, _straight = detector.detectAndDecodeMulti(bgr)
    if ok and decoded:
        opencv_vals = [item for item in decoded if item]
    if not opencv_vals:
        single, _pts, _straight = detector.detectAndDecode(bgr)
        if single:
            opencv_vals = [single]
    expected = {RALLY_URL, HOST_URL}
    print(f"pyzbar: {pyzbar_vals or 'none'}")
    print(f"opencv: {opencv_vals or 'none'}")
    if set(pyzbar_vals) != expected or len(pyzbar_vals) != 2:
        raise SystemExit(f"pyzbar did not decode both exact URLs in {path.name}.")
    if set(opencv_vals) != expected or len(opencv_vals) != 2:
        raise SystemExit(f"OpenCV QRCodeDetector did not decode both exact URLs in {path.name}.")
    return pyzbar_vals


def main() -> None:
    if not BANNER_PNG.is_file():
        raise SystemExit(f"Missing banner: {BANNER_PNG}")
    banner = Image.open(BANNER_PNG).convert("RGB")
    write_webp(banner)
    print(f"Wrote {BANNER_WEBP.relative_to(ROOT)} ({BANNER_WEBP.stat().st_size} bytes)")

    cache: dict[str, Path] = {}
    fonts = {
        "credit": load_font("source-serif-4-400-italic.woff2", 22, cache),
        "title": load_font("source-serif-4-600.woff2", 84, cache),
        "date": load_font("source-sans-3-600.woff2", 34, cache),
        "place": load_font("source-sans-3-400.woff2", 28, cache),
        "body": load_font("source-serif-4-400.woff2", 28, cache),
        "org": load_font("source-sans-3-600.woff2", 24, cache),
        "caption": load_font("source-sans-3-600.woff2", 22, cache),
        "qr_sub": load_font("source-sans-3-400.woff2", 18, cache),
        "url": load_font("source-sans-3-400.woff2", 16, cache),
    }
    canvas = compose(fonts)
    save_outputs(canvas)
    decode_qr(OUT_JPG)
    print("QR check passed:")
    print(" ", RALLY_URL)
    print(" ", HOST_URL)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
