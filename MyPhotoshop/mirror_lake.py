"""
File: mirror_lake.py
Name: Michelle
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, Import image path
    :return new_img: SimpleImage, Export Mirror image
    Function: Mirror the original picture downward
    Principle: Symmetrically copy the RGB value of the original picture to achieve the mirror effect
    """
    # open the mountain image by using SimpleImage(filename)
    old_img = SimpleImage(filename)

    # create a new blank image
    new_img = SimpleImage.blank(old_img.width, old_img.height*2)

    for x in range(old_img.width):
        for y in range(old_img.height):

            # to get pixel from the original image
            old_img_pixel = old_img.get_pixel(x, y)

            # the upper of new_img
            new_img_pixel1 = new_img.get_pixel(x, y)
            new_img_pixel1.red = old_img_pixel.red
            new_img_pixel1.green = old_img_pixel.green
            new_img_pixel1.blue = old_img_pixel.blue

            # the lower of new_img
            new_img_pixel2 = new_img.get_pixel(x, new_img.height-1-y)
            new_img_pixel2.red = old_img_pixel.red
            new_img_pixel2.green = old_img_pixel.green
            new_img_pixel2.blue = old_img_pixel.blue

    return new_img


def main():
    """
    Function: Mirror the original picture downward
    Principle: Display the original picture and the mirror picture
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
