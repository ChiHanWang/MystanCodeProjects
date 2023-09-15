"""
File: stanCodoshop.py
Name: Michelle
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

This program can compare several photos,
find out the best pixel,
and export a new photo with no sundries or strangers.
(photos which need to be compared should be the same size)
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # 某1個pixel的RGB value與mean RGB value距離(先平方再開根號)
    return math.sqrt((pixel.red-red)**2+(pixel.green-green)**2+(pixel.blue-blue)**2)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list with three values of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # pixels is a List containing lots of pixel
    red = sum(pixel.red for pixel in pixels) // len(pixels)
    green = sum(pixel.green for pixel in pixels) // len(pixels)
    blue = sum(pixel.blue for pixel in pixels) // len(pixels)
    return [red, green, blue]

    # Below is another way of doing it

    # sum為python內建字，請勿用，可改成total
    # red_sum = 0
    # green_sum = 0
    # blue_sum = 0
    # for pixel in pixels:
    #     red_sum += pixel.red
    #     green_sum += pixel.green
    #     blue_sum += pixel.blue
    # 把list裡的red_sum, green_sum, blue_sum依序丟入total裡，再與 len(pixels)相除後，包裝成新的list
    # return list(total // len(pixels) for total in [red_sum, green_sum, blue_sum])


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    [r, g, b] = get_average(pixels)
    pixel_lst = []
    for pixel in pixels:
        # add (distance, pixel)的tuple
        pixel_lst.append((get_pixel_dist(pixel, r, g, b), pixel))
    # 找到最小distance後，會得到(distance, pixel)的tuple，需取index=1的元素
    return min(pixel_lst, key=lambda ele: ele[0])[1]

    # Below is another way of doing it

    # 得到RGB三個平均值，裝在list中
    # [r, g, b] = get_average(pixels)
    # dist = get_pixel_dist(pixels[0], r, g, b)
    # min_dist = dist     # minimum distance
    # best_p = pixels[0]  # best pixel
    # for pixel in pixels[1:]:
    #     dist = get_pixel_dist(pixel, r, g, b)
    #     if dist < min_dist:
    #         min_dist = dist
    #         best_p = pixel
    # return best_p


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    # 與image相同大小的result
    result = SimpleImage.blank(width, height)

    # Write code to populate image and create the 'ghost' effect
    for i in range(result.width):
        for j in range(result.height):

            # 每更換一次xy值，需把pixels list清空
            pixels = []

            for img in images:
                # N張圖片中，取相同xy位置的pixel，放進pixels list
                pixels.append(img.get_pixel(i, j))

            # 找出最佳的pixel
            best = get_best_pixel(pixels)

            # 將最佳pixel的RGB值，assign給result的xy位置的pixel的RGB
            result.get_pixel(i, j).red = best.red
            result.get_pixel(i, j).green = best.green
            result.get_pixel(i, j).blue = best.blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
