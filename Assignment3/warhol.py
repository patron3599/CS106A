"""
File: warhol.py
---------------
By: Christopher Patron
Project: CS 106A Assignment 3: Problem 2.A
Date: 04/20/2022

This file creates an Andrew Warhol style image using the base photo of
Simba the pomeranian. Once ran, the resulting image created is a multi-colored
2x3 image of Simba.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage
import random

# Name of file that we will use to create the warhol image
IMAGE_FILE = 'images/simba.jpg'


def create_filtered_image(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol program. It creates an
    image object from the image in the file IMAGE_FILE, and then recolors the image
    object.  The parameters to this function are:
      red_scale: A number to multiply each pixels' red component by
      green_scale: A number to multiply each pixels' green component by
      blue_scale: A number to multiply each pixels' blue component by
    This function should return a newly generated image with the appropriately
    scaled color values of the pixels.
    """
    simba = SimpleImage(IMAGE_FILE)
    for pixel in simba:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale

    return simba


def make_warhol():
    """
    This function generates a Warhol-style picture based on the original image in the
    file IMAGE_FILE.  The Warhol image contains "patches" that are different colored
    versions of the original image.  This function returns the Warhol image.
    """
    # Initializing the blank canvas and base image
    simba = SimpleImage(IMAGE_FILE)
    blank_image = SimpleImage.blank(simba.width*3, simba.height*2)
    rand_rgb = random.randint(0, 3)

    # Creating individual patches by calling create_filtered_image
    dog_1 = create_filtered_image(1.5, 0, 1.5)  # pink
    dog_2 = create_filtered_image(1.5, 1, 0)  # orange
    dog_3 = create_filtered_image(0.5, 1.5, 1)  # lime green
    dog_4 = create_filtered_image(0, 1, 1.5)  # sky blue
    dog_5 = create_filtered_image(3, 1, 1.5)  # light red
    dog_6 = create_filtered_image(1, 0, 3)  # purple

    for i in range(6):
        simba_colored = create_filtered_image(rand_rgb, rand_rgb, rand_rgb)
        for pixel in simba:
            x = pixel.x
            y = pixel.y

            # Concatenating each patch to fill blank_image
            blank_image.set_pixel(x, y, dog_1.get_pixel(x, y))
            blank_image.set_pixel(x + simba.width, y, dog_2.get_pixel(x, y))
            blank_image.set_pixel(x + 2*simba.width, y, dog_3.get_pixel(x, y))
            blank_image.set_pixel(x, y + simba.height, dog_4.get_pixel(x, y))
            blank_image.set_pixel(x + simba.width, y + simba.height, dog_5.get_pixel(x, y))
            blank_image.set_pixel(x + 2*simba.width, y + simba.height, dog_6.get_pixel(x, y))

    warhol_image = blank_image
    return warhol_image

def main():
    """
    This program tests your create_filtered_image and make_warhol functions by calling
    those functions and displaying the resulting images.  Feel free to modify this code
    when you are writing your program.  For example, the call to the create_filtered_image
    function is provided to test that function by itself.  Feel free to delete that portion
    of the code when you have the create_filtered_image working, and then just focus on
    the make_warhol function.
    """

    warhol_image = make_warhol()
    if warhol_image != None:
        warhol_image.show()


if __name__ == '__main__':
    main()
