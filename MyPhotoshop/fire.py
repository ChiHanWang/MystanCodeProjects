"""
File: fire.py
Name: Michelle
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, Import image path
    :return: SimpleImage, Mark the picture of the fire area
    Function: Mark fire area
    Principle: Use mean value comparison to find the area with high R value and mark it out
    """
    # open the image
    img = SimpleImage(filename)

    for pixel in img:
        grayscale = (pixel.red + pixel.green + pixel.blue) // 3

        if pixel.red > grayscale * HURDLE_FACTOR:
            # highlight fires
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # grayscale
            pixel.red = grayscale
            pixel.green = grayscale
            pixel.blue = grayscale

    return img


def main():
    """
    Function: Mark fire area
    Principle: Display the original picture and the special fire area picture
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
