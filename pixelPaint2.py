import cv2
import numpy as np

# Load images
mountain_texture = cv2.imread('mountain_texture.jpg')
mountain_texture2 = cv2.imread('mountain_texture2.jpg')
mountain_texture3 = cv2.imread('mountain_texture3.jpg')
lake_image = cv2.imread('lake_image.jpg')
pine_tree_image = cv2.imread('pine_tree_image.png')
bush_image = cv2.imread('bush_image.png')
sunset_image = cv2.imread('sunset_image.jpg')

# Create a blank canvas
canvas = np.zeros((500, 800, 3), dtype=np.uint8)

# Resize the mountain texture to match the canvas width
mountain_texture = cv2.resize(mountain_texture, dsize=(canvas.shape[1], 150), interpolation=cv2.INTER_AREA)
mountain_texture2 = cv2.resize(mountain_texture2, dsize=(canvas.shape[1], 150), interpolation=cv2.INTER_AREA)
mountain_texture3 = cv2.resize(mountain_texture3, dsize=(canvas.shape[1], 150), interpolation=cv2.INTER_AREA)

# Create a mask for the mountain shape (larger peak)
large_mountain_mask = np.zeros(canvas.shape[:2], dtype=np.uint8)
cv2.fillConvexPoly(large_mountain_mask, np.array([[200, 100], [600, 100], [400, 350]]), (255,))
large_mountain_mask = cv2.flip(large_mountain_mask, 0)

# Create a mask for the mountain shape (smaller peak)
small_mountain_mask = np.zeros(canvas.shape[:2], dtype=np.uint8)
cv2.fillConvexPoly(small_mountain_mask, np.array([[100, 150], [400, 150], [200, 250]]), (255,))
small_mountain_mask = cv2.flip(small_mountain_mask, 0)

# Create a mask for the third mountain
third_mountain_mask = np.zeros(canvas.shape[:2], dtype=np.uint8)
cv2.fillConvexPoly(third_mountain_mask, np.array([[350, 100], [750, 100], [550, 300]]), (255,))
third_mountain_mask = cv2.flip(third_mountain_mask, 0)

# Apply the mountain texture to the canvas using the masks
for y in range(canvas.shape[0]):
    for x in range(canvas.shape[1]):
        if large_mountain_mask[y, x] == 255:
            canvas[y, x] = mountain_texture[y % mountain_texture.shape[0], x]

        if small_mountain_mask[y, x] == 255:
            canvas[y, x] = mountain_texture2[y % mountain_texture2.shape[0], x]

        if third_mountain_mask[y, x] == 255:
            canvas[y, x] = mountain_texture3[y % mountain_texture3.shape[0], x]


# Resize and apply the lake image to the canvas
lake_height = canvas.shape[0] // 3
resized_lake_image = cv2.resize(lake_image, dsize=(canvas.shape[1], lake_height), interpolation=cv2.INTER_AREA)
canvas[canvas.shape[0] - lake_height:, :] = resized_lake_image

# Resize and apply the sunset image to the canvas
sunset_image = cv2.resize(sunset_image, dsize=(canvas.shape[1], canvas.shape[0]), interpolation=cv2.INTER_LANCZOS4)
canvas = cv2.addWeighted(canvas, 0.5, sunset_image, 0.5, 0)

# Import the Pillow library for image processing
from PIL import Image

# Load the pine tree and bush images
pine_tree_image = Image.open('pine_tree_image.png').convert('RGBA')
bush_image = Image.open('bush_image.png').convert('RGBA')

# Draw the pine trees
pine_tree_height = 100
pine_tree_width = 50

for i in range(10):
   pine_tree_x = np.random.randint(-100, 250)  
   pine_tree_y = canvas.shape[0] - 100 - pine_tree_height

    # Create a mask based on the alpha channel of the pine tree image
   pine_tree_mask = pine_tree_image.split()[-1]

    # Resize the pine tree image and mask using Resampling.LANCZOS
   resized_pine_tree_image = pine_tree_image.resize((pine_tree_width, pine_tree_height), Image.Resampling.LANCZOS)
   resized_pine_tree_mask = pine_tree_mask.resize((pine_tree_width, pine_tree_height), Image.Resampling.LANCZOS)

    # Convert the resized pine tree image to RGB format
   resized_pine_tree_image = resized_pine_tree_image.convert('RGB')

    # Paste the resized pine tree image onto the canvas using the mask
   for y in range(pine_tree_height):
       for x in range(pine_tree_width):
           if resized_pine_tree_mask.getpixel((x, y)) > 0:
                canvas[pine_tree_y + y, pine_tree_x + x] = resized_pine_tree_image.getpixel((x, y))



# Display the canvas
cv2.imshow('Snowy Mountain Landscape', canvas)
cv2.waitKey(0)