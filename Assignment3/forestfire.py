"""
File: forestfire.py
----------------
By: Christopher Patron
Project: CS 106A Assignment 3: Problem 2.A
Date: 04/18/2022

This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


# Intensity threshold used to determine is a pixel is
# "sufficiently red" to indicate that it is a fire.
INTENSITY_THRESHOLD = 1.05


def highlight_fires(filename):
    """
    This function should highlight the "red" pixels in the image passed in
    and grayscale all other pixels in the image in order to highlight areas
    of wildfires.

    Input:
        filename (string): name of image file to be read in

    Returns:
        highlighted image with "sufficiently red" pixels highlighted
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3

        if pixel.red >= average * INTENSITY_THRESHOLD:
            x = pixel.x
            y = pixel.y

            # Highlighting the fire pixels in red
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # Turning all other pixels to grey scale
            pixel.red = average
            pixel.green = average
            pixel.blue = average

    return image


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
