import math

WIDTH = 800
HEIGHT = 450
ROWS = 16
COLS = 16
TILE_W = 20
TILE_H = 10

out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}">']
out.append('<style>')
out.append('.bg { fill: #0d1117; }')
out.append('@keyframes rise {')
out.append('  0%, 100% { transform: translateY(0px); }')
out.append('  50% { transform: translateY(-70px); }')
out.append('}')

for r in range(ROWS):
    for c in range(COLS):
        dist = math.sqrt((r-ROWS/2)**2 + (c-COLS/2)**2)
        delay = dist * -0.35
        out.append(f'.p_{r}_{c} {{ animation: rise 3.5s ease-in-out {delay:.2f}s infinite; }}')
out.append('</style>')

out.append(f'<rect class="bg" width="{WIDTH}" height="{HEIGHT}"/>')
out.append('<g transform="translate(400, 150)">')

for r in range(ROWS):
    for c in range(COLS):
        x = (c - r) * TILE_W
        y = (c + r) * TILE_H
        dist = math.sqrt((r-ROWS/2)**2 + (c-COLS/2)**2)
        
        # Cyberpunk / Synthwave colors (Cyan to Purple)
        hue = int((dist / 16) * 100 + 200) % 360 
        color_top = f'hsl({hue}, 90%, 65%)'
        color_left = f'hsl({hue}, 90%, 45%)'
        color_right = f'hsl({hue}, 90%, 25%)'

        out.append(f'<g class="p_{r}_{c}" transform="translate({x}, {y})">')
        out.append(f'<polygon points="0,0 {TILE_W},{TILE_H} 0,{TILE_H*2} {-TILE_W},{TILE_H}" fill="{color_top}"/>')
        out.append(f'<polygon points="{-TILE_W},{TILE_H} 0,{TILE_H*2} 0,{TILE_H*2+80} {-TILE_W},{TILE_H+80}" fill="{color_left}"/>')
        out.append(f'<polygon points="{TILE_W},{TILE_H} 0,{TILE_H*2} 0,{TILE_H*2+80} {TILE_W},{TILE_H+80}" fill="{color_right}"/>')
        out.append('</g>')

out.append('</g>')
out.append('</svg>')

with open('mesmerizing.svg', 'w') as f:
    f.write('\n'.join(out))
