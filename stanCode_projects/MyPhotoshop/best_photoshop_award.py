"""
File: best_photoshop_award.py
Name: Michelle
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""

from simpleimage import SimpleImage

THRESHOLD = 1.5
BLACK = 100


def main():
    """
    創作理念： Because the upside down world is cool, I want to be a member of Vecna's team.
    """
    fig = SimpleImage('image_contest/me.jpg')  # 2729 * 3596
    fig.show()

    bg = SimpleImage('image_contest/background.jpg')  # 1080 * 1350
    bg.make_as_big_as(fig)

    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    """
    Function: Using figure and background to make a composite image
    """
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue) // 3
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue

            if fig_pixel.blue > avg * THRESHOLD and total > BLACK:
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue

    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
