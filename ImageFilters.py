# Lab 9 – Image Processing
# Name: Talia Astorino
# Date: 04/05/2026
# Purpose: Swappinf values of pixels in images.

from PIL import Image


def swapGreenBlue(img):

    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = img.getpixel((x, y))
            img.putpixel((x, y), (red, blue, green))

    img.save("swapGB.png")


def darken(img, amount):

    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = img.getpixel((x, y))

            red = max(0, red - amount)
            green = max(0, green - amount)
            blue = max(0, blue - amount)

            img.putpixel((x, y), (red, green, blue))

    img.save("darkImg.png")


def bwFilter(img):

    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = img.getpixel((x, y))
            avg = (red + green + blue) // 3
            img.putpixel((x, y), (avg, avg, avg))

    img.save("bwImg.png")


def main():
    
    myImg = Image.open("durango.png")

    swapImg = myImg.copy()
    darkImg = myImg.copy()

    swapGreenBlue(swapImg)
    darken(darkImg, 20)


if __name__ == "__main__":
    main()
