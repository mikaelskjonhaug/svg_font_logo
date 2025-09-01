# Install Pillow
from PIL import Image, ImageDraw, ImageFont

# INTERFACE:
# What text render
text = "Your text here"
"""
FONTS: Drag a .ttf file into the project root and import it into the font_path

"""
ttf_path = "WindSong-Medium.ttf"   
# What resolutions to save, 512 seems to be best for most use cases
sizes = [128, 256, 512, 4096]  
# Hex color       
color = "#ff8800"              
padding = 20

for s in sizes:
    # Make new image in size x size dimensions
    img = Image.new("RGBA", (s, s), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    # rough font size: scale with canvas size
    font = ImageFont.truetype(ttf_path, size=int(s*0.75))
    w, h = draw.textbbox((0,0), text, font=font)[2:]
    x = (s - w) // 2
    y = (s - h) // 2
    draw.text((x, y), text, font=font, fill=color)
    img.save(f"ms-logo-{s}.png", optimize=True)
