"""
File: ghost.py
--------------
By: Christopher Patron
Project: CS 106A Assignment 3: Problem 2.B
Date: 04/21/2022

This program takes multiple images, processes them, and then
returns a "base image" where any obstructions are removed. For
example, in the "hoover" photos, the program removes pedestrians
and returns the image with no pedestrians.

"""

import os
import sys

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 0, 255)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """

    dist = (pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2
    return dist



def get_best_pixel(pixel_list):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across
    all pixels.

    Input:
        a list of pixels to be averaged and compared.  You can assume this list is never empty
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel([green_pixel, green_pixel, blue_pixel])
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel([red_pixel, red_pixel, red_pixel])
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """
    # Initializing the total number of respective rgb pixels for all images
    red_pixel_tot = 0
    green_pixel_tot = 0
    blue_pixel_tot = 0

    for i in range(len(pixel_list)):
        red_pixel_tot += pixel_list[i].red
        green_pixel_tot += pixel_list[i].green
        blue_pixel_tot += pixel_list[i].blue

    # All the pixels at each coordinate have been sorted, now their average are taken
    average_red = red_pixel_tot / len(pixel_list)
    average_green = green_pixel_tot / len(pixel_list)
    average_blue = blue_pixel_tot / len(pixel_list)

    # Initializing distance list
    dist = []

    # Calling get_pixel_dist to determine which pixel is the "best"
    for i in range(len(pixel_list)):
        dist.append(get_pixel_dist(pixel_list[i], average_red, average_green, average_blue))

    min_dist = min(dist)
    # Finding the index in the dist list in which the minimum value exists. This is the best pixel
    dist_index = dist.index(min_dist)

    return pixel_list[dist_index]



def create_ghost(image_list):
    """
    Given a list of image objects, this function creates and returns a Ghost
    solution image based on the images passed in. All the images passed
    in will be the same size.

    Input:
        a list images to be processed.  You can assume this list is never empty.
    Returns:
        a new Ghost solution image
    """

    # Initializing necessary variables
    width = image_list[0].width
    height = image_list[0].height
    ghost_image = SimpleImage.blank(width, height)

    for pixel in image_list[0]:
        pixel_list = []
        pixel_list.append(pixel)

        # Grabbing the pixel coordinates from the same pixel across all images
        for i in range(len(image_list)-1):
            pixel_list.append(image_list[i+1].get_pixel(pixel.x, pixel.y))

        best_pixel = get_best_pixel(pixel_list)

        # Creating the "ghost image" where all obstructions have been removed
        ghost_image.set_pixel(pixel.x, pixel.y, best_pixel)

    return ghost_image



######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images)
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")


if __name__ == '__main__':
    main()
