#!/usr/bin/python3

from PIL import Image
import sys

screen_width = 128
screen_height = 64
bitmap_width = 48
bitmap_height = 48

img_path = sys.argv[1]
img = Image.open(img_path)

img = img.convert('L')

img_resized = img.resize((bitmap_width, bitmap_height))

img_bw = img_resized.point(lambda x: 0 if x < 128 else 1, '1')

bitmap = []
pixels = img_bw.load()
for y in range(bitmap_height):
    byte = 0
    for x in range(bitmap_width):
        if pixels[x, y] == 1:
            byte |= (1 << (7 - (x % 8)))
        if x % 8 == 7:
            bitmap.append(f'B{byte:08b}')
            byte = 0
    if x % 8 != 7:
        bitmap.append(f'B{byte:08b}')

for byte in bitmap:
    print(byte + ',')

