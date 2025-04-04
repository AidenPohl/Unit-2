from PIL import Image, ImageFilter

spheal = Image.open(r"Unit-2\Lesson 6\images.jpg")

image_size = spheal.size
print(image_size)

cropped_image = spheal.crop((110,0,318,159)).show()

bw_spheal = spheal.convert("L")

spheal_smooth = bw_spheal.filter(ImageFilter.SMOOTH)

spheal_edges = spheal_smooth.filter(ImageFilter.FIND_EDGES)

spheal_edge_enhance = spheal_edges.filter(ImageFilter.EDGE_ENHANCE)

spheal_edge_enhance.show()