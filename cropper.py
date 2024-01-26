import os
from PIL import Image

def crop_image(input_image_path, output_image_path):
    image = Image.open(input_image_path).convert("RGBA")
    image_data = image.load()

    non_empty_pixels = False
    x_min, y_min, x_max, y_max = 0, 0, 0, 0

    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = image_data[x, y]
            if a > 0:
                if not non_empty_pixels:
                    non_empty_pixels = True
                    x_min, y_min, x_max, y_max = x, y, x, y
                else:
                    if x < x_min:
                        x_min = x
                    if y < y_min:
                        y_min = y
                    if x > x_max:
                        x_max = x
                    if y > y_max:
                        y_max = y

    cropped_image = image.crop((x_min, y_min, x_max+1, y_max+1))
    cropped_image.save(output_image_path)

def crop_images_in_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename.replace('.png', '_cropped.png'))
            crop_image(input_image_path, output_image_path)

# Usage
crop_images_in_folder('input_folder', 'output_folder')
