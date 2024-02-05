from simpleimage import SimpleImage


def copy_border(base_image, copy_image, up, down, left, right):
    """
    Copy copy_image onto base_image, leaving a border around the side of base_image
    defined by the parameters provided: 'left' pixels on the left, 'right' pixels on
    the right, 'up' pixels on top, and 'down' pixels on the bottom. You may assume
    the images are the same size, and that the borders aren't so big that they would
    overlap or be larger than the image.
    (As a practice exercise, how might you do bounds checking, or handle this if
    the images weren't the same size?)

    Directly modify pixels in the base image, no need to return anything.
    To preview the expected output for up,down,left,right of 10,40,5,30 respectively,
    run python3 copy_border_soln.py.
    """

    width = base_image.width
    height = base_image.height

    for pixel in copy_image:
        x = pixel.x + left
        y = pixel.y + up

        if x <= width-right and y <= height-down:
            base_image.set_pixel(x, y, copy_image.get_pixel(x, y))


def main():
    base = SimpleImage('karel.png')
    copy = SimpleImage('pink.png')
    copy_border(base, copy, 10, 40, 5, 30)
    base.show()


if __name__ == "__main__":
    main()
