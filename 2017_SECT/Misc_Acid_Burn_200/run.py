from PIL import Image

img = Image.open('chall.webp')
res = Image.new('RGB', img.size)
px = img.load()
res_px = res.load()

for x in range(0, img.width):
	for y in range(0, img.height):
		
#		if px[x, y] != (0, 0, 0) and px[x, y] != (3, 3, 3) :
#			print(px[x, y])
		
		if px[x, y] == (3, 3, 3) or px[x, y] == (4, 3, 0):
			for xx in range(0, 4):
				for yy in range(0, 4):
					try:
						res_px[x+xx, y+yy] = (0, 255, 0)
					except:
						pass
		
		if px[x, y] == (4, 3, 0):
			for xx in range(0, 4):
				for yy in range(0, 4):
					try:
						res_px[x+xx, y+yy] = (255, 0, 0)
					except:
						pass
		
res.save("ans.png")