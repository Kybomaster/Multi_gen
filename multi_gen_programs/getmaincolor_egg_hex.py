def getMainColor_egg_hex(path):
	from PIL import Image
	import random
 
	MAX_SIZE1 = 65537
	MAX_SIZE2 = 262145
	MAX_SIZE3 = 1048577
	MAX_SIZE4 = 4194304
	MAX_SIZE5 = 16777217
	MAX_SIZE6 = 67108880
	image = Image.open(path)
	pixel = []
	pixel2 = []

	w, h = image.size
		
	if w*h <= MAX_SIZE1:
		for x in range(w):
			for y in range(h):
				rgb = image.getpixel((x, y))
				if rgb[-1]:
					pixel.append(rgb)
		dx = 4
		dy = 4
		for xx in range(0, w, random.randint(1, dx)):
			dx = w - xx
			for yy in range(0, h, random.randint(1, dy)):
				dy = h - yy
				rgb = image.getpixel((xx, yy))
				if rgb[-1]:
					pixel2.append(rgb)
	 
	elif w*h > MAX_SIZE6:
		return ["default", "default"]

	elif w*h > MAX_SIZE5:
		for x in range(0, w, 1024):
			for y in range(0, h, 1024):
				rgb = image.getpixel((x, y))
				if rgb[-1]:
					pixel.append(rgb)
		dx = 1024
		dy = 1024
		for xx in range(0, w, random.randint(1, dx)):
			dx = w - xx
			for yy in range(0, h, random.randint(1, dy)):
				dy = h - yy
				rgb = image.getpixel((xx, yy))
				if rgb[-1]:
					pixel2.append(rgb)
		
	elif w*h > MAX_SIZE4:
		for x in range(0, w, 256):
			for y in range(0, h, 256):
				rgb = image.getpixel((x, y))
				if rgb[-1]:
					pixel.append(rgb)
		dx = 256
		dy = 256
		for xx in range(0, w, random.randint(1, dx)):
			dx = w - xx
			for yy in range(0, h, random.randint(1, dy)):
				dy = h - yy
				rgb = image.getpixel((xx, yy))
				if rgb[-1]:
					pixel2.append(rgb)
		
	elif w*h > MAX_SIZE3:
		for x in range(0, w, 64):
			for y in range(0, h, 64):
				rgb = image.getpixel((x, y))
				if rgb[-1]:
					pixel.append(rgb)
		dx = 64
		dy = 64
		for xx in range(0, w, random.randint(1, dx)):
			dx = w - xx
			for yy in range(0, h, random.randint(1, dy)):
				dy = h - yy
				rgb = image.getpixel((xx, yy))
				if rgb[-1]:
					pixel2.append(rgb)
		
	elif w*h > MAX_SIZE2:
		for x in range(0, w, 16):
			for y in range(0, h, 16):
				rgb = image.getpixel((x, y))
				if rgb[-1]:
					pixel.append(rgb)
		dx = 16
		dy = 16
		for xx in range(0, w, random.randint(1, dx)):
			dx = w - xx
			for yy in range(0, h, random.randint(1, dy)):
				dy = h - yy
				rgb = image.getpixel((xx, yy))
				if rgb[-1]:
					pixel2.append(rgb)
		
	elif w*h > MAX_SIZE1:
		for x in range(0, w, 4):
			for y in range(0, h, 4):
				cords = x, y
				rgb = image.getpixel(cords)
				if rgb[-1]:
					pixel.append(rgb)
		dx = 4
		dy = 4
		for xx in range(0, w, random.randint(1, dx)):
			dx = w - xx
			for yy in range(0, h, random.randint(1, dy)):
				dy = h - yy
				rgb = image.getpixel((xx, yy))
				if rgb[-1]:
					pixel2.append(rgb)

	avr = [sum(s)//len(s) for s in zip(*pixel)]
	if pixel == []:
		return ["default", "default"]


	if pixel2 == []:
		return ["default", "default"]
	avr2 = pixel2[random.randint(1, len(pixel2))]

	r_hex = (hex(avr[0])[2:len(str(hex(avr[0])))])
	g_hex = (hex(avr[1])[2:len(str(hex(avr[1])))])
	b_hex = (hex(avr[2])[2:len(str(hex(avr[2])))])
	
	if len(r_hex) < 2:
		r_hex = "10"
	if len(g_hex) < 2:
		g_hex = "10"
	if len(b_hex) < 2:
		b_hex = "10"

	r_hex2 = (hex(avr2[0])[2:len(str(hex(avr2[0])))])
	g_hex2 = (hex(avr2[1])[2:len(str(hex(avr2[1])))])
	b_hex2 = (hex(avr2[2])[2:len(str(hex(avr2[2])))])
	if len(r_hex2) < 2:
		r_hex = "10"
	if len(g_hex2) < 2:
		g_hex = "10"
	if len(b_hex2) < 2:
		b_hex = "10"

	return [ f"#{r_hex}{g_hex}{b_hex}", f"#{r_hex2}{g_hex2}{b_hex2}" ]