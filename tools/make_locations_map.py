"""Add the new Rally Room sites to the Roman Rally locations map.

Run from the repository root:

    python tools/make_locations_map.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

IMAGES = Path(__file__).resolve().parent.parent / 'assets' / 'images'
BASE_MAP = IMAGES / 'roman-rally-locations-base.jpg'
OUT_MAP = IMAGES / 'roman-rally-locations.png'

# Supersampling factor for crisp text and dots at the map's native size.
SS = 4

FUTURA = '/System/Library/Fonts/Supplemental/Futura.ttc'
AVENIR = '/System/Library/Fonts/Avenir Next.ttc'

# Colors sampled from the original map.
YELLOW = (229, 230, 109, 255)
WHITE = (240, 250, 255, 255)
BOX_FILL = (49, 53, 116, 235)
BOX_HEADER = (155, 185, 233, 255)


def get_font(path, size, index=0):
    """
    Load a font scaled for the supersampled overlay.

    Parameters
    ----------
    path : str
        Path to a TrueType or TrueType collection font file.
    size : float
        Font size in pixels at the map's native resolution.
    index : int, optional
        Face index within a font collection.

    Returns
    -------
    font : PIL.ImageFont.FreeTypeFont
        Font at size * SS.
    """
    font = ImageFont.truetype(path, size * SS, index=index)
    return font


def draw_site(draw, dot_xy, name_lines, place, label_xy, name_font, place_font):
    """
    Draw one site in the map's style: a yellow dot, a yellow name, and a
    white place line underneath.

    Parameters
    ----------
    draw : PIL.ImageDraw.ImageDraw
        Drawing context on the supersampled overlay.
    dot_xy : tuple of float
        Dot center (x, y) in native map pixels.
    name_lines : list of str
        Site name, one entry per line.
    place : str
        City and region shown under the name.
    label_xy : tuple of float
        Top-left (x, y) of the first name line in native map pixels.
    name_font, place_font : PIL.ImageFont.FreeTypeFont
        Fonts for the name and the place line.

    Returns
    -------
    None
    """
    # Dot radius matches the original 6 px dots.
    r = 3.0 * SS
    cx, cy = dot_xy[0] * SS, dot_xy[1] * SS
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=YELLOW)

    # Name lines in yellow, 13 px apart like the two-line STScI label.
    x, y = label_xy[0] * SS, label_xy[1] * SS
    for line in name_lines:
        draw.text((x, y), line, font=name_font, fill=YELLOW)
        y += 13 * SS

    # Place line in white, slightly tighter under the name.
    draw.text((x, y + 1 * SS), place, font=place_font, fill=WHITE)

    return None


def main():
    """
    Build the updated map from the original and save it as a PNG.

    Returns
    -------
    None
    """
    base = Image.open(BASE_MAP).convert('RGBA')
    w, h = base.size

    # Transparent overlay at SS x the native resolution.
    overlay = Image.new('RGBA', (w * SS, h * SS), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    name_font = get_font(FUTURA, 13, index=2)
    place_font = get_font(FUTURA, 10, index=0)

    # Caltech / IPAC at Pasadena; label sits up and right of the dot like
    # the Arizona State label.
    draw_site(draw, (146, 412), ['Caltech / IPAC'], 'Pasadena, CA', (152.5, 383),
              name_font, place_font)

    # International inset in the open Gulf of Mexico, styled after the
    # title box.
    box = (530, 579, 712, 640)
    draw.rounded_rectangle(tuple(v * SS for v in box), radius=8 * SS, fill=BOX_FILL)

    # Small spaced caps header, like the title's top line.
    header_font = get_font(AVENIR, 8, index=0)
    hx, hy = (box[0] + 10) * SS, (box[1] + 5) * SS
    for ch in 'INTERNATIONAL':
        draw.text((hx, hy), ch, font=header_font, fill=BOX_HEADER)
        hx += header_font.getlength(ch) + 1.6 * SS

    draw_site(draw, (box[0] + 13, box[1] + 26),
              ['Max Planck Institute', 'for Astronomy'], 'Heidelberg, Germany',
              (box[0] + 21, box[1] + 15), name_font, place_font)

    # Downsample the overlay and composite onto the original.
    overlay = overlay.resize((w, h), Image.LANCZOS)
    out = Image.alpha_composite(base, overlay).convert('RGB')
    out.save(OUT_MAP)

    return None


if __name__ == '__main__':
    main()
