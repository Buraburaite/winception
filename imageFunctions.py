import numpy as np
import PIL.Image as Image

def load_image(filename, max_size=None):
    image = Image.open(filename)

    if max_size is not None:
        # Calculate the appropriate rescale-factor for
        # ensuring a max height and width, while keeping
        # the proportion between them.
        factor = max_size / np.max(image.size)
        print('here')
        print(f'factor: {factor}')

        # Scale the image's height and width.
        size = np.array(image.size) * factor

        # The size is now floating-point because it was scaled.
        # But PIL requires the size to be integers.
        size = size.astype(int)

        # Resize the image.
        image = image.resize(size, PIL.Image.LANCZOS)

    # Convert to numpy floating-point array.
    return np.float32(image)

def save_image(image, filename):
    # Ensure the pixel-values are between 0 and 255.
    image = np.clip(image, 0.0, 255.0)

    # Convert to bytes.
    image = image.astype(np.uint8)

    # Write the image-file in jpeg-format.
    with open(filename, 'wb') as file:
        Image.fromarray(image).save(file, 'png')

# def plot_image_big(image):  # this is jupyter notebook thing I think
#     # Ensure the pixel-values are between 0 and 255.
#     image = np.clip(image, 0.0, 255.0)
#
#     # Convert pixels to bytes.
#     image = image.astype(np.uint8)
#
#     # Convert to a PIL-image and display it.
#     display(Image.fromarray(image))

goblin = load_image('images/goblin.png')
print(f'Image is a {len(goblin[0])}x{len(goblin)} array of rgba arrays')

# for row in goblin:
#     for pixel in row:
#         pixel[1] = 1.0

# save_image(goblin, 'images/red-goblin.png')
