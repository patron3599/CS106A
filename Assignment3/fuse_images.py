
# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

def fuse_images(img_1, img_2, dist_btwn_rect):
    obama = SimpleImage(img_1)
    megamind = SimpleImage(img_2)
    HEIGHT = obama.height
    WIDTH = obama.width

    # Top Bar
    for pixel in megamind:
        x = pixel.x + dist_btwn_rect
        y = pixel.y + dist_btwn_rect

        if x <= WIDTH - dist_btwn_rect and y <= 2*dist_btwn_rect:
            obama.set_pixel(x, y, megamind.get_pixel(x, y))

    # Bottom Bar
    for pixel in megamind:
        x = pixel.x + dist_btwn_rect
        y = HEIGHT - 2*dist_btwn_rect + pixel.y

        if x <= WIDTH - dist_btwn_rect and y <= HEIGHT - dist_btwn_rect:
            obama.set_pixel(x, y, megamind.get_pixel(x, y))

    # Left-Bar
    for pixel in megamind:
        x = pixel.x + dist_btwn_rect
        y = pixel.y + dist_btwn_rect

        if x <= 2*dist_btwn_rect and y <= HEIGHT - dist_btwn_rect:
            obama.set_pixel(x, y, megamind.get_pixel(x, y))

    # Right-Bar
    for pixel in megamind:
        x = WIDTH - 2*dist_btwn_rect + pixel.x
        y = pixel.y + dist_btwn_rect

        if x <= WIDTH - dist_btwn_rect and y <= HEIGHT - dist_btwn_rect:
            obama.set_pixel(x, y, megamind.get_pixel(x, y))

    obama.show()


def main():
    img_1 = 'obama.jpg'
    img_2 = 'megamind.jpg'
    dist_btwn_rect = 130

    fuse_images(img_1, img_2, dist_btwn_rect)




if __name__ == '__main__':
    main()
