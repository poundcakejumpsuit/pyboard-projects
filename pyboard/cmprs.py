from PIL import Image

def avg(*args):
    return sum(args) // len(args)

def main():
    im = Image.open('image.jpg')
    new_im = Image.new("RGB", (im.width // 24, im.height // 24))
    new_data = []
    print(im.width, im.height)
    for row in range(0, im.height - 24, 24):
        for col in range(0, im.width - 24, 24):
            r1, g1, b1 = im.getpixel((col, row))
            r2, g2, b2 = im.getpixel((col + 1, row))
            r3, g3, b3 = im.getpixel((col, row + 1))
            r4, g4, b4 = im.getpixel((col + 1, row + 1))
            r = avg(r1, r2, r3, r4)
            g = avg(g1, g2, g3, g4)
            b = avg(b1, b2, b3, b4)
            new_data.append((r,g,b))
    print(len(new_data))
    new_im.putdata(new_data)
    new_im.save('cmprs.png')

if __name__ == "__main__":
    main()
