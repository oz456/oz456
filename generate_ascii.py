from PIL import Image
import os

img_path = "/home/omni/.config/omarchy/themes/shinchan/backgrounds/0-cosmic-night.jpg"
if not os.path.exists(img_path):
    # Fallback just in case
    img_path = "/home/omni/.config/omarchy/themes/shinchan/backgrounds/3-minimal.jpg"

img = Image.open(img_path)

# 120 columns for high detail ASCII art
cols = 120
aspect_ratio = img.height / img.width
# Font height is usually roughly 2x the width, so multiply by 0.5
rows = int(aspect_ratio * cols * 0.5)

img = img.resize((cols, rows), Image.Resampling.LANCZOS)
img = img.convert('RGB')

chars = " .:-=+*#%@"
svg_w = cols * 7 + 40
svg_h = rows * 12 + 60

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="100%">')
out.append('''<style>
  .win { fill: #11111b; rx: 12px; }
  .top { fill: #1e1e2e; }
  .dot-red { fill: #f38ba8; }
  .dot-yel { fill: #f9e2af; }
  .dot-grn { fill: #a6e3a1; }
  .txt { font-family: "Fira Code", "Courier New", monospace; font-size: 11px; white-space: pre; font-weight: 800; }
  
  /* CRT Scanline Effect */
  .scanline { fill: rgba(255,255,255,0.03); animation: scan 4s linear infinite; }
  @keyframes scan { 0% { transform: translateY(-100px); } 100% { transform: translateY(1200px); } }
  
  /* Floating window */
  .float { animation: float 6s ease-in-out infinite; }
  @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-6px); } }
</style>''')

out.append('<g class="float">')
out.append(f'<rect class="win" width="{svg_w}" height="{svg_h}"/>')
out.append(f'<rect class="top" width="{svg_w}" height="32" rx="12"/>')
out.append(f'<rect class="top" width="{svg_w}" height="16" y="16"/>')
out.append('<circle class="dot-red" cx="20" cy="16" r="6"/>')
out.append('<circle class="dot-yel" cx="40" cy="16" r="6"/>')
out.append('<circle class="dot-grn" cx="60" cy="16" r="6"/>')
out.append(f'<text x="{svg_w/2}" y="21" fill="#a6adc8" font-family="monospace" font-size="12" text-anchor="middle">oz456@github ~ cat shinchan_wallpaper.jpg | ascii</text>')

out.append('<g class="txt" transform="translate(20, 55)">')

for y in range(rows):
    line = f'<text y="{y * 12}">'
    for x in range(cols):
        r, g, b = img.getpixel((x, y))
        brightness = sum([r, g, b]) / 3
        char_idx = int((brightness / 255) * (len(chars) - 1))
        char = chars[char_idx]
        if char == ' ': char = '&#160;'
        elif char == '<': char = '&lt;'
        elif char == '>': char = '&gt;'
        elif char == '&': char = '&amp;'
        
        # Optimize size: omit tspan if it's black space, just use text
        line += f'<tspan fill="rgb({r},{g},{b})">{char}</tspan>'
    line += '</text>'
    out.append(line)

out.append('</g>')
out.append(f'<rect class="scanline" width="{svg_w}" height="80" y="0"/>')
out.append('</g>')
out.append('</svg>')

with open('wallpaper_ascii.svg', 'w') as f:
    f.write('\n'.join(out))
