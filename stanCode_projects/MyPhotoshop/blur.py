"""
File: blur.py
Name: Michelle
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage

# Adjust the degree of blurring, preset 5 times
BLUR_LAYER = 5


def blur(img):
    """
    :param img: SimpleImage, Original picture
    :return new_img: SimpleImage, Blurred image
    Function: Blur the imported image
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    # create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):
            total_red = 0
            total_green = 0
            total_blue = 0
            neighbor = 0  # 計算有幾個相鄰點

            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):

                    # 尋找相鄰pixel的(x, y)值
                    x_pixel = x + i
                    y_pixel = y + j

                    # 判斷(x, y)坐標是否在圖像內
                    if 0 <= x_pixel < img.width and 0 <= y_pixel < img.height:
                        img_pixel = img.get_pixel(x_pixel, y_pixel)
                        neighbor += 1  # 計算有幾個相鄰點
                        total_red += img_pixel.red
                        total_green += img_pixel.green
                        total_blue += img_pixel.blue

            new_img_pixel = new_img.get_pixel(x, y)
            new_img_pixel.red = total_red // neighbor
            new_img_pixel.green = total_green // neighbor
            new_img_pixel.blue = total_blue // neighbor

    return new_img

    # Below is another way of doing it

    # # create a new blank img that is as big as the original one
    # new_img = SimpleImage.blank(img.width, img.height)
    #
    # # Loop over the picture
    # for x in range(img.width):
    #     for y in range(img.height):
    #         new_img_pixel = new_img.get_pixel(x, y)
    #         # 因為pixel的RGB值最大只能到255，所以需要額外使用變數來相加
    #         total_red = 0
    #         total_green = 0
    #         total_blue = 0
    #
    #         # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
    #         if x == 0 and y == 0:
    #             # Get pixel at the upper left corner of the image.
    #             for k in range(x + 2):
    #                 for t in range(y + 2):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 4
    #             total_green //= 4
    #             total_blue //= 4
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         elif x == img.width-1 and y == 0:
    #             # Get pixel at the upper right corner of the image.
    #             for k in range(x - 1, x + 1):
    #                 for t in range(y + 2):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 4
    #             total_green //= 4
    #             total_blue //= 4
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         elif x == 0 and y == img.height-1:
    #             # Get pixel at the lower left corner of the image
    #             for k in range(x + 2):
    #                 for t in range(y - 1, y + 1):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 4
    #             total_green //= 4
    #             total_blue //= 4
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         elif x == img.width-1 and y == img.height-1:
    #             # Get pixel at the lower right corner of the image
    #             for k in range(x - 1, x + 1):
    #                 for t in range(y - 1, y + 1):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 4
    #             total_green //= 4
    #             total_blue //= 4
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         elif 0 < x < img.width-1 and y == 0:
    #             # Get upper edge's pixels (without two corners)
    #             for k in range(x - 1, x + 2):
    #                 for t in range(y + 2):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 6
    #             total_green //= 6
    #             total_blue //= 6
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         elif 0 < x < img.width-1 and y == img.height-1:
    #             # Get lower edge's pixels (without two corners)
    #             for k in range(x - 1, x + 2):
    #                 for t in range(y - 1, y + 1):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 6
    #             total_green //= 6
    #             total_blue //= 6
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         elif x == 0 and 0 < y < img.height-1:
    #             # Get left edge's pixels (without two corners)
    #             for k in range(x + 2):
    #                 for t in range(y - 1, y + 2):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 6
    #             total_green //= 6
    #             total_blue //= 6
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         elif x == img.width-1 and 0 < y < img.height-1:
    #             # Get right edge's pixels (without two corners)
    #             for k in range(x - 1, x + 1):
    #                 for t in range(y - 1, y + 2):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 6
    #             total_green //= 6
    #             total_blue //= 6
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    #         else:
    #             # Inner pixels.
    #             for k in range(x - 1, x + 2):
    #                 for t in range(y - 1, y + 2):
    #                     img_pixel = img.get_pixel(k, t)
    #                     total_red += img_pixel.red
    #                     total_green += img_pixel.green
    #                     total_blue += img_pixel.blue
    #             total_red //= 9
    #             total_green //= 9
    #             total_blue //= 9
    #             new_img_pixel.red = total_red
    #             new_img_pixel.green = total_green
    #             new_img_pixel.blue = total_blue
    #
    # return new_img


def main():
    """
    Function: Blur the picture in 5 layers.
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLUR_LAYER):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
