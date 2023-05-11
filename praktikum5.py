import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('download.jpeg')




img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

# membuat array kosong untuk citra hasil pemrosesan
img_brightness = np.zeros(img.shape, dtype=np.uint8)


# fungsi untuk meningkatkan kecerahan citra
def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][1]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)

    # menampilkan citra asli dan hasil pemrosesan
    # menampilkan


brighter(-100)
plt.imshow(img_brightness)
plt.title("Brightness -100")
plt.show()
brighter(100)
plt.imshow(img_brightness)
plt.title("Brightness 100")
plt.show()

# bri RGB
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)


# fungsi rgb
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbright[y][x] = (red, green, blue)


# menampilkan
rgbbrighter(-100)
plt.imshow(img_rgbbright)
plt.title("Brightness -100")
plt.show()
rgbbrighter(100)
plt.imshow(img_rgbbright)
plt.title("Brightness 100")
plt.show()

img_contras = np.zeros(img.shape, dtype=np.uint8)


def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            img_contras[y][x] = (gray, gray, gray)


# menampilkan
contrass(20)
plt.imshow(img_contras)
plt.title("contrass 20")
plt.show()
contrass(100)
plt.imshow(img_contras)
plt.title("contrass 100")
plt.show()

img_contrasrgb = np.zeros(img.shape, dtype=np.uint8)


# fungsi rgb
def rgbcontrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            img_contrasrgb[y][x] = (red, green, blue)


# menampilkan
rgbcontrass(20)
plt.imshow(img_contrasrgb)
plt.title("contrass 20")
plt.show()
rgbcontrass(100)
plt.imshow(img_contrasrgb)
plt.title("contrass 100")
plt.show()

img_autocontrass = np.zeros(img.shape, dtype=np.uint8)

def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)

        autocontrass()
        plt.imshow(img_autocontrass)
        plt.title("Contrass Autolevel")
        plt.show()
