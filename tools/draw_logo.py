#!/usr/bin/env python3
"""Draw the Shippy logo: one bold robot face on a plain bright background.

Shippy is the little bounty bot from the coin dossier (see COIN.md): a
round-headed robot with an antenna, big friendly eyes and a wide grin,
holding nothing, doing one thing — building while you sleep.

Run:  python3 tools/draw_logo.py
Writes: logo.png (512 x 512, well under pump.fun's 5 MiB / 16 MP limits).
"""

from PIL import Image, ImageDraw

SIZE = 512
BG = (255, 214, 10)      # bright yellow, plain background
INK = (17, 24, 39)       # near-black navy for outlines
FACE = (255, 255, 255)   # white robot face
SCREEN = (34, 197, 94)   # green screen glow for the eyes
CHEEK = (255, 107, 107)  # coral cheeks
BOLT = (59, 130, 246)    # blue antenna tip

img = Image.new("RGB", (SIZE, SIZE), BG)
d = ImageDraw.Draw(img)

# Antenna: stem + glowing tip.
d.line([(256, 96), (256, 150)], fill=INK, width=14)
d.ellipse([228, 52, 284, 108], fill=BOLT, outline=INK, width=8)

# Robot head: big rounded rectangle, thick dark outline.
d.rounded_rectangle([86, 150, 426, 420], radius=90, fill=FACE, outline=INK, width=12)

# Head bolts (ears) on both sides.
d.ellipse([58, 252, 96, 300], fill=BOLT, outline=INK, width=8)
d.ellipse([416, 252, 454, 300], fill=BOLT, outline=INK, width=8)

# Eyes: two big green screens with white shine dots.
for x0 in (138, 292):
    d.rounded_rectangle([x0, 210, x0 + 82, 272], radius=22, fill=SCREEN, outline=INK, width=8)
    d.ellipse([x0 + 14, 222, x0 + 34, 242], fill=(255, 255, 255))
    d.ellipse([x0 + 48, 222, x0 + 62, 236], fill=(255, 255, 255))

# Cheeks.
d.ellipse([118, 300, 158, 330], fill=CHEEK)
d.ellipse([354, 300, 394, 330], fill=CHEEK)

# Grin: a wide smile arc.
d.arc([176, 296, 336, 392], start=15, end=165, fill=INK, width=12)
# Smile end dimples.
d.ellipse([172, 330, 188, 346], fill=INK)
d.ellipse([324, 330, 340, 346], fill=INK)

# A small gold coin with a "B" (for bounty) tucked at the bottom corner,
# like a badge Shippy earned.
d.ellipse([352, 356, 440, 444], fill=(255, 196, 0), outline=INK, width=8)
d.ellipse([366, 370, 426, 430], outline=INK, width=5)
d.text((393, 400), "B", fill=INK, anchor="mm")

img.save("logo.png", format="PNG")
print("wrote logo.png", img.size)
