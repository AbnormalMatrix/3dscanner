from PIL import Image, ImageDraw

WIDTH = 3300
HEIGHT = 2550

# If you want to fill the width, calculate size based on WIDTH / COLUMNS
COLUMNS = 12 
ROWS = 9

cal_img = Image.new("L", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(cal_img)

# Calculate size to fit the width exactly
square_size = WIDTH // COLUMNS 

# Loop through COLUMNS to fill the width
for row in range(ROWS):
    y1 = row * square_size
    y2 = y1 + square_size
    for col in range(COLUMNS):
        if (col + row) % 2 == 0:
            x1 = col * square_size
            x2 = x1 + square_size
            # This draws a row of squares across the top
            draw.rectangle([(x1, y1), (x2, y2)], 255)

cal_img.save("calibration_img.png")