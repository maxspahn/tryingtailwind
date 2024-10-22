import sys
from PIL import Image, ImageOps

# Open your original image
image = Image.open(sys.argv[1])

# Define target size
target_width = 1600
target_height = 939

# Calculate the padding sizes
new_width = target_width
new_height = image.height
padding_width = (new_width - image.width) // 2  # Padding for left and right

# Add padding on the sides
padded_image = ImageOps.expand(image, border=(padding_width, 0), fill='white')

# Save the new image
padded_image.save(sys.argv[2])

