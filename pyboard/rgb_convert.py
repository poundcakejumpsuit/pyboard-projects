from PIL import Image

def rgb(r, g, b):
		return ((b & 0xf8) << 8) | ((g & 0xfc) << 3) | (r >> 3)

def main():
	im = Image.open("cmprs.png")
	print("H,W: ", im.height,im.width)
	with open('colors.txt', 'w') as f:
		for row in range(im.height - 1):
			for col in range(im.width - 1):
					# print(col, row)
					r, g, b = im.getpixel((col, row))
					f.write("{} ,".format(rgb(r,g,b)))


if __name__ == "__main__":
	main()